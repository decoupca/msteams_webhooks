"""Actions provide ways to interact with cards.

Not all actions defined in the Adaptive Card standard work with webhooks. Only those
actions which work with webhooks are implemented.
"""
from typing import Any, Optional

from msteams_webhooks import types
from msteams_webhooks.base import Entity


class Action(Entity):
    """Base action class."""


class OpenURLAction(Action):
    """Opens a URL when clicked or tapped.

    Schema Explorer: https://adaptivecards.io/explorer/Action.OpenUrl.html
    """

    def __init__(
        self,
        url: types.URL,
        *,
        title: Optional[str] = None,
    ) -> None:
        """Open a URL.

        When invoked, show the given url either by launching it in an external web browser
        or showing within an embedded web browser.

        Args:
            url: The URL to open.
            title: Label for button or link that represents this action.

        Returns:
            None.

        Raises:
            N/A
        """
        self.url = url
        self.title = title

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload: dict[str, Any] = {
            "type": "Action.OpenUrl",
            "url": self.url,
        }
        if self.title:
            payload["title"] = self.title
        return payload
