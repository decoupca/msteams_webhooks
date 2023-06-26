from msteams_webhooks.actions import OpenURLAction


def test_open_url_action() -> None:
    payload = {"type": "Action.OpenUrl", "url": "https://example.com/", "title": "Example action"}
    action = OpenURLAction(url="https://example.com/", title="Example action")
    assert action.serialize() == payload
