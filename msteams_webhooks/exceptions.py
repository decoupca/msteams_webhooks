class TeamsWebhookError(Exception):
    """Generic error."""



class TeamsRateLimitError(TeamsWebhookError):
    """Raised when rate limiting is encountered."""

