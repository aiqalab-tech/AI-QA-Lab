from playwright.sync_api import Page

from automation.playwright.pages.money_transfer_page import MoneyTransferPage

def test_money_transfer(page: Page):
    
    transaction_page = MoneyTransferPage(page)
    
    transaction_page.navigate()
    
    transaction_page.perform_transaction()
    
