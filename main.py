from src.user_story_reader import read_user_story
from src.requirement_analyzer import analyze_requirement

file_path = "data/login_story.txt"

user_story = read_user_story(file_path)
requirement = analyze_requirement(user_story)

print("AI QA Lab - Input User Story")
print("------------------------------")
print("Role   :", requirement["role"])
print("Action :", requirement["action"])
print("Goal   :", requirement["goal"])