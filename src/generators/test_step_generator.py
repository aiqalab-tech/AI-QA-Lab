def generate_test_steps(feature, scenario_type):

    if feature == "Login":

        if scenario_type == "Positive":
            return [
                "Open the banking application",
                "Enter valid username",
                "Enter valid password",
                "Click Login"
            ]

        elif scenario_type == "Negative":
            return [
                "Open the banking application",
                "Enter valid username",
                "Enter invalid password",
                "Click Login"
            ]

    elif feature == "Money Transfer":

        if scenario_type == "Positive":
            return [
                "Login to application",
                "Navigate to Money Transfer",
                "Select beneficiary",
                "Enter transfer amount",
                "Click Transfer",
                "Enter OTP",
                "Submit transaction"
            ]

        elif scenario_type == "Negative":
            return [
                "Login to application",
                "Navigate to Money Transfer",
                "Select beneficiary",
                "Enter amount greater than balance",
                "Click Transfer"
            ]

        elif scenario_type == "Validation":
            return [
                "Login to application",
                "Navigate to Money Transfer",
                "Enter invalid transfer amount",
                "Click Transfer",
                "Verify validation message"
            ]

        elif scenario_type == "Security":
            return [
                "Login to application",
                "Navigate to Money Transfer",
                "Initiate money transfer",
                "Enter incorrect OTP",
                "Verify security error message"
            ]

    return [
        "Test steps not available"
    ]