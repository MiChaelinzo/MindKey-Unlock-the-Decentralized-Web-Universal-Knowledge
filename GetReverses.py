import requests

url = "https://api.unstoppabledomains.com/resolve/reverse/query"

query = {
  "data": [
    "string",
    "string",
    "x"
  ],
  "sortBy": "string",
  "sortDirection": "string",
  "startingAfter": "string",
  "perPage": "0"
}

payload = {
  "addresses": [
    "string"
  ]
}

headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer <YOUR_TOKEN_HERE>"
}

response = requests.post(url, json=payload, headers=headers, params=query)

data = response.json()
print(data)
