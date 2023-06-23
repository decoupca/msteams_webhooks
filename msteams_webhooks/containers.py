from typing import Optional, Union

from msteams_webhooks import types
from msteams_webhooks.actions import Action
from msteams_webhooks.elements import CardElement, Image


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


class ColumnSet(CardContainer):
    """ColumnSet.

    https://adaptivecards.io/explorer/ColumnSet.html
    """

    TYPE = "ColumnSet"

    def __init__(
        self,
        columns: Optional[list[Column]] = None,
        select_action: Optional[Action] = None,
        style: Optional[types.ContainerStyleTypes] = None,
        bleed: Optional[bool] = None,
        min_height: Optional[str] = None,
        horizontal_alignment: Optional[types.HorizontalAlignmentTypes] = None,
    ) -> None:
        self.columns = columns
        self.select_action = select_action
        self.style = style
        self.bleed = bleed
        self.min_height = min_height
        self.horizontal_alignment = horizontal_alignment

    def serialize(self) -> dict:
        payload = {"type": self.TYPE}
        if self.columns:
            payload["columns"] = [x.serialize() for x in self.columns]
        if self.select_action:
            payload["selectAction"] = self.select_action.serialize()
        if self.style:
            payload["style"] = self.style
        if self.bleed is not None:
            payload["bleed"] = self.bleed
        if self.min_height:
            payload["minHeight"] = self.min_height
        if self.horizontal_alignment:
            payload["horizontalAlignment"] = self.horizontal_alignment
        return payload


class Fact(CardContainer):
    """Fact.

    https://adaptivecards.io/explorer/Fact.html
    """

    def __init__(self, title: str, value: str) -> None:
        self.title = title
        self.value = value

    def serialize(self) -> dict:
        return {"title": self.title, "value": self.value}


class FactSet(CardContainer):
    """FactSet.

    https://adaptivecards.io/explorer/FactSet.html
    """

    TYPE = "FactSet"

    def __init__(self, facts: list[Fact]) -> None:
        self.facts = facts

    def serialize(self) -> dict:
        return {
            "type": self.TYPE,
            "facts": [x.serialize() for x in self.facts],
        }


class ImageSet(CardContainer):
    """ImageSet.

    https://adaptivecards.io/explorer/ImageSet.html
    """

    TYPE = "ImageSet"

    def __init__(
        self, images: list[Image], *, image_size: Optional[types.ImageSizeTypes] = None
    ) -> None:
        self.images = images
        self.image_size = image_size

    def serialize(self) -> dict:
        payload = {
            "type": self.TYPE,
            "images": [x.serialize() for x in self.images],
        }
        if self.image_size:
            payload["imageSize"] = self.image_size
        return payload


class TableCell(CardContainer):
    """Table cell.

    https://adaptivecards.io/explorer/TableCell.html
    """

    TYPE = "TableCell"

    def __init__(
        self,
        items: list[CardElement],
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


class TableRow(CardContainer):
    """TableRow."""

    TYPE = "TableRow"

    def __init__(self, cells: list[TableCell]) -> None:
        self.cells = cells

    def serialize(self) -> dict:
        return {"type": self.TYPE, "cells": [x.serialize() for x in self.cells]}


class TableColumn:
    """TableColumn.

    This entity is not documented beyond a few Table examples. Other properties
    are unknown.
    """

    def __init__(self, width: int) -> None:
        self.width = width

    def serialize(self) -> dict:
        return {"width": self.width}


class Table(CardContainer):
    """Table.

    https://adaptivecards.io/explorer/Table.html
    """

    TYPE = "Table"

    def __init__(
        self,
        columns: Optional[list[TableColumn]] = None,
        rows: Optional[list[TableRow]] = None,
        first_row_as_headers: Optional[bool] = None,
        show_grid_lines: Optional[bool] = None,
        grid_style: Optional[types.ContainerStyleTypes] = None,
        horizontal_cell_content_alignment: Optional[types.HorizontalAlignmentTypes] = None,
        vertical_cell_content_alignment: Optional[types.VerticalAlignmentTypes] = None,
    ) -> None:
        self.columns = columns
        self.rows = rows
        self.first_row_as_headers = first_row_as_headers
        self.show_grid_lines = show_grid_lines
        self.grid_style = grid_style
        self.horizontal_cell_content_alignment = horizontal_cell_content_alignment
        self.vertical_cell_content_alignment = vertical_cell_content_alignment

    def serialize(self) -> dict:
        payload = {"type": self.TYPE}
        if self.columns:
            payload["columns"] = [x.serialize() for x in self.columns]
        if self.rows:
            payload["rows"] = [x.serialize() for x in self.rows]
        if self.first_row_as_headers is not None:
            payload["firstRowAsHeaders"] = self.first_row_as_headers
        if self.show_grid_lines is not None:
            payload["showGridLines"] = self.show_grid_lines
        if self.grid_style:
            payload["gridStyle"] = self.grid_style
        if self.horizontal_cell_content_alignment:
            payload["horizontalCellContentAlignment"] = self.horizontal_cell_content_alignment
        if self.vertical_cell_content_alignment:
            payload["verticalCellContentAlignment"] = self.vertical_cell_content_alignment
        return payload
