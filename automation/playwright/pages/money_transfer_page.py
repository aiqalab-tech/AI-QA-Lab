from playwright.sync_api import Page


class MoneyTransferPage:

    def __init__(self, page: Page):
        self.page = page


    def navigate(self):
        self.page.goto("https://parabank.parasoft.com")


    def perform_transaction(self):
        self.page.goto("https://parabank.parasoft.com")
        self.page.get_by_label("Transfer Amount").fill("1000")
        self.page.get_by_role("button", name="Transfer").click()
        self.page.get_by_label("OTP").fill("123456")
        self.page.get_by_role("button", name="Submit").click()

