def generate_expected_result(feature, scenario_type):

    if feature == "Login":

        if scenario_type == "Positive":
            return [
                "User should login successfully",
                "Account dashboard should be displayed"
            ]

        elif scenario_type == "Negative":
            return [
                "System should display invalid credentials message",
                "User should not be logged in"
            ]

        elif scenario_type == "Validation":
            return [
                "System should display mandatory field validation message"
            ]

        elif scenario_type == "Security":
            return [
                "Account should be locked after multiple failed attempts",
                "Security message should be displayed"
            ]


    elif feature == "Money Transfer":

        if scenario_type == "Positive":
            return [
                "Transaction should complete successfully",
                "Transaction reference number should be generated",
                "Account balance should be updated"
            ]


        elif scenario_type == "Negative":
            return [
                "System should display insufficient balance message",
                "Transaction should not be processed",
                "Account balance should remain unchanged"
            ]


        elif scenario_type == "Validation":
            return [
                "System should display transfer amount validation message",
                "Transaction should not be submitted"
            ]


        elif scenario_type == "Security":
            return [
                "System should reject invalid OTP",
                "Transaction should not be completed",
                "Security error message should be displayed"
            ]


    return [
        "System should perform expected behavior"
    ]