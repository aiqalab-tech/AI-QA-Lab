def generate_locator(action_text):

    action = action_text.lower()

    if "amount" in action:
        return 'get_by_label("Transfer Amount")'

    elif "transfer" in action:
        return 'get_by_role("button", name="Transfer")'

    elif "otp" in action:
        return 'get_by_label("OTP")'

    elif "submit" in action:
        return 'get_by_role("button", name="Submit")'

    else:
        return 'locator("UNKNOWN")'