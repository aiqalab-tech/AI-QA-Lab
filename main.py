from src.user_story_reader import read_user_story

file_path = "data/login_story.txt"

user_story = read_user_story(file_path)

print("AI QA Lab - Input User Story")
print("------------------------------")
print(user_story)