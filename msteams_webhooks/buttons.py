"""msteams_webhooks.buttons."""
from typing import Any

from msteams_webhooks import types


class Button:
    """Base button class."""

    def serialize(self) -> dict:
        """Serialize object into data structure."""
        return {}


class OpenURLButton(Button):
    """Open a URL."""

    def __init__(self, url: types.URL, title: str) -> None:
        """Open a URL.

        Args:
            url: URL to open.
            title: Label that represents this button.

        Returns:
            None.

        Raises:
            N/A
        """
        self.title = title
        self.url = url

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        return {"type": "openUrl", "title": self.title, "value": self.url}
