def read_user_story(file_path):
    with open(file_path, "r") as file:
        user_story = file.read()

    return user_story
