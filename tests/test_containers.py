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
