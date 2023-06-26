from msteams_webhooks import containers
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
