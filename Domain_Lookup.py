import requests

url = "https://api.unstoppabledomains.com/resolve/chains/matic/rpc"

headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer <YOUR_TOKEN_HERE>"
}

response = requests.post(url, headers=headers)

data = response.json()
print(data)
