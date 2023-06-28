"""Buttons are interactive elements available to use in Hero Cards."""
from typing import Any, Optional

from msteams_webhooks.base import Entity


class Button(Entity):
    """Base button class."""


class OpenURLButton(Button):
    """Button that opens a URL when clicked or tapped."""

    def __init__(self, url: str, title: str, *, image: Optional[str] = None) -> None:
        """Open a URL.

        Args:
            url: URL to open.
            title: Label that represents this button.
            image: URL to image representing the button.

        Returns:
            None.

        Raises:
            N/A
        """
        self.title = title
        self.url = url
        self.image = image

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload: dict[str, Any] = {"type": "openUrl", "title": self.title, "value": self.url}
        if self.image:
            payload["image"] = self.image
        return payload
