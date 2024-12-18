import streamlit as st
from classes.NotionApi import NotionApi
import os

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

# Check for new pages to be created
# Which pages exist at source
notion_api = NotionApi()
pages_available = list(notion_api.available_child_pages.keys())

# Which pages exist locally
local_pages_files = os.listdir(os.path.join(os.getcwd(), "pages"))
local_pages = [page.replace(".py", "") for page in local_pages_files]

# Which pages to be created
missing_pages = [page for page in pages_available if page not in local_pages]
for page in missing_pages:
    subpage_code = """import streamlit as st
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
st.markdown(display_string)"""

    subpage_name = f"{page}.py"
    out_path = os.path.join(os.getcwd(), "pages", subpage_name)
    with open(out_path, "w") as f:
        f.write(subpage_code)