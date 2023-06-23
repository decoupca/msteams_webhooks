from typing import Optional, Union

from msteams_webhooks import types
from msteams_webhooks.actions import Action
from msteams_webhooks.elements import CardElement


class CardContainer:
    """Base container class."""

    def serialize(self) -> dict:
        pass


class Container(CardContainer):
    """Generic container.

    https://adaptivecards.io/explorer/Container.html
    """

    TYPE = "Container"

    def __init__(
        self,
        items: list[Union[CardElement, CardContainer]],
        *,
        select_action: Optional[Action] = None,
        style: Optional[types.ContainerStyleTypes] = None,
        vertical_content_alignment: Optional[types.VerticalAlignmentTypes] = None,
        bleed: Optional[bool] = None,
        background_image: Optional[types.URL] = None,
        min_height: Optional[str] = None,
        rtl: Optional[bool] = None,
    ) -> None:
        self.items = items
        self.select_action = select_action
        self.style = style
        self.vertical_content_alignment = vertical_content_alignment
        self.bleed = bleed
        self.background_image = background_image
        self.min_height = min_height
        self.rtl = rtl

    def serialize(self) -> dict:
        payload = {
            "type": self.TYPE,
            "items": [x.serialize() for x in self.items],
        }
        if self.select_action:
            payload["selectAction"] = self.select_action
        if self.style:
            payload["style"] = self.style
        if self.vertical_content_alignment:
            payload["verticalContentAlignment"] = self.vertical_content_alignment
        if self.bleed:
            payload["bleed"] = self.bleed
        if self.background_image:
            payload["backgroundImage"] = self.background_image
        if self.min_height:
            payload["minHeight"] = self.min_height
        if self.rtl:
            payload["rtl"] = self.rtl
        return payload
