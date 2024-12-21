from classes.NotionApi import NotionApi
import os

def manage_subpages():
    """
    Create new subpages on the app based on which Golden Formulas pages exist in Notion.
    And delete subpages in the app for pages that no longer exist in Notion.
    """
    # Check for new pages to be created
    # Which pages exist at source
    notion_api = NotionApi()
    pages_available = list(notion_api.available_child_pages.keys())

    print(f"Pages available in Notion: {pages_available}")

    # Which pages exist locally
    local_pages_files = os.listdir(os.path.join(os.getcwd(), "pages"))
    local_pages = [page.replace(".py", "") for page in local_pages_files if page != ".gitkeep"]
    print(f"Pages available locally: {local_pages}")

    # Which pages to be created
    missing_pages = [page for page in pages_available if page not in local_pages]
    for page in missing_pages:
        subpage_code = """
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
st.markdown(display_string)"""

        subpage_name = f"{page}.py"
        out_path = os.path.join(os.getcwd(), "pages", subpage_name)
        with open(out_path, "w") as f:
            print(f"Created page {subpage_name}")
            f.write(subpage_code)

    todelete_pages = [page for page in local_pages if page not in pages_available]
    for page in todelete_pages:
        subpage_name = f"{page}.py"
        out_path = os.path.join(os.getcwd(), "pages", subpage_name)
        print(f"Deleted page {subpage_name}")
        os.remove(out_path)