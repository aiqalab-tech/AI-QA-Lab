def generate_playwright_actions(test_steps):

    actions = []

    for step in test_steps:

        step_lower = step.lower()

        if "login" in step_lower:
            actions.append('self.page.goto("https://parabank.parasoft.com")')

        elif "enter transfer amount" in step_lower:
            actions.append('self.page.fill("#amount", "1000")')

        elif "click transfer" in step_lower:
            actions.append('self.page.click("#transfer")')

        elif "enter otp" in step_lower:
            actions.append('self.page.fill("#otp", "123456")')

        elif "submit" in step_lower:
            actions.append('self.page.click("#submit")')

    return actions