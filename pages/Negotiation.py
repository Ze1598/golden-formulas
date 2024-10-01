import streamlit as st
from notion_api import *
import os

page_name = os.path.basename(__file__).replace(".py", "")

st.set_page_config(
    page_title = page_name
)

st.markdown(f"# {page_name}")

child_pages = get_child_pages(BASE_PAGE_ID, NOTION_KEY)

formula_pages = {page["child_page"]["title"]: page["id"] for page in child_pages}

page_bullets = {formula: get_page_bullets(formula_pages[formula], NOTION_KEY) for formula in formula_pages}

display_string = "\n".join([f"* {bullet_item}" for bullet_item in page_bullets[page_name]])

st.markdown(display_string)