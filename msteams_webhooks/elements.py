"""msteams_webhooks.elements."""
from typing import Any, ClassVar, Literal, Optional, Union

from msteams_webhooks import types
from msteams_webhooks.actions import Action


class CardElement:
    """Base element class."""

    TYPE = ""
    ATTR_MAP = None

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload = {"type": self.TYPE}
        for attr, key in self.ATTR_MAP.items():
            if (value := getattr(self, attr)) and value is not None:
                payload[key] = value
        return payload


class TextBlock(CardElement):
    """TextBlock element.

    https://adaptivecards.io/explorer/TextBlock.html
    """

    TYPE = "TextBlock"
    ATTR_MAP: ClassVar[dict[str, str]] = {
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
        """Displays text, allowing control over font sizes, weight, and color.

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
            N/A
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


class Image(CardElement):
    """Image element.

    https://adaptivecards.io/explorer/Image.html.
    """

    TYPE = "Image"
    ATTR_MAP: ClassVar[dict[str, str]] = {
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
            N/A
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


class MediaSource(CardElement):
    """Media source element.

    https://adaptivecards.io/explorer/MediaSource.html
    """

    def __init__(self, url: types.URL, *, mime_type: Optional[str] = None) -> None:
        """Defines a source for a Media element.

        Args:
            url: URL to media. Supports data URI in version 1.2+
            mime_type: Mime type of associated media (e.g. "video/mp4"). For YouTube
                and other Web video URLs, mime_type can be omitted.

        Returns:
            None.

        Raises:
            N/A
        """
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
            N/A
        """
        self.sources = sources
        self.poster = poster
        self.alt_text = alt_text

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload = {
            "type": "Media",
            "sources": [x.serialize() for x in self.sources],
        }
        if self.poster:
            payload["poster"] = self.poster
        if self.alt_text:
            payload["altText"] = self.alt_text
        return payload
