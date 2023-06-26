import ssl
from typing import Optional, Union

import httpx

from msteams_webhooks import types
from msteams_webhooks.cards import AdaptiveCard, Card, HeroCard
from msteams_webhooks.elements import TextBlock
from msteams_webhooks.exceptions import TeamsRateLimitError, TeamsWebhookError


class TeamsWebhook:
    def __init__(
        self,
        url: types.URL,
        *,
        verify: Union[str, bool, ssl.SSLContext] = True,
        timeout: float = 15.0,
    ) -> None:
        self.url = url
        self.client = httpx.Client(verify=verify, timeout=timeout)
        self.response = None

    def send_card(self, card: Card) -> None:
        """Sends a card to the channel.

        Args:
            card: The card to send.

        Returns:
            None.

        Raises:
            TeamsWebhookError if the response was not 200/OK.
            TeamsRateLimitError if 429 was found inside the response body.
        """
        headers = {"Content-Type": "application/json"}
        # Even though the attachments key as a list implies that more than one card
        # may be sent in a single webhook call, this is not the case. If you send more
        # than one card, only the first will be posted to the channel.
        data = {"type": "message", "attachments": [card.serialize()]}
        self.response = self.client.post(self.url, json=data, headers=headers)
        if self.response.status_code != httpx.codes.OK:
            raise TeamsWebhookError(self.response.text)
        if "429" in self.response.text:
            # Rate limit errors receive HTTP code 200 with 429 in response body.
            raise TeamsRateLimitError("Exceeded message rate limit.")

    def send_message(
        self,
        text: str,
        *,
        font_type: Optional[types.FontTypes] = None,
        horizontal_alignment: Optional[types.HorizontalAlignmentTypes] = None,
        is_subtle: Optional[bool] = None,
        max_lines: Optional[int] = None,
        size: Optional[types.FontSizes] = None,
        weight: Optional[types.FontWeights] = None,
        style: Optional[types.TextBlockStyles] = None,
        wrap: bool = True,
    ) -> None:
        """Sends a basic message to the channel.

        Builds an Adaptive Card and adds a TextBlock element with provided info.
        """
        text_block = TextBlock(
            text=text,
            font_type=font_type,
            horizontal_alignment=horizontal_alignment,
            is_subtle=is_subtle,
            max_lines=max_lines,
            size=size,
            weight=weight,
            wrap=wrap,
            style=style,
        )
        card = AdaptiveCard(body=[text_block])
        self.send_card(card=card)


__all__ = (
    "TeamsWebhook",
    "AdaptiveCard",
    "HeroCard",
    "TextBlock",
)
