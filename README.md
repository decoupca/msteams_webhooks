# msteams_webhooks

A modern Python API for sending messages to Microsoft Teams using webhooks. Requires Python 3.9+

**Warning**: This package is in early development and may introduce breaking changes. You may expect a stable API in the 1.0.0 release. 

## Intro

Teams webhooks do not use plaintext messages, but rather "[cards](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/what-are-cards)" sent as JSON data structures. The format of each structure depends on the [type of card](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference#card-types). This package greatly simplifies creating and sending these cards by generating the required data structure for you, based on simple and famililar Python objects.

Teams webhooks [support most card types](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference#features-that-support-different-card-types), but the most common and flexible type is the [Adaptive Card](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference#adaptive-card). Adaptive cards can contain many types of data including text, images, inputs, and buttons.

This package aims to provide a consistent, stable Python API for all cards and elements supported by the Teams webhook API. 

## Quick Start

### Install package

Until the package reaches stability, this package will not be added to PyPI. For now, install it from git:

`pip install git+https://github.com/decoupca/msteams_webhooks.git`

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

## Manually Build a Card

[Hero Cards](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference#hero-card) provide a simple example of building a card from scratch.

Here's how to build the example Hero Card from the [documentation](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference#hero-card):

```python
from msteams_webhooks import TeamsWebhook
from msteams_webhooks.buttons import OpenURLButton
from msteams_webhooks.cards import AdaptiveCard, HeroCard
channel = TeamsWebhook('<your-webhook-url>')
official_website = OpenURLButton(
    title="Official website",
    url="https://www.seattlemonorail.com"
)
wikipedia_page = OpenURLButton(
    title="Wikipedia page",
    url="https://en.wikipedia.org/wiki/Seattle_Center_Monorail"
)
card = HeroCard(
    title='Seattle Center Monorail',
    subtitle='Seattle Center Monorail',
    text=("The Seattle Center Monorail is an elevated train line between Seattle Center "
            "(near the Space Needle) and downtown Seattle. It was built for the 1962 World's Fair. "
            "Its original two trains, completed in 1961, are still in service."),
    images=["https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Seattle_monorail01_2008-02-25.jpg/1024px-Seattle_monorail01_2008-02-25.jpg"],
    buttons=[official_website, wikipedia_page]
)
channel.send_card(card)
```

## Advanced Usage

### Inspecting JSON Payloads

You can inspect any object's JSON payload by calling its `serialize()` method. This may be helpful when debugging, or learning about an object's schema.

```python
>>> from msteams_webhooks import TeamsWebhook, AdaptiveCard, TextBlock
>>> import pprint
>>> channel = TeamsWebhook('<your-webhook-url>')
>>> card = AdaptiveCard()
>>> text_block = TextBlock(text="Hello, World!", color='good', weight='bolder')
>>> card.body.append(text_block)
>>> pprint.pprint(card.serialize())
{'content': {'$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
             'body': [{'color': 'good',
                       'text': 'Hello, World!',
                       'type': 'TextBlock',
                       'weight': 'bolder'}],
             'type': 'AdaptiveCard',
             'version': '1.5'},
 'contentType': 'application/vnd.microsoft.card.adaptive'}
```

### HTTP Tuning

#### HTTPS Certificate Verification

You can provide a custom CA cert bundle directly to `TeamsWebhook`:

```python
channel = TeamsWebhook(url='<your-webhook-url>', verify='/path/to/internal/ca.pem')
```

Or, disable verification altogether with `verify=False`.

#### Adjusting Timeouts

You can override the default 15sec timeout when constructing `TeamsWebhook`:

```python
channel = TeamsWebhook(url='<your-webhook-url>', timeout=30.0)
```

You can [further tune timeouts](https://www.python-httpx.org/advanced/#setting-and-disabling-timeouts) using options provided by `httpx`, if necessary.

#### Advanced HTTP Tuning

All webhook requests are dispatched by an [`httpx.Client`](https://www.python-httpx.org/api/#client) instance, stored in the `TeamsWebhook.client` property. For full control over all HTTP options, you can create your own client and replace the `client` property:

```python
from msteams_webhooks import TeamsWebhook
import httpx

channel = TeamsWebhook('<your-webhook-url>')
channel.client = httpx.Client(...)
```

## Limitations

### Mentions

#### Whole Channel

There is currently no way to notify/mention the whole channel using webhooks. This feature is only available to [Bots](https://learn.microsoft.com/en-us/microsoftteams/platform/bots/what-are-bots).

#### Individuals

The Teams webhooks API does support [mentioning individuals](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-format?tabs=adaptive-md%2Cdesktop%2Cconnector-html#user-mention-in-incoming-webhook-with-adaptive-cards). However, the approach is somewhat complex and has not yet been implemented by `msteams_webhooks`.
