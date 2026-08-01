from playwright.sync_api import Page


class MoneyTransferPage:

    def __init__(self, page: Page):
        self.page = page


    def navigate(self):
        self.page.goto("https://parabank.parasoft.com")


    def perform_transaction(self):
        self.page.goto("https://parabank.parasoft.com")
        self.page.fill("#amount", "1000")
        self.page.click("#transfer")
        self.page.fill("#otp", "123456")
        self.page.click("#submit")

