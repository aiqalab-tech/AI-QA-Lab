def generate_dom_locator(element):

    if element.id:
        return f'page.locator("#{element.id}")'

    elif element.name:
        return f'page.locator("[name=\\"{element.name}\\"]")'

    elif element.placeholder:
        return f'page.get_by_placeholder("{element.placeholder}")'

    elif element.text:
        return f'page.get_by_role("button", name="{element.text}")'

    else:
        return 'locator("UNKNOWN")'