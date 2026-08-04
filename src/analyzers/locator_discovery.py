from src.models.ui_element import UIElement

def discover_locator(element: UIElement):

    # Highest priority
    if element.id:
        return f'page.locator("#{element.id}")'

    # Second priority
    if element.name:
        return f'page.locator("[name=\\"{element.name}\\"]")'

    # Third priority
    if element.label:
        return f'page.get_by_label("{element.label}")'

    # Forth priority
    if element.placeholder:
        return f'page.get_by_placeholder("{element.placeholder}")'

    # Fifth priority
    if element.tag == "button" and element.text:
        return f'page.get_by_role("button", name="{element.text}")'

    return "Locator not found"