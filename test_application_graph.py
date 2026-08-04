from src.knowledge.application_graph import ApplicationKnowledgeGraph

graph = ApplicationKnowledgeGraph()

graph.connect(
    "Money Transfer",
    "Transfer Page"
)

graph.connect(
    "Transfer Page",
    "Amount Field"
)

graph.connect(
    "Transfer Page",
    "Transfer Button"
)

graph.connect(
    "Transfer Page",
    "OTP Field"
)

graph.display()