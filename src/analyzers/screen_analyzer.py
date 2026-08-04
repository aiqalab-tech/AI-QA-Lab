def analyze_screen(elements):

    names = []

    for element in elements:

        if element.name:
            names.append(element.name.lower())

        if element.text:
            names.append(element.text.lower())

    # Login Screen
    if(
        "username" in names and
        "password" in names
    ):
        return {
            "screen_name": "Login Screen",
            "purpose": "User Authentication"
        }

    # Money Transfer
    if(
        "amount" in names and
        "transfer" in names
    ):
        return {
            "screen_name": "Money Transfer",
            "purpose": "Fund Transfer"
        }

    return {
        "screen_name": "UNKNOWN",
        "purpose": "UNKNOWN"
    }