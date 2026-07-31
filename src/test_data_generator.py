def generate_test_data(feature, scenario_type):

    if feature == "Login":

        return {
            "preconditions": [
                "User account exists",
                "Banking application is available"
            ],
            "test_data": {
                "username": "valid_username",
                "password": "valid_password"
            }
        }

    elif feature == "Money Transfer":

        if scenario_type == "Positive":

            return {
                "preconditions": [
                    "User account exists",
                    "User is logged into application",
                    "Beneficiary is registered"
                ],
                "test_data": {
                    "beneficiary": "John",
                    "transfer_amount": "1000",
                    "otp": "valid OTP"
                }
        }

        elif scenario_type == "Negative":

            return {
                "preconditions": [
                    "User account exists",
                    "User is logged into application",
                    "Account balance is insufficient"
                ],
                "test_data": {
                    "beneficiary": "John",
                    "transfer_amount": "50000 INR",
                    "available_balance": "1000 INR"
                }
            }

        elif scenario_type == "Validation":

            return {
                "preconditions": [
                    "User is logged into application"
                ],
                "test_data": {
                    "transfer_amount": "0 or blank"
                }
            }


        elif scenario_type == "Security":

            return {
                "preconditions": [
                    "User initiated money transfer"
                ],
                "test_data": {
                    "otp": "Invalid OTP"
                }
            }

    return {
        "preconditions": [],
        "test_data": {}
    }