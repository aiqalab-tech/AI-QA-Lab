# AI QA Lab - Step 1
# Read user story from file

file_path = "data/login_story.txt"

with open(file_path, "r") as file:
    user_story = file.read()

print("AI QA Lab - Input User Story")
print("------------------------------")
print(user_story)