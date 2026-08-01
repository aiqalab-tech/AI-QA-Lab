from src.readers.user_story_reader import read_user_story
from src.requirement_analyzer import analyze_requirement
from src.classifiers.requirement_classifier import classify_requirements
from src.generators.scenario_generator import generate_scenarios
from src.generators.professional_testcase_generator import generate_professional_test_cases
from src.formatters.test_case_formatter import format_test_case
from src.generators.feature_file_generator import (generate_feature_file, save_feature_file)


def main():

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

if __name__ == "__main__":
    main()