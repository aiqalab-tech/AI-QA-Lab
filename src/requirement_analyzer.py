def analyze_requirement(user_story):
    requirement = {
        "role": "",
        "action": "",
        "goal": ""
    }

    lines = user_story.split("\n")

    for line in lines:
        line = line.strip()

        if line.startswith("As a"):
            requirement["role"] = line.replace("As a", "").strip().strip(",")

        elif line.startswith("I want"):
            requirement["action"] = line.replace("I want to", "").strip()

        elif line.startswith("So that"):
            requirement["goal"] = line.replace("So that I can", "").strip().strip(".")

    return requirement