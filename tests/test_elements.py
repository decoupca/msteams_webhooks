from msteams_webhooks.elements import Image, Media, MediaSource, TextBlock


def test_text_block() -> None:
    payload = {
        "type": "TextBlock",
        "text": "Lorem ipsum dolor sit amet",
        "color": "good",
        "fontType": "default",
        "horizontalAlignment": "center",
        "maxLines": 3,
        "size": "extraLarge",
        "weight": "bolder",
        "style": "heading",
    }
    text_block = TextBlock(
        text="Lorem ipsum dolor sit amet",
        color="good",
        font_type="default",
        horizontal_alignment="center",
        is_subtle=False,
        max_lines=3,
        size="extraLarge",
        weight="bolder",
        style="heading",
    )
    assert text_block.serialize() == payload


def test_image() -> None:
    payload = {
        "type": "Image",
        "url": "https://adaptivecards.io/content/cats/1.png",
        "altText": "Cat",
        "backgroundColor": "#FFFFFF",
        "height": "80px",
        "horizontalAlignment": "right",
        "size": "stretch",
        "style": "default",
        "width": "100px",
    }
    image = Image(
        url="https://adaptivecards.io/content/cats/1.png",
        alt_text="Cat",
        background_color="#FFFFFF",
        height="80px",
        horizontal_alignment="right",
        size="stretch",
        style="default",
        width="100px",
    )
    assert image.serialize() == payload


def test_media() -> None:
    payload = {
        "type": "Media",
        "sources": [
            {
                "url": "https://adaptivecardsblob.blob.core.windows.net/assets/AdaptiveCardsOverviewVideo.mp4",
                "mimeType": "video/mp4",
            },
        ],
        "poster": "https://adaptivecards.io/content/poster-video.png",
        "altText": "Adaptive Cards overview video",
    }
    media = Media(
        sources=[
            MediaSource(
                url="https://adaptivecardsblob.blob.core.windows.net/assets/AdaptiveCardsOverviewVideo.mp4",
                mime_type="video/mp4",
            ),
        ],
        poster="https://adaptivecards.io/content/poster-video.png",
        alt_text="Adaptive Cards overview video",
    )
    assert media.serialize() == payload
