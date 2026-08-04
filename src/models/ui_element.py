from dataclasses import dataclass

@dataclass
class UIElement:

    tag: str

    text: str

    id: str

    name: str

    label: str

    placeholder: str

    type: str

    locator: str
