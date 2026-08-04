from src.analyzers.application_analyzer import analyze_application
from src.analyzers.dom_parser import parse_dom
from src.analyzers.locator_discovery import discover_locator
from src.analyzers.screen_analyzer import analyze_screen

html = analyze_application(
    "https://parabank.parasoft.com"
)

elements = parse_dom(html)

print("\nDiscovered Elements")
print("--------------------------------")

for element in elements:

    locator = discover_locator(element)

    print(element)

    print(locator)

    print()

screen = analyze_screen(elements)

print("\nScreen Intelligence")
print("----------------------")

print(screen)