from src.user_story_reader import read_user_story
from src.requirement_analyzer import analyze_requirement
from src.scenario_generator import generate_scenarios
from src.professional_testcase_generator import generate_professional_test_cases
from src.test_case_formatter import format_test_case


def main():

    file_path = "data/login_story.txt"

    print("AI QA Lab - Input User Story")
    print("------------------------------")

    # Step 1: Read User Story
    story = read_user_story(file_path)

    # Step 2: Analyze Requirement
    requirement = analyze_requirement(story)

    # Step 3: Generate Scenarios
    scenarios = generate_scenarios(requirement)

    print("\nGenerated Scenarios")
    print("------------------------------")

    for scenario in scenarios:
        print(scenario)

    # Step 4: Generate Professional Test Cases
    professional_test_cases = generate_professional_test_cases(scenarios)

    print("\nProfessional Test Case Report")
    print("------------------------------")

    for test_case in professional_test_cases:
        report = format_test_case(test_case)
        print(report)


if __name__ == "__main__":
    main()