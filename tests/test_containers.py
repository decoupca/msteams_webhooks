from msteams_webhooks.actions import OpenURLAction
from msteams_webhooks.containers import (
    ActionSet,
    Column,
    ColumnSet,
    Container,
    Fact,
    FactSet,
    ImageSet,
    Table,
    TableCell,
    TableRow,
)
from msteams_webhooks.elements import Image, Media, MediaSource, TextBlock


def test_action_set() -> None:
    payload = {
        "type": "ActionSet",
        "actions": [
            {"type": "Action.OpenUrl", "url": "https://example.com/", "title": "Example action"}
        ],
    }
    action = OpenURLAction(url="https://example.com/", title="Example action")
    action_set = ActionSet(actions=[action])
    assert action_set.serialize() == payload


def test_container() -> None:
    payload = {
        "type": "Container",
        "items": [
            {"type": "TextBlock", "text": "This is some text"},
            {
                "type": "Image",
                "url": "https://adaptivecards.io/content/cats/1.png",
                "altText": "Cat",
            },
        ],
        "style": "attention",
        "verticalContentAlignment": "bottom",
        "bleed": True,
        "minHeight": "150px",
        "rtl": True,
    }
    text_block = TextBlock(text="This is some text")
    image = Image(url="https://adaptivecards.io/content/cats/1.png", alt_text="Cat")
    container = Container(
        items=[text_block, image],
        vertical_content_alignment="bottom",
        style="attention",
        min_height="150px",
        bleed=True,
        rtl=True,
    )
    assert container.serialize() == payload


def test_column() -> None:
    payload = {
        "type": "ColumnSet",
        "columns": [
            {
                "type": "Column",
                "items": [
                    {"type": "TextBlock", "text": "Column 1"},
                    {
                        "type": "Image",
                        "url": "https://adaptivecards.io/content/cats/1.png",
                        "altText": "Cat",
                    },
                ],
            },
            {
                "type": "Column",
                "items": [
                    {"type": "TextBlock", "text": "Column 2"},
                    {
                        "type": "Image",
                        "url": "https://adaptivecards.io/content/cats/1.png",
                        "altText": "Cat",
                    },
                ],
            },
            {
                "type": "Column",
                "items": [
                    {"type": "TextBlock", "text": "Column 3"},
                    {
                        "type": "Image",
                        "url": "https://adaptivecards.io/content/cats/1.png",
                        "altText": "Cat",
                    },
                ],
            },
        ],
    }
    image = Image(url="https://adaptivecards.io/content/cats/1.png", alt_text="Cat")
    col1_text = TextBlock(text="Column 1")
    col2_text = TextBlock(text="Column 2")
    col3_text = TextBlock(text="Column 3")
    col_set = ColumnSet(
        columns=[
            Column(items=[col1_text, image]),
            Column(items=[col2_text, image]),
            Column(items=[col3_text, image]),
        ]
    )
    assert col_set.serialize() == payload


def test_facts() -> None:
    payload = {
        "type": "FactSet",
        "facts": [
            {"title": "Fact 1", "value": "Value 1"},
            {"title": "Fact 2", "value": "Value 2"},
            {"title": "Fact 3", "value": "Value 3"},
        ],
    }
    fact_set = FactSet(
        facts=[
            Fact(title="Fact 1", value="Value 1"),
            Fact(title="Fact 2", value="Value 2"),
            Fact(title="Fact 3", value="Value 3"),
        ]
    )
    assert fact_set.serialize() == payload


def test_image_set() -> None:
    payload = {
        "type": "ImageSet",
        "images": [
            {
                "type": "Image",
                "url": "https://adaptivecards.io/content/cats/1.png",
                "altText": "Cat",
            },
            {
                "type": "Image",
                "url": "https://adaptivecards.io/content/cats/1.png",
                "altText": "Cat",
            },
            {
                "type": "Image",
                "url": "https://adaptivecards.io/content/cats/1.png",
                "altText": "Cat",
            },
            {
                "type": "Image",
                "url": "https://adaptivecards.io/content/cats/1.png",
                "altText": "Cat",
            },
            {
                "type": "Image",
                "url": "https://adaptivecards.io/content/cats/1.png",
                "altText": "Cat",
            },
            {
                "type": "Image",
                "url": "https://adaptivecards.io/content/cats/1.png",
                "altText": "Cat",
            },
        ],
    }
    image = Image(url="https://adaptivecards.io/content/cats/1.png", alt_text="Cat")
    image_set = ImageSet(images=[image, image, image, image, image, image])
    assert image_set.serialize() == payload


