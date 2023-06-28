from msteams_webhooks.buttons import OpenURLButton
from msteams_webhooks.cards import ReceiptCard
from msteams_webhooks.containers import ReceiptFact, ReceiptItem


def test_receipt_card() -> None:
    payload = {
        "contentType": "application/vnd.microsoft.card.receipt",
        "content": {
            "title": "John Doe",
            "total": "$ 90.95",
            "items": [
                {
                    "title": "Data Transfer",
                    "price": "$ 38.45",
                    "quantity": "368",
                    "image": {
                        "url": "https://github.com/amido/azure-vector-icons/raw/master/renders/traffic-manager.png"
                    },
                },
                {
                    "title": "App Service",
                    "price": "$ 45.00",
                    "quantity": "720",
                    "image": {
                        "url": "https://github.com/amido/azure-vector-icons/raw/master/renders/cloud-service.png"
                    },
                },
            ],
            "facts": [
                {"key": "Order Number", "value": "1234"},
                {"key": "Payment Method", "value": "VISA 5555-****"},
            ],
            "tax": "$ 7.50",
            "buttons": [
                {
                    "type": "openUrl",
                    "title": "More information",
                    "value": "https://azure.microsoft.com/en-us/pricing/",
                    "image": "https://account.windowsazure.com/content/6.10.1.38-.8225.160809-1618/aux-pre/images/offer-icon-freetrial.png",
                }
            ],
        },
    }
    items = [
        ReceiptItem(
            title="Data Transfer",
            price="$ 38.45",
            quantity=368,
            image="https://github.com/amido/azure-vector-icons/raw/master/renders/traffic-manager.png",
        ),
        ReceiptItem(
            title="App Service",
            price="$ 45.00",
            quantity=720,
            image="https://github.com/amido/azure-vector-icons/raw/master/renders/cloud-service.png",
        ),
    ]
    facts = [
        ReceiptFact(key="Order Number", value="1234"),
        ReceiptFact(key="Payment Method", value="VISA 5555-****"),
    ]
    button = OpenURLButton(
        url="https://azure.microsoft.com/en-us/pricing/",
        title="More information",
        image="https://account.windowsazure.com/content/6.10.1.38-.8225.160809-1618/aux-pre/images/offer-icon-freetrial.png",
    )
    card = ReceiptCard(
        title="John Doe",
        items=items,
        facts=facts,
        total="$ 90.95",
        tax="$ 7.50",
        buttons=[button],
    )
    assert card.serialize() == payload
