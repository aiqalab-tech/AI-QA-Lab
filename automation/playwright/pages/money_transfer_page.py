from playwright.sync_api import Page

class MoneyTransferPage:

    def __init__(self, page: Page):
        self.page = page
        
    def navigate(self):
        self.page.goto("https://parabank.parasoft.com")
        
    def perform_transaction(self):
        pass

