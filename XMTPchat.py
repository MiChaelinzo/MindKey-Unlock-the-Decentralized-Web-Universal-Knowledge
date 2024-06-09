import requests

url = "https://api.unstoppabledomains.com/messaging/xmtp/topics/accept"

payload = {
  "ownerAddress": 123,
  "signedPublicKey": 456,
  "registrations": [
    {
      "accept": True,
      "block": True,
      "topic": "topic-123",
      "peerAddress": "string",
      "signature": "<signed topic ID>"
    }
  ]
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(data)
