"""Containers provide ways to organize and format elements within cards."""
from typing import Any, Optional, Union

from msteams_webhooks import types
from msteams_webhooks.actions import Action
from msteams_webhooks.base import Entity
from msteams_webhooks.elements import CardElement, Image


class CardContainer(Entity):
    """Base container class."""


class ActionSet(CardContainer):
    """Action sets.

    Schema Explorer: https://adaptivecards.io/explorer/ActionSet.html
    """

    def __init__(self, actions: list[Action]) -> None:
        """Displays a set of actions.

        Args:
            actions: List of ``Action`` elements to show.

        Returns:
            None.

        Raises:
            N/A
        """
        self.actions = actions

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        return {"type": "ActionSet", "actions": [x.serialize() for x in self.actions]}


class Container(CardContainer):
    """Generic container, which may contain any other container or element.

    Schema Explorer: https://adaptivecards.io/explorer/Container.html
    """

    def __init__(
        self,
        items: list[Union[CardElement, CardContainer]],
        *,
        select_action: Optional[Action] = None,
        style: Optional[types.ContainerStyleTypes] = None,
        vertical_content_alignment: Optional[types.VerticalAlignmentTypes] = None,
        bleed: Optional[bool] = None,
        background_image: Optional[str] = None,
        min_height: Optional[str] = None,
        rtl: Optional[bool] = None,
    ) -> None:
        """Containers group items together in arbitrary ways.

        May be combined with other containers or elements in flexible ways.

        Args:
            items: The card elements to render inside the ``Container``.
            select_action: An ``Action`` that will be invoked when the ``Container`` is
                tapped or selected. Action.ShowCard is not supported.
            style: Style hint for ``Container``.
            vertical_content_alignment: Defines how the content should be aligned
                vertically within the container. When not specified, the value of
                vertical_content_alignment is inherited from the parent container. If no
                parent container has verticalContentAlignment set, it defaults to Top.
            bleed: Determines whether the element should bleed through its parent`s padding.
            background_image: Specifies the background image. Acceptable formats are PNG,
                JPEG, and GIF.
            min_height: Specifies the minimum height of the container in pixels, like "80px".
            rtl: When true content in this container should be presented right to left. When
                'false' content in this container should be presented left to right. When unset
                layout direction will inherit from parent container or column. If unset in all
                ancestors, the default platform behavior will apply.

        Returns:
            None.

        Raises:
            N/A
        """
        self.items = items
        self.select_action = select_action
        self.style = style
        self.vertical_content_alignment = vertical_content_alignment
        self.bleed = bleed
        self.background_image = background_image
        self.min_height = min_height
        self.rtl = rtl

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload = {
            "type": "Container",
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
    """A single column, as an lement of a ``ColumnSet``, or a column in a ``Table``.

    Schema explorer: https://adaptivecards.io/explorer/Column.html
    """

    def __init__(
        self,
        items: Optional[list[CardElement]] = None,
        background_image: Optional[str] = None,
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
        """Defines a container that is part of a ``ColumnSet`` or a column in a ``Table``.

        Args:
            items: The card elements to render inside the ``Column``.
            background_image: Specifies the background image. Acceptable formats are
                PNG, JPEG, and GIF.
            bleed: Determines whether the column should bleed through its parent`s padding.
            min_height: Specifies the minimum height of the column in pixels, like "80px".
            rtl: When true content in this column should be presented right to left. When
                ``False`` content in this column should be presented left to right. When
                unset layout direction will inherit from parent container or column. If unset
                in all ancestors, the default platform behavior will apply.
            separator: When ``True``, draw a separating line between this column and the previous
                column.
            spacing: Controls the amount of spacing between this column and the preceding column.
            select_action: An ``Action`` that will be invoked when the ``Column`` is tapped or
                selected. Action.ShowCard is not supported.
            style: Style hint for ``Column``.
            vertical_content_alignment: Defines how the content should be aligned vertically within
                the column. When not specified, the value of verticalContentAlignment is inherited
                from the parent container. If no parent container has verticalContentAlignment set,
                it defaults to Top.
            width: "auto", "stretch", a number representing relative width of the column in the
                column group, or in version 1.1 and higher, a specific pixel width, like "50px".

        Returns:
            None.

        Raises:
            N/A
        """
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

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload: dict[str, Any] = {"type": "Column"}
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
    """Grouping of columns.

    Schema Explorer: https://adaptivecards.io/explorer/ColumnSet.html
    """

    def __init__(
        self,
        columns: Optional[list[Column]] = None,
        select_action: Optional[Action] = None,
        style: Optional[types.ContainerStyleTypes] = None,
        bleed: Optional[bool] = None,
        min_height: Optional[str] = None,
        horizontal_alignment: Optional[types.HorizontalAlignmentTypes] = None,
    ) -> None:
        """``ColumnSet`` divides a region into ``Columns``, allowing elements to sit side-by-side.

        Args:
            columns: The list of ``Columns`` to divide the region into.
            select_action: 	An ``Action`` that will be invoked when the ColumnSet is tapped
                or selected. Action.ShowCard is not supported.
            style: Style hint for ``ColumnSet``.
            bleed: Determines whether the element should bleed through its parent's padding.
            min_height: Specifies the minimum height of the column set in pixels, like "80px".
            horizontal_alignment: Controls the horizontal alignment of the ColumnSet. When not
                specified, the value of horizontalAlignment is inherited from the parent container.
                If no parent container has horizontalAlignment set, it defaults to Left.

        Returns:
            None.

        Raises:
            N/A
        """
        self.columns = columns
        self.select_action = select_action
        self.style = style
        self.bleed = bleed
        self.min_height = min_height
        self.horizontal_alignment = horizontal_alignment

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload: dict[str, Any] = {"type": "ColumnSet"}
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
    """Facts organize key/value pairs into an organized list.

    Schema Explorer: https://adaptivecards.io/explorer/Fact.html
    """

    def __init__(self, title: str, value: str) -> None:
        """Describes a Fact in a FactSet as a key/value pair.

        Args:
            title: The title of the fact.
            value: The value of the fact.

        Returns:
            None.

        Raises:
            N/A
        """
        self.title = title
        self.value = value

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        return {"title": self.title, "value": self.value}


class FactSet(CardContainer):
    """A group of ``Fact`` containers.

    Schema Explorer: https://adaptivecards.io/explorer/FactSet.html
    """

    def __init__(self, facts: list[Fact]) -> None:
        """Displays a series of facts (i.e. name/value pairs) in a tabular form.

        Args:
            facts: The list of ``Fact`` elements to show.

        Returns:
            None.

        Raises:
            N/A
        """
        self.facts = facts

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        return {
            "type": "FactSet",
            "facts": [x.serialize() for x in self.facts],
        }


class ImageSet(CardContainer):
    """A collection of images.

    Schema Explorer: https://adaptivecards.io/explorer/ImageSet.html
    """

    def __init__(
        self,
        images: list[Image],
        *,
        image_size: Optional[types.ImageSizeTypes] = None,
    ) -> None:
        """Displays a collection of Images similar to a gallery.

        Acceptable formats are PNG, JPEG, and GIF.

        Args:
            images: The list of ``Image`` elements to show.
            image_size: Controls the approximate size of each image. The physical
                dimensions will vary per host. Auto and stretch are not supported for
                ImageSet. The size will default to medium if those values are set.

        Returns:
            None.

        Raises:
            N/A
        """
        self.images = images
        self.image_size = image_size

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload = {
            "type": "ImageSet",
            "images": [x.serialize() for x in self.images],
        }
        if self.image_size:
            payload["imageSize"] = self.image_size
        return payload


class ReceiptFact(CardContainer):
    """A key/value pair for use with a Receipt Card."""

    def __init__(self, key: str, value: str) -> None:
        """Create a fact to include in a Receipt Card.

        Args:
            key: Fact key.
            value: Fact value.

        Returns:
            None.

        Raises:
            N/A
        """
        self.key = key
        self.value = value

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        return {"key": self.key, "value": self.value}


class ReceiptItem(CardContainer):
    """Item for a Receipt Card."""

    def __init__(
        self,
        title: str,
        price: str,
        quantity: int,
        *,
        image: Optional[str] = None,
    ) -> None:
        """Item for a Receipt Card.

        Args:
            title: Title of the item.
            price: Unit price of the item.
            quantity: Number of items sold.
            image: Optional URL to an image of the item.

        Returns:
            None.

        Raises:
            N/A
        """
        self.title = title
        self.price = price
        self.quantity = quantity
        self.image = image

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload: dict[str, Any] = {
            "title": self.title,
            "price": self.price,
            "quantity": self.quantity,
        }
        if self.image:
            payload["image"] = {"url": self.image}
        return payload


class TableCell(CardContainer):
    """Single cell of a ``Table`` container.

    Schema Explorer: https://adaptivecards.io/explorer/TableCell.html
    """

    def __init__(
        self,
        items: list[CardElement],
        *,
        select_action: Optional[Action] = None,
        style: Optional[types.ContainerStyleTypes] = None,
        vertical_content_alignment: Optional[types.VerticalAlignmentTypes] = None,
        bleed: Optional[bool] = None,
        background_image: Optional[str] = None,
        min_height: Optional[str] = None,
        rtl: Optional[bool] = None,
    ) -> None:
        """Represents a cell within a row of a ``Table`` element.

        Args:
            items: The card elements to render inside the ``TableCell``.
            select_action: An Action that will be invoked when the ``TableCell`` is tapped
                or selected. Action.ShowCard is not supported.
            style: Style hint for ``TableCell``.
            vertical_content_alignment: Defines how the content should be aligned vertically
                within the container. When not specified, the value of vertical_content_alignment
                is inherited from the parent container. If no parent container has
                vertical_content_alignment set, it defaults to Top.
            bleed: Determines whether the element should bleed through its parent's padding.
            background_image: Specifies the background image. Acceptable formats are PNG, JPEG,
                and GIF.
            min_height: Specifies the minimum height of the container in pixels, like "80px".
            rtl: When true content in this container should be presented right to left. When 'false'
                content in this container should be presented left to right. When unset layout
                direction will inherit from parent container or column. If unset in all ancestors,
                the default platform behavior will apply.

        Returns:
            None.

        Raises:
            N/A
        """
        self.items = items
        self.select_action = select_action
        self.style = style
        self.vertical_content_alignment = vertical_content_alignment
        self.bleed = bleed
        self.background_image = background_image
        self.min_height = min_height
        self.rtl = rtl

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload = {
            "type": "TableCell",
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
    """Single row of a ``Table`` container."""

    def __init__(
        self,
        cells: list[TableCell],
        style: Optional[types.ContainerStyleTypes] = None,
    ) -> None:
        """Organizes cells into a row for a ``Table``.

        Args:
            cells: List of ``TableCells`` to include in the row.
            style: Style hint for ``TableRow``.

        Returns:
            None.

        Raises:
            N/A
        """
        self.cells = cells
        self.style = style

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload = {"type": "TableRow", "cells": [x.serialize() for x in self.cells]}
        if self.style:
            payload["style"] = self.style
        return payload


class Table(CardContainer):
    """Container for displaying tabular data.

    Schema Explorer: https://adaptivecards.io/explorer/Table.html
    """

    def __init__(
        self,
        columns: Optional[list[Column]] = None,
        rows: Optional[list[TableRow]] = None,
        first_row_as_headers: Optional[bool] = None,
        show_grid_lines: Optional[bool] = None,
        grid_style: Optional[types.ContainerStyleTypes] = None,
        horizontal_cell_content_alignment: Optional[types.HorizontalAlignmentTypes] = None,
        vertical_cell_content_alignment: Optional[types.VerticalAlignmentTypes] = None,
    ) -> None:
        """Provides a way to display data in a tabular form.

        Args:
            columns: List of ``Column`` elements to include.
            rows: List of ``TableRow`` elements to include.
            first_row_as_headers: Specifies whether the first row of the table should be treated
                as a header row, and be announced as such by accessibility software.
            show_grid_lines: Specifies whether grid lines should be displayed.
            grid_style: Defines the style of the grid. This property currently only controls the
                grid's color.
            horizontal_cell_content_alignment: Controls how the content of all cells is horizontally
                aligned by default. When not specified, horizontal alignment is defined on a
                per-cell basis.
            vertical_cell_content_alignment: Controls how the content of all cells is vertically
                aligned by default. When not specified, vertical alignment is defined on a per-cell
                basis.
        """
        self.columns = columns
        self.rows = rows
        self.first_row_as_headers = first_row_as_headers
        self.show_grid_lines = show_grid_lines
        self.grid_style = grid_style
        self.horizontal_cell_content_alignment = horizontal_cell_content_alignment
        self.vertical_cell_content_alignment = vertical_cell_content_alignment

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload: dict[str, Any] = {"type": "Table"}
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
