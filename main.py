import os

from src.readers.user_story_reader import read_user_story
from src.requirement_analyzer import analyze_requirement
from src.classifiers.requirement_classifier import classify_requirements
from src.generators.scenario_generator import generate_scenarios
from src.generators.professional_testcase_generator import generate_professional_test_cases
from src.formatters.test_case_formatter import format_test_case
from src.generators.feature_file_generator import (generate_feature_file, save_feature_file)
from src.generators.playwright_generator import generate_page_object
from src.generators.playwright_test_generator import generate_test_file
from src.runners.playwright_runner import run_playwright_test

def main():

    os.makedirs(
        "automation/playwright/pages",
        exist_ok=True
    )

    os.makedirs(
        "automation/playwright/tests",
        exist_ok=True
    )

    print("AI QA Lab - Input User Story")
    print("------------------------------")

    # Step 1: Read User Story
    #story = read_user_story("data/login_story.txt")
    print("\nPlease enter your user story")
    print("------------------------------")
    print("1. Login")
    print("2. Money Transfer")

    choice = input("Enter your choice: ")

    if choice == "1":
        user_story = read_user_story("data/login_story.txt")
    elif choice == "2":
        user_story = read_user_story("data/money_transfer_story.txt")
    else:
        print("Invalid choice")
        return

    # Step 2: Analyze Requirement
    requirement = analyze_requirement(user_story)

    feature = classify_requirements(requirement)

    print("\nDetected Feature")
    print("------------------------------")
    print(feature)

    # Step 3: Generate Scenarios
    scenarios = generate_scenarios(feature)
    print("\nGenerated Scenarios")
    print("------------------------------")

    for scenario in scenarios:
        print(scenario)

    # Step 4: Generate Professional Test Cases
    professional_test_cases = generate_professional_test_cases(feature, scenarios)

    print("\nProfessional Test Case Report")
    print("------------------------------")

    for test_case in professional_test_cases:
        report = format_test_case(test_case)
        print(report)

    # -----------------------------------------
    # Generate Feature File
    # -----------------------------------------
    feature_text = generate_feature_file(feature,scenarios)
    save_feature_file(feature, feature_text)

    print("BDD Feature File generated successfully.")

    # -----------------------------------------
    # Generate Playwright Automation Assets
    # -----------------------------------------
    print("\nGenerating Playwright Automation Assets...")

    page_object_code = generate_page_object(feature, professional_test_cases[0]["test_steps"])
    test_code = generate_test_file(feature)

    page_file = (
        f"automation/playwright/pages/"
        f"{feature.lower().replace(' ','_')}_page.py"
    )

    test_file = (
        f"automation/playwright/tests/"
        f"test_{feature.lower().replace(' ','_')}.py"
    )

    with open(page_file, "w") as file:
        file.write(page_object_code)


    with open(test_file, "w") as file:
        file.write(test_code)

    print("Playwright files generated successfully.")

    # -----------------------------------------
    # Execute Generated Playwright Test
    # -----------------------------------------

    print("\nExecuting Playwright Test...")
    print("------------------------------")

    result = run_playwright_test("automation/playwright/tests/test_money_transfer.py")

    print("\nExecution Status")
    print("------------------------------")
    print(result["status"])

    print("\nExecution Output")
    print("------------------------------")
    print(result["output"])

if __name__ == "__main__":
    main()