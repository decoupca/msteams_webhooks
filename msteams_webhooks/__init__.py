"""msteams_webhooks."""
import ssl
from typing import Any, Optional, Union

import httpx

from msteams_webhooks import types
from msteams_webhooks.actions import Action, OpenURLAction
from msteams_webhooks.buttons import OpenURLButton
from msteams_webhooks.cards import AdaptiveCard, Card, HeroCard, ReceiptCard
from msteams_webhooks.containers import (
    ActionSet,
    Column,
    ColumnSet,
    Container,
    Fact,
    FactSet,
    ImageSet,
    ReceiptFact,
    ReceiptItem,
    Table,
    TableCell,
    TableRow,
)
from msteams_webhooks.elements import Image, Media, MediaSource, TextBlock
from msteams_webhooks.exceptions import TeamsRateLimitError, TeamsWebhookError


class TeamsWebhook:
    """Core webhook class.

    Dispatches messages to webhook URL.
    """

    def __init__(
        self,
        url: str,
        *,
        verify: Union[str, bool, ssl.SSLContext] = True,
        timeout: float = 15.0,
    ) -> None:
        """Construct webhook object.

        Args:
            url: Teams webhook URL to send all cards (messages) to.
            verify: How to handle HTTPS certificate verification.
            timeout: Global timeout in seconds for all HTTP operations.
                May be further tuned with an ``httpx.Timeout`` object.

        Returns:
            None.

        Raises:
            None.
        """
        self.url = url
        self.client = httpx.Client(verify=verify, timeout=timeout)
        self.response = None

    def send_card(self, card: Optional[Card] = None, json: Optional[dict[Any, Any]] = None) -> None:
        """Sends a card to the channel.

        Args:
            card: The ``Card`` to send. Only one card may be sent at a time.
            json: Raw JSON card data to send. Useful for debugging or testing.

        Returns:
            None.

        Raises:
            None.
        """
        # Since the attachments value is a list, you might think you can send more
        # than one card to the channel at once, but this isn't true. If you send
        # more than one, only the first will be posted to the channel.
        json = json or {}
        if not card and not json:
            raise ValueError("Must provide either `card` or `json` values.")  # noqa TRY003
        if card:
            json = {"type": "message", "attachments": [card.serialize()]}
        if json:
            json = {"type": "message", "attachments": [json]}
        self.send_json(json=json)

    def send_json(self, json: dict[Any, Any]) -> None:
        """Posts a raw JSON payload to the webhook URL.

        Args:
            json: Data dict that will be converted to JSON before posting to webhook.

        Returns:
            None.

        Raises:
            TeamsWebhookError: if the response was anything other than 200/OK.
            TeamsRateLimitError: if "429" was found inside the response body.
        """
        headers = {"Content-Type": "application/json"}
        self.response = self.client.post(self.url, json=json, headers=headers)
        if self.response.status_code != httpx.codes.OK or "error" in self.response.text.lower():
            raise TeamsWebhookError(self.response.text)
        if "429" in self.response.text:
            # Rate limit errors receive HTTP code 200 with 429 in response body.
            raise TeamsRateLimitError()

    def send_message(
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
        style: Optional[types.TextBlockStyles] = None,
        wrap: bool = True,
    ) -> None:
        """Sends a basic text message to the channel.

        Convenience method that builds an ``AdaptiveCard`` and adds a single ``TextBlock``
        element to its body, with optional formatting.

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
        text_block = TextBlock(
            text=text,
            color=color,
            font_type=font_type,
            horizontal_alignment=horizontal_alignment,
            is_subtle=is_subtle,
            max_lines=max_lines,
            size=size,
            weight=weight,
            wrap=wrap,
            style=style,
        )
        self.send_card(card=AdaptiveCard(body=[text_block]))


class AsyncTeamsWebhook:
    """Core async webhook class.

    Dispatches messages to webhook URL.
    """

    def __init__(
        self,
        url: str,
        *,
        verify: Union[str, bool, ssl.SSLContext] = True,
        timeout: float = 15.0,
    ) -> None:
        """Construct webhook object.

        Args:
            url: Teams webhook URL to send all cards (messages) to.
            verify: How to handle HTTPS certificate verification.
            timeout: Global timeout in seconds for all HTTP operations.
                May be further tuned with an ``httpx.Timeout`` object.

        Returns:
            None.

        Raises:
            None.
        """
        self.url = url
        self.client = httpx.AsyncClient(verify=verify, timeout=timeout)
        self.response = None

    async def send_card(
        self,
        card: Optional[Card] = None,
        json: Optional[dict[Any, Any]] = None,
    ) -> None:
        """Sends a card to the channel.

        Args:
            card: The ``Card`` to send. Only one card may be sent at a time.
            json: Raw JSON card data to send. Useful for debugging or testing.

        Returns:
            None.

        Raises:
            None.
        """
        # Since the attachments value is a list, you might think you can send more
        # than one card to the channel at once, but this isn't true. If you send
        # more than one, only the first will be posted to the channel.
        json = json or {}
        if not card and not json:
            raise ValueError("Must provide either `card` or `json` values.")  # noqa: TRY003
        if card:
            json = {"type": "message", "attachments": [card.serialize()]}
        if json:
            json = {"type": "message", "attachments": [json]}
        await self.send_json(json=json)

    async def send_json(self, json: dict[Any, Any]) -> None:
        """Posts a raw JSON payload to the webhook URL.

        Args:
            json: Data dict that will be converted to JSON before posting to webhook.

        Returns:
            None.

        Raises:
            TeamsWebhookError: if the response was anything other than 200/OK.
            TeamsRateLimitError: if "429" was found inside the response body.
        """
        headers = {"Content-Type": "application/json"}
        self.response = await self.client.post(self.url, json=json, headers=headers)
        if self.response.status_code != httpx.codes.OK:
            raise TeamsWebhookError(self.response.text)
        if "429" in self.response.text:
            # Rate limit errors receive HTTP code 200 with 429 in response body.
            raise TeamsRateLimitError()

    async def send_message(
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
        style: Optional[types.TextBlockStyles] = None,
        wrap: bool = True,
    ) -> None:
        """Sends a basic text message to the channel.

        Convenience method that builds an ``AdaptiveCard`` and adds a single ``TextBlock``
        element to its body, with optional formatting.

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
        text_block = TextBlock(
            text=text,
            color=color,
            font_type=font_type,
            horizontal_alignment=horizontal_alignment,
            is_subtle=is_subtle,
            max_lines=max_lines,
            size=size,
            weight=weight,
            wrap=wrap,
            style=style,
        )
        await self.send_card(card=AdaptiveCard(body=[text_block]))


__all__ = (
    "Action",
    "ActionSet",
    "AdaptiveCard",
    "AsyncTeamsWebhook",
    "Column",
    "ColumnSet",
    "Container",
    "Fact",
    "FactSet",
    "HeroCard",
    "Image",
    "ImageSet",
    "Media",
    "MediaSource",
    "OpenURLAction",
    "OpenURLButton",
    "ReceiptCard",
    "ReceiptFact",
    "ReceiptItem",
    "Table",
    "TableCell",
    "TableRow",
    "TeamsWebhook",
    "TextBlock",
)
