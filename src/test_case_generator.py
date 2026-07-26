def generate_test_cases(requirement):

    test_cases = [

        {
            "id": "TC001",
            "scenario": f"Verify successful {requirement['action']}",
            "expected_result": "User should complete the action successfully"
        },

        {
            "id": "TC002",
            "scenario": "Verify invalid credentials",
            "expected_result": "System should display an error message"
        },

        {
            "id": "TC003",
            "scenario": "Verify mandatory fields validation",
            "expected_result": "System should show validation message"
        }

    ]

    return test_cases