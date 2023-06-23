from typing import Optional, Union

from msteams_webhooks import types
from msteams_webhooks.actions import Action
from msteams_webhooks.buttons import Button
from msteams_webhooks.containers import CardContainer
from msteams_webhooks.elements import CardElement


class Card:
    TYPE = ""
    SCHEMA = ""

    def serialize(self) -> dict:
        pass


class AdaptiveCard(Card):
    TYPE = "AdaptiveCard"
    SCHEMA = "http://adaptivecards.io/schemas/adaptive-card.json"

    def __init__(
        self,
        *,
        body: Optional[list[Union[CardElement, CardContainer]]] = None,
        actions: Optional[list[Action]] = None,
    ) -> None:
        self.body = body or []
        self.actions = actions or []

    def serialize(self) -> dict:
        payload = {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "$schema": self.SCHEMA,
                "type": self.TYPE,
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
    TYPE = "application/vnd.microsoft.card.hero"

    def __init__(
        self,
        title: str,
        text: str,
        *,
        subtitle: Optional[str] = None,
        images: Optional[list[types.URL]] = None,
        buttons: Optional[list[Button]] = None,
    ) -> None:
        self.title = title
        self.text = text
        self.subtitle = subtitle
        self.images = images
        self.buttons = buttons

    def serialize(self) -> dict:
        payload = {"contentType": self.TYPE, "content": {}}
        payload["content"]["title"] = self.title
        payload["content"]["text"] = self.text
        if self.subtitle:
            payload["content"]["subtitle"] = self.subtitle
        if self.images:
            payload["content"]["images"] = [{"url": img} for img in self.images]
        if self.buttons:
            payload["content"]["buttons"] = [x.serialize() for x in self.buttons]
        return payload


class ListCard(Card):
    pass


class ReceiptCard(Card):
    pass


class ThumbnailCard(Card):
    pass
