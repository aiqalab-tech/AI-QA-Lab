from src.generators.playwright_action_generator import generate_playwright_actions

def generate_page_object(feature, test_steps):

    class_name = feature.replace(" ", "")

    actions = generate_playwright_actions(test_steps)

    action_code = ""

    for action in actions:
        action_code += f"\n        {action}"


    page_code = f"""from playwright.sync_api import Page


class {class_name}Page:

    def __init__(self, page: Page):
        self.page = page


    def navigate(self):
        self.page.goto("https://parabank.parasoft.com")


    def perform_transaction(self):{action_code}

"""

    return page_code