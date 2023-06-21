class Button:
    def serialize(self) -> dict:
        pass


class OpenURLButton(Button):
    button_type = "openUrl"

    def __init__(self, title: str, url: str) -> None:
        self.title = title
        self.url = url

    def serialize(self) -> dict:
        return {"type": self.button_type, "title": self.title, "value": self.url}
