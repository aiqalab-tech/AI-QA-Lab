from src.planners.navigation_graph import NavigationGraph

graph = NavigationGraph()

graph.add_connection(
    "Login",
    "Accounts Overview"
)

graph.add_connection(
    "Accounts Overview",
    "Transfer Funds"
)

graph.add_connection(
    "Accounts Overview",
    "Bill Pay"
)

graph.add_connection(
    "Accounts Overview",
    "Request Loan"
)

graph.display()