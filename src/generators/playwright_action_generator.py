from src.generators.locator_generator import generate_locator

def generate_playwright_actions(test_steps):

    actions = []

    for step in test_steps:

        step_lower = step.lower()

        if "login" in step_lower:
            actions.append('self.page.goto("https://parabank.parasoft.com")')

        elif "enter transfer amount" in step_lower:

            locator = generate_locator(step)
            actions.append(f'self.page.{locator}.fill("1000")')

        elif "click transfer" in step_lower:
            locator = generate_locator(step)
            actions.append(f'self.page.{locator}.click()')

        elif "enter otp" in step_lower:
            locator = generate_locator(step)
            actions.append(f'self.page.{locator}.fill("123456")')

        elif "submit" in step_lower:
            locator = generate_locator(step)
            actions.append(f'self.page.{locator}.click()')

    return actions