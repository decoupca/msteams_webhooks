from typing import Optional, Union

from msteams_webhooks import types
from msteams_webhooks.actions import Action
from msteams_webhooks.elements import CardElement


class CardContainer:
    """Base container class."""

    def serialize(self) -> dict:
        pass


class ActionSet(CardContainer):
    """Action sets.

    https://adaptivecards.io/explorer/ActionSet.html
    """

    TYPE = "ActionSet"

    def __init__(self, actions: list[Action]) -> None:
        self.actions = actions

    def serialize(self) -> dict:
        return {"type": self.TYPE, "actions": [x.serialize() for x in self.actions]}


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
            payload["selectAction"] = self.select_action.serialize()
        if self.style:
            payload["style"] = self.style
        if self.vertical_content_alignment:
            payload["verticalContentAlignment"] = self.vertical_content_alignment
        if self.bleed is not None:
            payload["bleed"] = self.bleed
        if self.background_image:
            payload["backgroundImage"] = self.background_image
        if self.min_height:
            payload["minHeight"] = self.min_height
        if self.rtl is not None:
            payload["rtl"] = self.rtl
        return payload


class Column(CardContainer):
    """Column, element of a ColumnSet.

    https://adaptivecards.io/explorer/Column.html
    """

    TYPE = "Column"

    def __init__(
        self,
        items: Optional[list[CardElement]] = None,
        background_image: Optional[types.URL] = None,
        bleed: Optional[bool] = None,
        min_height: Optional[str] = None,
        rtl: Optional[bool] = None,
        separator: Optional[bool] = None,
        spacing: Optional[types.SpacingTypes] = None,
        select_action: Optional[Action] = None,
        style: Optional[types.ContainerStyleTypes] = None,
        vertical_content_alignment: Optional[types.VerticalAlignmentTypes] = None,
        width: Optional[types.ColumnWidthTypes] = None,
    ) -> None:
        self.items = items
        self.background_image = background_image
        self.bleed = bleed
        self.min_height = min_height
        self.rtl = rtl
        self.separator = separator
        self.spacing = spacing
        self.select_action = select_action
        self.style = style
        self.vertical_content_alignment = vertical_content_alignment
        self.width = width

    def serialize(self) -> dict:
        payload = {"type": self.TYPE}
        if self.items:
            payload["items"] = [x.serialize() for x in self.items]
        if self.background_image:
            payload["backgroundImage"] = self.background_image
        if self.bleed is not None:
            payload["bleed"] = self.bleed
        if self.min_height:
            payload["minHeight"] = self.min_height
        if self.rtl is not None:
            payload["rtl"] = self.rtl
        if self.separator is not None:
            payload["separator"] = self.separator
        if self.spacing:
            payload["spacing"] = self.spacing
        if self.select_action:
            payload["selectAction"] = self.select_action.serialize()
        if self.style:
            payload["style"] = self.style
        if self.vertical_content_alignment:
            payload["verticalContentAlignment"] = self.vertical_content_alignment
        if self.width:
            payload["width"] = self.width
        return payload
