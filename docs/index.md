# msteams_webhooks

A modern Python API for sending messages to Microsoft Teams using webhooks. Requires Python 3.9+.

!!! warning "Unstable API"
    This package is in early development and may introduce breaking changes. You can expect a stable API in the 1.0.0 release.

## Intro

Instead of plaintext messages, Microsoft Teams uses JSON data structures called [cards](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/what-are-cards). This package aims to simplify creating and sending these cards by building these data structures for you, using simple and well-documented Python objects.

## Quick Start

### Install

Until the package reaches stability, this package will not be added to PyPI. For now, install it from git:

```python
pip install git+https://github.com/decoupca/msteams_webhooks.git
```

### Create a Webhook URL

Follow [this guide](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=dotnet#create-incoming-webhooks-1) to create a webhook URL for your channel.

### Send a Basic Message

```python
from msteams_webhooks import TeamsWebhook

channel = TeamsWebhook('<your-webhook-url>')
channel.send_message("Hello, World!")
```

Behind the scences, this creates an [Adaptive Card](https://adaptivecards.io/) and adds a single [`TextBlock`](https://adaptivecards.io/explorer/TextBlock.html) element to the body before sending it to the channel.

### Customize the Message

You can further customize the message with all properties supported by a [`TextBlock`](https://adaptivecards.io/explorer/TextBlock.html) element. For example:

```python
channel.send_message(
    text="Hello, World!",
    color="good",
    horizontal_alignment="center",
    font_size="large",
    weight="bolder"
)
```

The `text` property also supports [a subset of Markdown](https://support.microsoft.com/en-us/office/use-markdown-formatting-in-teams-4d10bd65-55e2-4b2d-a1f3-2bebdcd2c772) formatting syntax.