from src.test_step_generator import generate_test_steps
from src.test_data_generator import generate_test_data
from src.expected_result_generator import generate_expected_result

def generate_professional_test_cases(feature, scenarios):

    test_cases = []

    counter = 1

    feature_config = {
        "Login": {
            "requirement_id": "Login_001",
            "module": "Login"
        },
        "Money Transfer": {
            "requirement_id": "Money_Transfer_001",
            "module": "Money Transfer"
        }
    }

    config = feature_config.get(feature)

    if config:
        requirement_id = config["requirement_id"]
        module = config["module"]
    else:
        requirement_id = "GEN_001"
        module = "General"

    for scenario in scenarios:

        steps = generate_test_steps(feature, scenario["type"])
        test_information = generate_test_data(feature, scenario["type"])
        expected_results = generate_expected_result(feature,scenario["type"]
        )

        test_case = {

            "test_case_id": f"TC00{counter}",

            "requirement_id": requirement_id,

            "scenario": scenario["title"],

            "module": module,

            "priority": "High",

            "test_type": scenario["type"],

            "automation_status": "Candidate",

            "preconditions": test_information["preconditions"],

            "test_data": test_information["test_data"],

            "test_steps": steps,

            "expected_result":expected_results

        }

        test_cases.append(test_case)

        counter += 1


    return test_cases