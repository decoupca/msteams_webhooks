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

### Asynchronous API

If you need to send many messages at once and performance is a factor, asynchronous code may help. Async code typically outperforms multithreaded code for I/O bound tasks like posting HTTP payloads to remote servers. Here's a basic async example that sends different messages to three channels at the same time:

```python
from msteams_webhooks import AsyncTeamsWebhook
import asyncio
channel1 = AsyncTeamsWebhook('https://webhook.office.com/webhookb2/your/channel/url1')
channel2 = AsyncTeamsWebhook('https://webhook.office.com/webhookb2/your/channel/url2')
channel3 = AsyncTeamsWebhook('https://webhook.office.com/webhookb2/your/channel/url3')
async def send_messages() -> None:
    await asyncio.gather(
        channel1.send_message('Channel 1 message'),
        channel2.send_message('Channel 2 message'),
        channel3.send_message('Channel 3 message'),
    )
asyncio.run(send_messages())
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

The Teams webhooks API supports [mentioning individuals](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-format?tabs=adaptive-md%2Cdesktop%2Cconnector-html#user-mention-in-incoming-webhook-with-adaptive-cards). However, the approach is somewhat complex and has not yet been implemented by `msteams_webhooks`.
