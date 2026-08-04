from src.knowledge.application_graph import ApplicationKnowledgeGraph

class ApplicationModelBuilder:

    def __init__(self):
        self.graph = ApplicationKnowledgeGraph()

    def build(self, page_name, elements):

        self.graph.add_node(page_name)

        for element in elements:

            print(element)
            node_name = f"{element.tag}:{element.name or element.text or element.id}"

            self.graph.connect(page_name, node_name)

            if element.locator:
                self.graph.connect(node_name, element.locator)

        return self.graph