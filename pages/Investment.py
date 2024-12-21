
import streamlit as st
from classes.SubPage import SubPage
import os

# Get page name from script name
page_name = os.path.basename(__file__).replace(".py", "")

# Start class to handle Notion connectivity and content formatting
sub_page = SubPage(page_name)
# Tidy up content for page
display_string = sub_page.get_formatted_bullet_list()

# Streamlit page config
st.set_page_config(
    page_title = sub_page.get_page_name()
)

# Page header
st.markdown(f"# {sub_page.get_page_name()}")

# Page body
st.markdown(display_string)