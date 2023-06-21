from typing import Optional

from msteams_webhooks.buttons import Button
from msteams_webhooks.types import URL


class Card:
    content_type = ""
    schema = ""

    def serialize(self) -> dict:
        pass


class AdaptiveCard(Card):
    schema = "http://adaptivecards.io/schemas/adaptive-card.json"
    card_type = "AdaptiveCard"

    def __init__(self) -> None:
        self.body = []
        self.actions = []

    def serialize(self) -> dict:
        payload = {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "$schema": self.schema,
                "type": self.card_type,
                "version": "1.5",
            },
        }
        if self.body:
            payload["content"]["body"] = [x.serialize() for x in self.body]
        if self.actions:
            payload["content"]["actions"] = [x.serialize() for x in self.actions]
        return payload


class ConnectorCard(Card):
    pass


class HeroCard(Card):
    content_type = "application/vnd.microsoft.card.hero"

    def __init__(
        self,
        title: str,
        text: str,
        *,
        subtitle: Optional[str] = None,
        images: Optional[list[URL]] = None,
        buttons: Optional[list[Button]] = None
    ) -> None:
        self.title = title
        self.text = text
        self.subtitle = subtitle
        self.images = images
        self.buttons = buttons

    def serialize(self) -> dict:
        payload = {"contentType": self.content_type, "content": {}}
        payload["content"]["title"] = self.title
        payload["content"]["text"] = self.text
        if self.subtitle:
            payload["content"]["subtitle"] = self.subtitle
        if self.images:
            payload["content"]["images"] = [{"url": img} for img in self.images]
        if self.buttons:
            payload["content"]["buttons"] = [
                button.serialize() for button in self.buttons
            ]
        return payload


class ListCard(Card):
    pass


class ReceiptCard(Card):
    pass


class ThumbnailCard(Card):
    pass
