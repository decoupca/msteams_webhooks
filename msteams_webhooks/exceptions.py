class TeamsWebhookError(Exception):
    """Generic error."""

    pass


class EmptyPayloadError(TeamsWebhookError):
    """Raised when attempting to send a webhook with an empty payload."""

    pass


class TeamsRateLimitError(TeamsWebhookError):
    """Raised when rate limiting is encountered."""

    pass
