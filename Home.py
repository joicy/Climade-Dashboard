import streamlit as st
from source.pages.header import *
from config import *
from utils.functions import *

st.set_page_config(
        page_title="CLIMADE AFRICA DASHBOARD",
        layout="wide",
        initial_sidebar_state="expanded",
        page_icon="img/cropped-ceri_branco-01-150x150.png"
    )

st.markdown(css_changes, unsafe_allow_html=True)
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

text = """# CLIMADE AFRICA DASHBOARD\n**INTERPRET THIS DATA WITH CARE:**\n
       \nThe data displayed on the dashboard is sourced from [BV-BRC](https://www.bv-brc.org/).
       Figures on the dashboard were inspired by [Wilkinson et al. Science 2021](https://www.science.org/doi/full/10.1126/science.abj4336).\n
       \n The CLIMADE Africa dashboard was built using the SARS-CoV-2 Africa dashboard computational architecture [Cite us](https://www.nature.com/articles/s41564-022-01276-9).\n
       \n**CONTACT US:**\n- Email: 21618488@sun.ac.za\n- Email: joicy.xavier@ufvjm.edu.br
       """

st.write(text)

st.sidebar.success("Select an arbovirus above.")