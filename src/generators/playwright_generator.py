def generate_page_object(feature):

    class_name = feature.replace(" ", "") + "Page"

    page_code = f"""

from playwright.sync_api import Page

class {class_name}:

    def __init__(self, page: Page):
        self.page = page
        
    def navigate(self):
        self.page.goto("https://parabank.parasoft.com")
        
    def perform_transaction(self):
        pass

"""
    return page_code