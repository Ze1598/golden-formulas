from classes.NotionApi import NotionApi

class SubPage(NotionApi):
    def __init__(self, page_name):
        # Instantiate parent class to have access to the init attributes
        NotionApi.__init__(self)
        self.page_name = page_name
        self.page_id = self.available_child_pages[self.page_name]
        self.page_bullets_list = super().get_page_bullets(self.page_id)

    def get_page_name(self):
        return self.page_name
    
    def get_page_id(self):
        return self.page_id
    
    def get_page_bullet_list(self):
        return self.page_bullets_list
    
    def get_formatted_bullet_list(self):
        return "\n".join([f"* {bullet_item}" for bullet_item in self.page_bullets_list])


if __name__ == "__main__":
    sub_page = SubPage("Negotiation")

    print(sub_page.get_page_name())
    print(sub_page.get_page_id())

    print(sub_page.get_formatted_bullet_list())