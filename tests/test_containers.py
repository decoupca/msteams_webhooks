from msteams_webhooks import containers
from msteams_webhooks import elements
from msteams_webhooks.actions import OpenURLAction


def test_action_set() -> None:
    payload = {
        "type": "ActionSet",
        "actions": [
            {"type": "Action.OpenUrl", "url": "https://example.com/", "title": "Example action"}
        ],
    }
    action = OpenURLAction(url="https://example.com/", title="Example action")
    action_set = containers.ActionSet(actions=[action])
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
    text_block = elements.TextBlock(text="This is some text")
    image = elements.Image(url="https://adaptivecards.io/content/cats/1.png", alt_text="Cat")
    container = containers.Container(
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
    image = elements.Image(url="https://adaptivecards.io/content/cats/1.png", alt_text="Cat")
    col1_text = elements.TextBlock(text="Column 1")
    col2_text = elements.TextBlock(text="Column 2")
    col3_text = elements.TextBlock(text="Column 3")
    col_set = containers.ColumnSet(
        columns=[
            containers.Column(items=[col1_text, image]),
            containers.Column(items=[col2_text, image]),
            containers.Column(items=[col3_text, image]),
        ]
    )
    assert col_set.serialize() == payload
