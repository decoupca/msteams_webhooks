class TeamsWebhookError(Exception):
    """Generic error."""

    pass


class TeamsRateLimitError(TeamsWebhookError):
    """Raised when rate limiting is encountered."""

    pass
