def format_test_case(test_case):

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

=====================================
"""

    return formatted_output