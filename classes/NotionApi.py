import streamlit as st
import requests

class NotionApi:

    NOTION_KEY = st.secrets["NOTION_KEY"]
    BASE_PAGE_ID = "10f16f5e14c18095863ccadd6d9140de"

    def __init__(self):
        # Dict of child_page_name: child_page_id
        self.available_child_pages = self.get_child_pages()

    def get_child_pages(self):
        """
        Get a dictionary of child_page_name: child_page_id
        """
        url = f"https://api.notion.com/v1/blocks/{self.BASE_PAGE_ID}/children"
        headers = {
            "Authorization": f"Bearer {self.NOTION_KEY}",
            "Notion-Version": "2022-06-28" 
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            child_pages = [
                block for block in data["results"]
                if block["type"] == "child_page"
            ]

            # De-nest all the JSON to map child page title to child page id
            formula_pages = {page["child_page"]["title"]: page["id"] for page in child_pages}

            return formula_pages
        else:
            print(f"Error: {response.status_code}")
            return None

    def get_page_bullets(self, page_id):
        """
        Get a list of the bullet points from the given page id.
        """
        url = f"https://api.notion.com/v1/blocks/{page_id}/children"
        headers = {
            "Authorization": f"Bearer {self.NOTION_KEY}",
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
    notion_api = NotionApi()

    formula_pages = notion_api.get_child_pages()

    print(formula_pages)

    formula_content = {formula: notion_api.get_page_bullets(formula_pages[formula]) for formula in formula_pages}
    
    print(formula_content)