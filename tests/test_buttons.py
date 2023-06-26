from msteams_webhooks.buttons import OpenURLButton


def test_open_url_button():
    payload = {"type": "openUrl", "title": "Test Button", "value": "https://example.com/"}
    button = OpenURLButton(title="Test Button", url="https://example.com/")
    assert button.serialize() == payload
