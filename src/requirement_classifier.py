from pyexpat import features


def classify_requirements(requirement):

    action = requirement["action"].lower()

    feature = "Unknown"

    if "login" in action or "log in" in action:
        feature = "Login"

    elif "transfer" in action or "send money" in action:
        feature = "Money Transfer"

    return feature

