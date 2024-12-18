import streamlit as st
from utils import manage_subpages

st.set_page_config(
    page_title = "Home"
)

st.write("# Welcome to Golden Formulas! 👋")


st.markdown(
    """
    This is a one stop-shop for all Golden Formulas documented by José Costa.
    Enjoy as a 26-year old from Portugal documents his journey and what he learns along the way 😊

    Technical notes below 🗒️:
    * This web app is connected to his Notion workspace in real time meaning the content for these pages is dynamically generated via API calls
    * GitHub repository available [here](https://github.com/Ze1598/golden-formulas)
    
"""
)

# Create and delete local subpages to sync with pages available in Notion
manage_subpages()