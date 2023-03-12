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

st.write("#  Welcome to CLIMADE AFRICA DASHBOARD! 👋")

st.sidebar.success("Select an arbovirus above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)