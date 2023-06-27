"""msteams_webhooks.cards."""
from typing import Any, Optional, Union

from msteams_webhooks import types
from msteams_webhooks.actions import Action
from msteams_webhooks.buttons import Button
from msteams_webhooks.containers import CardContainer
from msteams_webhooks.elements import CardElement


class Card:
    """Base card class."""

    TYPE = ""
    SCHEMA = ""

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        return {}


class AdaptiveCard(Card):
    """Adaptive Card.

    https://adaptivecards.io/explorer/AdaptiveCard.html
    """

    TYPE = "AdaptiveCard"
    SCHEMA = "http://adaptivecards.io/schemas/adaptive-card.json"

    def __init__(
        self,
        *,
        body: Optional[list[Union[CardElement, CardContainer]]] = None,
        actions: Optional[list[Action]] = None,
        version: Optional[str] = None,
        background_image: Optional[types.URL] = None,
        min_height: Optional[str] = None,
        rtl: Optional[bool] = None,
        speak: Optional[str] = None,
        lang: Optional[str] = None,
        vertical_content_alignment: Optional[types.VerticalAlignmentTypes] = None,
    ) -> None:
        """An Adaptive Card, containing a free-form body of card elements.

        Args:
            body: The card elements to show in the primary card region.
            actions: The Actions to show in the card's action bar.
            version: Schema version that this card requires. If a client is lower than
                this version, the fallbackText will be rendered. NOTE: Version is not
                required for cards within an ``Action.ShowCard``. However, it is required
                for the top-level card.
            background_image: Specifies the background image of the card.
            min_height: Specifies the minimum height of the card.
            rtl: When true content in this Adaptive Card should be presented right to left.
                When ``False`` content in this Adaptive Card should be presented left to right.
                If unset, the default platform behavior will apply.
            speak: Specifies what should be spoken for this entire card. This is simple text or
                SSML fragment.
            lang: The 2-letter ISO-639-1 language used in the card. Used to localize any
                date/time functions.
            vertical_content_alignment: Defines how the content should be aligned vertically
                within the container. Only relevant for fixed-height cards, or cards with a
                `min_height` specified.

        Returns:
            None.

        Raises:
            N/A
        """
        self.version = version or "1.6"
        self.body = body or []
        self.actions = actions or []
        self.background_image = background_image
        self.min_height = min_height
        self.rtl = rtl
        self.speak = speak
        self.lang = lang
        self.vertical_content_alignment = vertical_content_alignment

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload = {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "$schema": self.SCHEMA,
                "type": self.TYPE,
                "version": self.version,
            },
        }
        if self.body:
            payload["content"]["body"] = [x.serialize() for x in self.body]
        if self.actions:
            payload["content"]["actions"] = [x.serialize() for x in self.actions]
        if self.background_image:
            payload["content"]["backgroundImage"] = self.background_image
        if self.min_height:
            payload["content"]["minHeight"] = self.min_height
        if self.rtl is not None:
            payload["content"]["rtl"] = self.rtl
        if self.speak:
            payload["content"]["speak"] = self.speak
        if self.lang:
            payload["content"]["lang"] = self.lang
        if self.vertical_content_alignment:
            payload["content"]["verticalContentAlignment"] = self.vertical_content_alignment
        return payload


class HeroCard(Card):
    """Hero Card.

    A card that typically contains a single large image, one or more buttons, and text.
    """

    TYPE = "application/vnd.microsoft.card.hero"

    def __init__(
        self,
        title: str,
        text: str,
        *,
        subtitle: Optional[str] = None,
        images: Optional[list[types.URL]] = None,
        buttons: Optional[list[Button]] = None,
    ) -> None:
        """Display a single large image, one or more buttons, and text.

        Args:
            title: Main text to display.
            text: Text to display. A subset of markdown is supported (https://aka.ms/ACTextFeatures)
            subtitle: Sub-title to display under `title`.
            images: List of image URLs to display.
            buttons: List of buttons to include in the card.

        Returns:
            None.

        Raises:
            N/A
        """
        self.title = title
        self.text = text
        self.subtitle = subtitle
        self.images = images
        self.buttons = buttons

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        payload: dict[str, Any] = {"contentType": self.TYPE, "content": {}}
        payload["content"]["title"] = self.title
        payload["content"]["text"] = self.text
        if self.subtitle:
            payload["content"]["subtitle"] = self.subtitle
        if self.images:
            payload["content"]["images"] = [{"url": img} for img in self.images]
        if self.buttons:
            payload["content"]["buttons"] = [x.serialize() for x in self.buttons]
        return payload
