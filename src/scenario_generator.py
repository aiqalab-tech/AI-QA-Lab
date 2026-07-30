def generate_scenarios(requirement):

    requirement_text = requirement['action'].lower()

    if "login" in requirement_text or "log in" in requirement_text:
        print("Login feature detected")

    scenarios = [
        {
            "id": "SC001",
            "type": "Positive",
            "title": "Verify successful login with valid credentials"
        },
        {
            "id": "SC002",
            "type": "Negative",
            "title": "Verify login fails with invalid password"
        },
        {
            "id": "SC003",
            "type": "Validation",
            "title": "Verify mandatory login fields validation"
        },
        {
            "id": "SC004",
            "type": "Security",
            "title": "Verify account lock after multiple failed login attempts"
        }
    ]

    return scenarios