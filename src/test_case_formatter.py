def format_test_case(test_case):

    preconditions = ""

    for item in test_case["preconditions"]:
        preconditions += f"- {item}\n"

    test_data = ""

    for key, value in test_case["test_data"].items():
        test_data += f"{key}: {value}\n"

    test_steps = ""

    for index, step in enumerate(test_case["test_steps"], start=1):
        test_steps += f"{index}. {step}\n"

    expected_result = ""

    for item in test_case["expected_result"]:
        expected_result += f"- {item}\n"

    formatted_output = f"""
=====================================
          TEST CASE REPORT
=====================================

Test Case ID: 
{test_case['test_case_id']}

Requirement ID: 
{test_case['requirement_id']}

Scenario:
{test_case['scenario']}

Module:
{test_case['module']}

Priority:
{test_case['priority']}

Test Type:
{test_case['test_type']}

Automation Status:
{test_case['automation_status']}

Preconditions:
{preconditions}

Test Data:
{test_data}

Test Steps:
{test_steps}

Expected Results:
{expected_result}

=====================================
"""

    return formatted_output