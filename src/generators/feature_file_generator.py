def generate_feature_file(feature_name, scenarios):
    """
    Generate Gherkin feature content from scenarios.
    """

    feature_text = f"Feature: {feature_name}\n\n"

    for scenario in scenarios:

        feature_text += f"  Scenario: {scenario['title']}\n"

        scenario_type = scenario["type"]

        if scenario_type == "Positive":

            feature_text += (
                "   Given the customer is logged into ParaBank\n"
                "   And the customer has sufficient balance\n"
                "   When the customer performs the transaction\n"
                "   Then the transaction should be completed successfully\n\n"
            )

        elif scenario_type == "Negative":

            feature_text += (
                "   Given the customer is logged into ParaBank\n"
                "   When the customer performs an invalid transaction\n"
                "   Then an appropriate error message should be displayed\n\n"
            )

        elif scenario_type == "Validation":

            feature_text += (
                "   Given the customer is on the transaction page\n"
                "   When invalid input is entered\n"
                "   Then validation messages should be displayed\n\n"
            )

        elif scenario_type == "Security":

            feature_text += (
                "   Given the customer initiates a secure transaction\n"
                "   When an invalid OTP is entered\n"
                "   Then the transaction should be rejected\n\n"
            )

    return feature_text

def save_feature_file(feature_name, feature_text):

    file_name = feature_name.lower().replace(" ", "_") + ".feature"

    file_path = f"output/feature_files/{file_name}"

    with open(file_path, "w") as file:
        file.write(feature_text)

    print(f"\nFeature file created successfully:\n{file_path}")