def test_table() -> None:
    payload = {
        "type": "Table",
        "gridStyle": "accent",
        "firstRowAsHeaders": True,
        "columns": [
            {"type": "Column", "width": 1},
            {"type": "Column", "width": 1},
            {"type": "Column", "width": 3},
        ],
        "rows": [
            {
                "type": "TableRow",
                "cells": [
                    {
                        "type": "TableCell",
                        "items": [
                            {
                                "type": "TextBlock",
                                "text": "Name",
                                "wrap": True,
                                "weight": "bolder",
                            }
                        ],
                    },
                    {
                        "type": "TableCell",
                        "items": [
                            {
                                "type": "TextBlock",
                                "text": "Type",
                                "wrap": True,
                                "weight": "bolder",
                            }
                        ],
                    },
                    {
                        "type": "TableCell",
                        "items": [
                            {
                                "type": "TextBlock",
                                "text": "Description",
                                "wrap": True,
                                "weight": "bolder",
                            }
                        ],
                    },
                ],
                "style": "accent",
            },
            {
                "type": "TableRow",
                "cells": [
                    {
                        "type": "TableCell",
                        "style": "good",
                        "items": [{"type": "TextBlock", "text": "columns", "wrap": True}],
                    },
                    {
                        "type": "TableCell",
                        "style": "warning",
                        "items": [
                            {"type": "TextBlock", "text": "ColumnDefinition[]", "wrap": True}
                        ],
                    },
                    {
                        "type": "TableCell",
                        "style": "accent",
                        "items": [
                            {
                                "type": "TextBlock",
                                "text": "Defines the table's columns (number of columns, and column sizes).",
                                "wrap": True,
                            }
                        ],
                    },
                ],
            },
            {
                "type": "TableRow",
                "cells": [
                    {
                        "type": "TableCell",
                        "style": "good",
                        "items": [{"type": "TextBlock", "text": "rows", "wrap": True}],
                    },
                    {
                        "type": "TableCell",
                        "style": "accent",
                        "items": [{"type": "TextBlock", "text": "TableRow[]", "wrap": True}],
                    },
                    {
                        "type": "TableCell",
                        "style": "attention",
                        "items": [
                            {
                                "type": "TextBlock",
                                "text": "Defines the rows of the Table, each being a collection of cells. Rows are not required, which allows empty Tables to be generated via templating without breaking the rendering of the whole card.",
                                "wrap": True,
                            }
                        ],
                    },
                ],
            },
        ],
    }
    table = Table(
        grid_style="accent",
        first_row_as_headers=True,
        columns=[
            Column(width=1),
            Column(width=1),
            Column(width=3),
        ],
        rows=[
            TableRow(
                cells=[
                    TableCell(items=[TextBlock(text="Name", wrap=True, weight="bolder")]),
                    TableCell(items=[TextBlock(text="Type", wrap=True, weight="bolder")]),
                    TableCell(items=[TextBlock(text="Description", wrap=True, weight="bolder")]),
                ],
                style="accent",
            ),
            TableRow(
                cells=[
                    TableCell(style="good", items=[TextBlock(text="columns", wrap=True)]),
                    TableCell(
                        style="warning", items=[TextBlock(text="ColumnDefinition[]", wrap=True)]
                    ),
                    TableCell(
                        style="accent",
                        items=[
                            TextBlock(
                                text="Defines the table's columns (number of columns, and column sizes).",
                                wrap=True,
                            )
                        ],
                    ),
                ],
            ),
            TableRow(
                cells=[
                    TableCell(style="good", items=[TextBlock(text="rows", wrap=True)]),
                    TableCell(style="accent", items=[TextBlock(text="TableRow[]", wrap=True)]),
                    TableCell(
                        style="attention",
                        items=[
                            TextBlock(
                                text="Defines the rows of the Table, each being a collection of cells. Rows are not required, which allows empty Tables to be generated via templating without breaking the rendering of the whole card.",
                                wrap=True,
                            )
                        ],
                    ),
                ]
            ),
        ],
    )
    assert table.serialize() == payload
