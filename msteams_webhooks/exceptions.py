"""msteams_webhooks.exceptions."""


class TeamsWebhookError(Exception):
    """Generic error."""


class TeamsRateLimitError(TeamsWebhookError):
    """Raised when rate limiting is encountered."""

    def __init__(self, *args: object) -> None:
        """Raised when rate limiting is encountered."""
        super().__init__("Rate limit exceeded. Slow messaging rate and try again.", *args)
