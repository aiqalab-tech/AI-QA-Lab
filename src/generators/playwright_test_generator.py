def generate_test_file(feature):

    class_name = feature.replace(" ", "") + "Page"
    test_name = feature.lower().replace(" ", "_")

    test_code = f"""

from playwright.sync_api import Page
from automation.playwright.pages.{test_name}_page import {feature.replace(" ", "")}Page

def test_{test_name}(page: Page):
    
    transaction_page = {class_name}(page)
    
    transaction_page.navigate()
    
    transaction_page.perform_transaction()
    
"""
    return test_code