from typing import Optional

from msteams_webhooks import types


class Action:
    """Base action class."""

    def serialize(self) -> dict:
        """Serialize object into data structure."""
        pass


class OpenURLAction(Action):
    """Open URL action.

    https://adaptivecards.io/explorer/Action.OpenUrl.html
    """

    def __init__(
        self,
        url: types.URL,
        *,
        title: Optional[str] = None,
    ) -> None:
        self.url = url
        self.title = title

    def serialize(self) -> dict:
        payload = {
            "type": "Action.OpenUrl",
            "url": self.url,
        }
        if self.title:
            payload["title"] = self.title
        return payload
