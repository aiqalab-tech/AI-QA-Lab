def generate_professional_test_cases(scenarios):

    test_cases = []

    counter = 1

    for scenario in scenarios:

        test_case = {

            "test_case_id": f"TC00{counter}",

            "requirement_id": "Login_001",

            "scenario": scenario["title"],

            "module": "Login",

            "priority": "High",

            "test_type": scenario["type"],

            "automation_status": "Candidate",

            "preconditions": [
                "Application is available",
                "User account exists"
            ],

            "test_steps": [
                "Open application",
                "Perform required action"
            ],

            "expected_result":
                "System should behave as expected"

        }

        test_cases.append(test_case)

        counter += 1


    return test_cases