class ApplicationKnowledgeGraph:

    def __init__(self):
        self.graph = {}

    def add_node(self, node):

        if node not in self.graph:
            self.graph[node] = []

    def connect(self, source, destination):

        self.add_node(source)
        self.add_node(destination)

        self.graph[source].append(destination)

    def display(self):

        print("\nApplication Knowledge Graph")
        print("--------------------------------")

        for node, children in self.graph.items():

            if not children:
                continue

            print(node)

            for child in children:
                print(f"   └──► {child}")