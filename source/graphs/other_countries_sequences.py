import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import timedelta, datetime

from utils.dicts import main_lineages_color_scheme


def other_countries_with_sequences_chart(df_count, column, color_function, legend_title):
    c = column
    df_country_lineages = df_count.copy()

    df_country_lineages['date_initial'] = pd.to_datetime(df_country_lineages['date_2weeks']) - timedelta(days=14)
    df_country_lineages['date_initial'] = df_country_lineages['date_initial'].dt.strftime('%Y')

    df_country_lineages['date_final'] = pd.to_datetime(df_country_lineages['date_2weeks']).dt.strftime('%Y')

    ##### Processing df to show prevalent lineage
    # Total genomes column
    df_country_lineages['total_genomes'] = df_country_lineages.groupby(['country', 'date_2weeks'])['Count']\
        .transform('sum')

    # counting genomes per lineage
    df_country_lineages['lineage'] = df_country_lineages[['country', 'lineage', 'date_2weeks', 'Count']].groupby(['country', 'date_2weeks'])['lineage']\
    .transform(lambda x: ', '.join(x))

    df_country_lineages['counts_per_lineage'] = df_country_lineages[
        ['country', 'lineage', 'date_2weeks', 'Count']].groupby(
        ['country', 'date_2weeks', 'lineage'])['Count'].transform(lambda x: ', '.join(x.astype(str)))

    genomes_per_lineage = []
    for index, row in df_country_lineages.iterrows():
        label = ', '.join(' : '.join(x) for x in zip(row['lineage'].split(','), row['counts_per_lineage'].split(',')))
        genomes_per_lineage.append(label)

    df_country_lineages['genomes_per_lineage'] = genomes_per_lineage

    df_country_lineages = df_country_lineages.drop_duplicates(subset=["country", "date_2weeks", "genomes_per_lineage"])

    # Determining prevalent lineage per date and country
    prevalent_lineage = []
    for index, row in df_country_lineages.iterrows():
        a = row['genomes_per_lineage']
        genomes_per_lineage_dict = dict((x.strip(), int(y.strip()))
                                        for x, y in (element.split(' : ')
                                                     for element in a.split(', ')))
        prevalent_lineage.append(max(genomes_per_lineage_dict, key=genomes_per_lineage_dict.get))

    df_country_lineages['prevalent_lineage'] = prevalent_lineage

    df_country_lineages.drop(['lineage', 'Count', 'counts_per_lineage', ], axis=1, inplace=True)

    with st.container():
        c.subheader("Sequence data available per country")

        country_lineages = px.strip(df_country_lineages.sort_values('total_genomes', ascending=False),
                                    x="date_2weeks", y='country',
                                    color="prevalent_lineage",
                                    title= '    ',
                                    custom_data=['country','date_2weeks', 'prevalent_lineage', 'total_genomes',
                                                 'genomes_per_lineage', 'date_initial', 'date_final'],
                                    color_discrete_map=color_function,
                                    stripmode='group').update_traces(jitter=1)
        country_lineages.update_traces(marker=dict(size=13, line=dict(width=0.5, color='#E5ECF6')))
        country_lineages.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1,
            xanchor="right",
            x=1
        ), legend_title_text=legend_title)
        country_lineages.update_layout(title=dict(y=1), yaxis={'categoryorder': 'category descending'})
        country_lineages.update_yaxes(title="Country")
        country_lineages.update_xaxes(title="Date", range=[df_country_lineages['date_2weeks'].min(), datetime.today()])

        # creating standardize hover template
        custom_hovertemplate = '<b>Country: %{customdata[0]} <br>' + \
                                'Date: %{customdata[5]} to %{customdata[6]} <br>' +\
                                'Total number of genomes: %{customdata[3]} </b><br>' +\
                                'Genomes per genotype: %{customdata[4]} <br>'

        country_lineages.update_traces(hovertemplate=custom_hovertemplate)

        for frame in country_lineages.frames:
            for data in frame.data:
                data.hovertemplate = custom_hovertemplate

        country_lineages.update_layout(hovermode="closest")

        c.plotly_chart(country_lineages, use_container_width=True)

def countries_with_sequences_chart_one_variant(df_count, column, variant, start_date, color):
    c = column
    df_country_lineages = df_count[df_count['variant'].isin(variant)]

    df_country_lineages['date_initial'] = pd.to_datetime(df_country_lineages['date_2weeks']) - timedelta(days=14)
    df_country_lineages['date_initial'] = df_country_lineages['date_initial'].dt.strftime('%Y-%m-%d')

    with st.container():
        country_lineages = px.strip(df_country_lineages.sort_values(by='variant', ascending=False), x="date_2weeks",
                                      y="country", color="variant", custom_data=['country','variant', 'date_2weeks', 'Count'],
                                      color_discrete_map=color)
        country_lineages.update_traces(marker=dict(size=13, line=dict(width=0.5, color='#E5ECF6')))
        country_lineages.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1,
            xanchor="right",
            x=1
        ), legend_title_text="Variants")
        country_lineages.update_layout(title=dict(y=1), yaxis={'categoryorder': 'category descending'})
        country_lineages.update_yaxes(title="Country")
        country_lineages.update_xaxes(title="Date", range=[start_date, datetime.today()])

        # creating standardize hover template
        custom_hovertemplate = '<b>Country: %{customdata[0]} </b><br><br>' + \
                               'Variant: %{customdata[1]} <br>Date: %{customdata[2]} <br>' + \
                               'Genomes: %{customdata[3]} <br>'

        country_lineages.update_traces(hovertemplate=custom_hovertemplate)

        for frame in country_lineages.frames:
            for data in frame.data:
                data.hovertemplate = custom_hovertemplate

        c.plotly_chart(country_lineages, use_container_width=True)