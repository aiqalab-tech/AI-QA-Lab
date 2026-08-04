from src.analyzers.dom_parser import parse_dom
from src.knowledge.application_model_builder import ApplicationModelBuilder

html = """

<form>

<input name="username"/>

<input name="password" type="password"/>

<button>Log In</button>

</form>

"""

elements = parse_dom(html)

builder = ApplicationModelBuilder()

graph = builder.build("Login Page", elements)

graph.display()