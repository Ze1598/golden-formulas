import streamlit as st
import requests

NOTION_KEY = st.secrets["NOTION_KEY"]
BASE_PAGE_ID = "10f16f5e14c18095863ccadd6d9140de"

def get_child_pages(page_id, token):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28" 
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        child_pages = [
            block for block in data["results"]
            if block["type"] == "child_page"
        ]
        return child_pages
    else:
        print(f"Error: {response.status_code}")
        return None

def get_page_bullets(page_id, token):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28" 
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        child_pages = [
            block["bulleted_list_item"]["rich_text"][0]["plain_text"] for block in data["results"]
            if block["type"] == "bulleted_list_item"
        ]
        return child_pages
    else:
        print(f"Error: {response.status_code}")
        return None


if __name__ == "__main__":
    child_pages = get_child_pages(BASE_PAGE_ID, NOTION_KEY)

    formula_pages = {page["child_page"]["title"]: page["id"] for page in child_pages}

    print(formula_pages)

    formula_content = {formula: get_page_bullets(formula_pages[formula], NOTION_KEY) for formula in formula_pages}
    
    print(formula_content)