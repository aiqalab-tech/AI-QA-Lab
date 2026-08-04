def plan_workflow(feature):

    workflow = {

        "Login": [
            "Open Login Page",
            "Enter Username",
            "Enter Password",
            "Click Login",
            "Verify Dashboard"
        ],

        "Money Transfer": [
            "Login",
            "Open Transfer Funds",
            "Select From Account",
            "Select To Account",
            "Enter Amount",
            "Submit Transfer",
            "Verify Success"
        ]

    }

    return workflow.get(feature, [])