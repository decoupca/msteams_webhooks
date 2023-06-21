from typing import Optional

from msteams_webhooks.types import (
    Colors,
    FontSizes,
    FontTypes,
    FontWeights,
    HorizontalAlignmentTypes,
    TextBlockStyles,
)


class Element:
    pass


class TextBlock(Element):
    def __init__(
        self,
        text: str,
        *,
        color: Optional[Colors] = None,
        font_type: Optional[FontTypes] = None,
        horizontal_alignment: Optional[HorizontalAlignmentTypes] = None,
        is_subtle: Optional[bool] = None,
        max_lines: Optional[int] = None,
        size: Optional[FontSizes] = None,
        weight: Optional[FontWeights] = None,
        wrap: Optional[bool] = None,
        style: Optional[TextBlockStyles] = None,
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

    def serialize(self) -> dict:
        payload = {
            "type": "TextBlock",
            "text": self.text,
        }
        if self.color:
            payload["color"] = self.color
        if self.font_type:
            payload["fontType"] = self.font_type
        if self.horizontal_alignment:
            payload["horizontalAlighment"] = self.horizontal_alignment
        if self.is_subtle is not None:
            payload["isSubtle"] = self.is_subtle
        if self.max_lines:
            payload["maxLines"] = self.max_lines
        if self.size:
            payload["size"] = self.size
        if self.weight:
            payload["weight"] = self.weight
        if self.wrap is not None:
            payload["wrap"] = self.wrap
        if self.style:
            payload["style"] = self.style
        return payload
