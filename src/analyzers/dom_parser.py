from bs4 import BeautifulSoup
from src.models.ui_element import UIElement
from src.analyzers.dom_locator_generator import generate_dom_locator

def parse_dom(html):

    soup = BeautifulSoup(html, "html.parser")

    elements = []

    # -------------------------
    # Input Fields
    # -------------------------
    for tag in soup.find_all("input"):

        input_type = tag.get("type", "")

        if input_type == "submit":

            element = UIElement(
                tag="button",
                text=tag.get("value", ""),
                id=tag.get("id", ""),
                name=tag.get("name", ""),
                label="",
                placeholder="",
                type="submit",
                locator=""
            )
        else:
            element = UIElement(
                tag="input",
                text="",
                id=tag.get("id", ""),
                name=tag.get("name", ""),
                label="",
                placeholder=tag.get("placeholder", ""),
                type=tag.get("type", ""),
                locator=""
            )

        # Generate locator
        element.locator = generate_dom_locator(element)

        elements.append(element)

    # -------------------------
    # Buttons
    # -------------------------
    for tag in soup.find_all("button"):

        element = UIElement(
            tag="button",
            text=tag.get_text(strip=True),
            id=tag.get("id", ""),
            name=tag.get("name", ""),
            label="",
            placeholder="",
            type="button",
            locator=""
        )

        # Generate locator
        element.locator = generate_dom_locator(element)

        elements.append(element)

    return elements