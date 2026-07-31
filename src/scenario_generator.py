def generate_scenarios(feature):

    #requirement_text = requirement['action'].lower()

    #if "login" in requirement_text or "log in" in requirement_text:
    #    print("Login feature detected")

    scenarios = []

    if feature == "Login":

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

    elif feature == "Money Transfer":
        scenarios = [
            {
                "id": "SC001",
                "type": "Positive",
                "title": "Verify successful money transfer with valid beneficiary"
            },
            {
                "id": "SC002",
                "type": "Negative",
                "title": "Verify transfer fails with insufficient balance"
            },
            {
                "id": "SC003",
                "type": "Validation",
                "title": "Verify transfer amount validation"
            },
            {
                "id": "SC004",
                "type": "Security",
                "title": "Verify OTP validation during money transfer"
            }
        ]
    return scenarios