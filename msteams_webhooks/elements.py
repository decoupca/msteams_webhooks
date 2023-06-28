"""Cards are built using various elements."""
from typing import Any, Literal, Optional, Union

from msteams_webhooks import types
from msteams_webhooks.actions import Action
from msteams_webhooks.base import Entity


class CardElement(Entity):
    """Base element class."""


class Image(CardElement):
    """Displays an image. Acceptable formats are PNG, JPEG, and GIF.

    Schema Explorer: https://adaptivecards.io/explorer/Image.html.
    """

    def __init__(
        self,
        url: str,
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
        """Displays an image. Acceptable formats are PNG, JPEG, and GIF.

        Args:
            url: The URL to the image. Supports data URI in version 1.2+.
            alt_text: Alternate text describing the image.
            background_color: Applies a background to a transparent image.
                This property will respect the image style.
            height: The desired height of the image. If specified as a pixel value,
                ending in 'px', E.g., 50px, the image will distort to fit that exact
                height. This overrides the size property.
            horizontal_alignment: Controls how this element is horizontally positioned
                within its parent. When not specified, the value of horizontalAlignment
                is inherited from the parent container. If no parent container has
                horizontalAlignment set, it defaults to Left.
            select_action: An ``Action`` that will be invoked when the ``Image`` is tapped
                or selected. ``Action.ShowCard`` is not supported.
            size: Controls the approximate size of the image. The physical dimensions will
                vary per host.
            style: Controls how this ``Image`` is displayed.
            width: The desired on-screen width of the image, ending in 'px'. E.g., 50px.
                This overrides the size property.

        Returns:
            None.

        Raises:
            None.
        """
        self.url = url
        self.alt_text = alt_text
        self.background_color = background_color
        self.height = height
        self.horizontal_alignment = horizontal_alignment
        self.select_action = select_action
        self.size = size
        self.style = style
        self.width = width

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload: dict[str, Any] = {
            "type": "Image",
            "url": self.url,
        }
        if self.alt_text:
            payload["altText"] = self.alt_text
        if self.background_color:
            payload["backgroundColor"] = self.background_color
        if self.height:
            payload["height"] = self.height
        if self.horizontal_alignment:
            payload["horizontalAlignment"] = self.horizontal_alignment
        if self.select_action:
            payload["selectAction"] = self.select_action.serialize()
        if self.size:
            payload["size"] = self.size
        if self.style:
            payload["style"] = self.style
        if self.width:
            payload["width"] = self.width
        return payload


class MediaSource(CardElement):
    """Defines a source for a Media element.

    Schema Explorer: https://adaptivecards.io/explorer/MediaSource.html
    """

    def __init__(self, url: str, *, mime_type: Optional[str] = None) -> None:
        """Defines a source for a Media element.

        Args:
            url: URL to media. Supports data URI in version 1.2+
            mime_type: Mime type of associated media (e.g. "video/mp4"). For YouTube
                and other Web video URLs, mime_type can be omitted.

        Returns:
            None.

        Raises:
            None.
        """
        self.url = url
        self.mime_type = mime_type

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload: dict[str, Any] = {"url": self.url}
        if self.mime_type:
            payload["mimeType"] = self.mime_type
        return payload


class Media(CardElement):
    """Displays a media player for audio or video content.

    Schema Explorer: https://adaptivecards.io/explorer/Media.html
    """

    def __init__(
        self,
        sources: list[MediaSource],
        *,
        poster: Optional[str] = None,
        alt_text: Optional[str] = None,
    ) -> None:
        """Displays a media player for audio or video content.

        Args:
            sources: List of ``MediaSource`` elements to display.
            poster: URL of an image to display before playing. Supports data URI in version 1.2+.
                If poster is omitted, the Media element will either use a default poster
                (controlled by the host application) or will attempt to automatically pull
                the poster from the target video service when the source URL points to a
                video from a Web provider such as YouTube.
            alt_text: Alternate text describing the audio or video.

        Returns:
            None.

        Raises:
            None.
        """
        self.sources = sources
        self.poster = poster
        self.alt_text = alt_text

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload: dict[str, Any] = {
            "type": "Media",
            "sources": [x.serialize() for x in self.sources],
        }
        if self.poster:
            payload["poster"] = self.poster
        if self.alt_text:
            payload["altText"] = self.alt_text
        return payload


class TextBlock(CardElement):
    """Displays text, allowing control over font sizes, weight, and color.

    Schema Explorer: https://adaptivecards.io/explorer/TextBlock.html
    """

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
        """Build a TextBlock element.

        Args:
            text: Text to display. A subset of markdown is supported (https://aka.ms/ACTextFeatures)
            color: Controls the color of TextBlock elements.
            font_type: Type of font to use for rendering.
            horizontal_alignment: Controls the horizontal text alignment. When not specified,
                the value of horizontalAlignment is inherited from the parent container. If no
                parent container has horizontalAlignment set, it defaults to Left.
            is_subtle: If true, displays text slightly toned down to appear less prominent.
                Default: ``False``
            max_lines: Specifies the maximum number of lines to display. `text` will be
                clipped if it exceeds `max_lines`.
            size: Controls size of text.
            weight: Controls the weight of TextBlock elements.
            wrap: If true, allow `text` to wrap. Otherwise, text is clipped. Default: False
            style: The style of this TextBlock for accessibility purposes.

        Returns:
            None.

        Raises:
            None.
        """
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

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload: dict[str, Any] = {
            "type": "TextBlock",
            "text": self.text,
        }
        if self.color:
            payload["color"] = self.color
        if self.font_type:
            payload["fontType"] = self.font_type
        if self.horizontal_alignment:
            payload["horizontalAlignment"] = self.horizontal_alignment
        if self.is_subtle:
            payload["isSubtle"] = self.is_subtle
        if self.max_lines:
            payload["maxLines"] = self.max_lines
        if self.size:
            payload["size"] = self.size
        if self.weight:
            payload["weight"] = self.weight
        if self.wrap:
            payload["wrap"] = self.wrap
        if self.style:
            payload["style"] = self.style
        return payload
