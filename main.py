from src.user_story_reader import read_user_story
from src.requirement_analyzer import analyze_requirement
from src.test_case_generator import generate_test_cases

file_path = "data/login_story.txt"

user_story = read_user_story(file_path)
requirement = analyze_requirement(user_story)
test_cases = generate_test_cases(requirement)

print("AI QA Lab - Input User Story")
print("------------------------------")

for test_case in test_cases:
    print()
    print("Test Case ID:", test_case["id"])
    print("Scenario:", test_case["scenario"])
    print("Expected Result:", test_case["expected_result"])