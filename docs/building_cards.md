# Building Cards

Cards form the basis of any Teams message.

The most common and flexible card is the [Adaptive Card](https://adaptivecards.io/). Adaptive Cards may include any combination of text, images, and media inside any number of containers.

Let's build a basic Adaptive Card using inline objects:

```python
from msteams_webhooks import AdaptiveCard, Image, TextBlock
card = AdaptiveCard(body=[
    Image(url="https://adaptivecards.io/content/cats/1.png", alt_text="Cat"),
    TextBlock(text="This is a picture of a cat.")
])
```

You can also build cards incrementally:

```python
from msteams_webhooks import AdaptiveCard, Image, TextBlock
card = AdaptiveCard()
image = Image(url="https://adaptivecards.io/content/cats/1.png", alt_text="Cat")
text_block = TextBlock(text="This is a picture of a cat.")
card.body.extend([image, text_block])
```

You can also change properties of any object after building it:

```python
text_block.text = "This text will overwrite the text provided above."
```

# Sending Cards

Sending cards to a Teams channel requires a webhook URL. Follow [this guide](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=dotnet#create-incoming-webhooks-1) to get one for your channel.

Then, build a `TeamsWebhook` instance to send the card:

```python
from msteams_webhooks import TeamsWebhook
channel = TeamsWebhook('<your-webhook-url>')
channel.send_card(card)
```

The `TeamsWebhook` class handles all HTTP-related tasks. Have a look at [Advanced] for tuning options.