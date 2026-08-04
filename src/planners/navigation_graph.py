
class NavigationGraph:

    def __init__(self):
        self.graph = {}

    def add_page(self, page):

        if page not in self.graph:
            self.graph[page] = []

    def add_connection(self, source, destination):

        self.add_page(source)
        self.add_page(destination)

        self.graph[source].append(destination)

    def get_next_pages(self, page):

        return self.graph.get(page, [])

    def display(self):

        print("\nNavigation Graph")
        print("--------------------------")

        for page, links in self.graph.items():

            print("Page:", page)

            for link in links:

                print(f"    └──► {link}")