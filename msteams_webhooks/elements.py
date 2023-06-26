from typing import Any, Literal, Optional, Union

from msteams_webhooks import types
from msteams_webhooks.actions import Action


class CardElement:
    """Base Element class."""

    TYPE = ""
    ATTR_MAP = {}

    def serialize(self) -> dict[str, Any]:
        payload = {"type": self.TYPE}
        for attr, key in self.ATTR_MAP.items():
            if value := getattr(self, attr):
                if value is not None:
                    payload[key] = value
        return payload


class TextBlock(CardElement):
    """TextBlock element.
    https://adaptivecards.io/explorer/TextBlock.html
    """

    TYPE = "TextBlock"
    ATTR_MAP = {
        "text": "text",
        "color": "color",
        "font_type": "fontType",
        "horizontal_alignment": "horizontalAlignment",
        "is_subtle": "isSubtle",
        "max_lines": "maxLines",
        "size": "size",
        "weight": "weight",
        "wrap": "wrap",
        "style": "style",
    }

    def __init__(
        self,
        text: str,
        *,
        color: Optional[types.Colors] = None,
        font_type: Optional[types.FontTypes] = None,
        horizontal_alignment: Optional[types.HorizontalAlignmentTypes] = None,
        is_subtle: Optional[bool] = None,
        max_lines: Optional[int] = None,
        size: Optional[types.FontSizes] = None,
        weight: Optional[types.FontWeights] = None,
        wrap: Optional[bool] = None,
        style: Optional[types.TextBlockStyles] = None,
    ) -> None:
        self.text = text
        self.color = color
        self.font_type = font_type
        self.horizontal_alignment = horizontal_alignment
        self.is_subtle = is_subtle
        self.max_lines = max_lines
        self.size = size
        self.weight = weight
        self.wrap = wrap
        self.style = style


class Image(CardElement):
    """
    Image element.
    https://adaptivecards.io/explorer/Image.html

    """

    TYPE = "Image"
    ATTR_MAP = {
        "url": "url",
        "alt_text": "altText",
        "background_color": "backgroundColor",
        "height": "height",
        "horizontal_alignment": "horizontalAlignment",
        "select_action": "selectAction",
        "size": "size",
        "style": "style",
        "width": "width",
    }

    def __init__(
        self,
        url: types.URL,
        *,
        alt_text: Optional[str] = None,
        background_color: Optional[str] = None,
        height: Optional[Union[str, Literal["auto", "stretch"]]] = None,
        horizontal_alignment: Optional[types.HorizontalAlignmentTypes] = None,
        select_action: Optional[Action] = None,
        size: Optional[types.ImageSizeTypes] = None,
        style: Optional[types.ImageStyleTypes] = None,
        width: Optional[str] = None,
    ) -> None:
        self.url = url
        self.alt_text = alt_text
        self.background_color = background_color
        self.height = height
        self.horizontal_alignment = horizontal_alignment
        self.select_action = select_action
        self.size = size
        self.style = style
        self.width = width


class MediaSource(CardElement):
    """Media source element.

    https://adaptivecards.io/explorer/MediaSource.html
    """

    def __init__(self, url: types.URL, *, mime_type: Optional[str] = None) -> None:
        self.url = url
        self.mime_type = mime_type

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload = {"url": self.url}
        if self.mime_type:
            payload["mimeType"] = self.mime_type
        return payload


class Media(CardElement):
    """Media element.

    https://adaptivecards.io/explorer/Media.html
    """

    def __init__(
        self,
        sources: list[MediaSource],
        *,
        poster: Optional[types.URL] = None,
        alt_text: Optional[str] = None,
    ) -> None:
        self.sources = sources
        self.poster = poster
        self.alt_text = alt_text

    def serialize(self) -> dict:
        payload = {
            "type": "Media",
            "sources": [x.serialize() for x in self.sources],
        }
        if self.poster:
            payload["poster"] = self.poster
        if self.alt_text:
            payload["altText"] = self.alt_text
        return payload
