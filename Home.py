import streamlit as st
from notion_api import *
import json
import time

st.set_page_config(
    page_title = "Home"
)

st.write("# Welcome to Golden Formulas! 👋")


st.markdown(
    """
    This is a one stop-shop for all Golden Formulas documented by José Costa.
    Enjoy as a 26-year old from Portugal documents his journey and what he learns along the way 😊

    Technical note: this web app is directly connected to his Notion workspace meaning the content for these pages is dynamically generated via API calls - both the available pages and their content.
"""
)