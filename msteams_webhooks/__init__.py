import ssl
from typing import Union

import httpx

from msteams_webhooks.cards import Card
from msteams_webhooks.exceptions import TeamsRateLimitError, TeamsWebhookError
from msteams_webhooks import types


class TeamsWebhook:
    def __init__(
        self,
        url: types.URL,
        *,
        verify: Union[str, bool, ssl.SSLContext] = True,
        timeout: float = 15.0
    ) -> None:
        self.url = url
        self.client = httpx.Client(verify=verify, timeout=timeout)
        self.response = None

    def send(self, card: Card) -> None:
        headers = {"Content-Type": "application/json"}
        data = {"type": "message", "attachments": [card.serialize()]}
        self.response = self.client.post(self.url, json=data, headers=headers)
        if self.response.status_code != httpx.codes.OK:
            raise TeamsWebhookError(self.response.text)
        if "429" in self.response.text:
            # Rate limit errors receive HTTP code 200 with 429 in response body.
            raise TeamsRateLimitError("Exceeded message rate limit.")
