# MindKey-Unlock-the-Decentralized-Web-Universal-Knowledge

![Gemini_Generated_Image_wsuzmtwsuzmtwsuz](https://github.com/MiChaelinzo/MindKey-Unlock-the-Decentralized-Web-Universal-Knowledge/assets/68110223/7f284f79-6e6a-4c54-b7c8-af4e935ddc8d)

![Gemini_Generated_Image_l48qlwl48qlwl48q](https://github.com/MiChaelinzo/MindKey-Unlock-the-Decentralized-Web-Universal-Knowledge/assets/68110223/8dab71a6-0f30-4538-953f-f8b9812aeec3)


# Example of Get Records for a Domain

<img width="446" alt="Screenshot 2024-06-07 101035" src="https://github.com/MiChaelinzo/MindKey-Unlock-the-Decentralized-Web-Universal-Knowledge/assets/68110223/f5c57af0-5260-4320-a231-e161fa508677">

```
import requests

domain_name = "YOUR_domainName_PARAMETER"
url = "https://api.unstoppabledomains.com/resolve/domains/" + domain_name

headers = {"Authorization": "Bearer <YOUR_TOKEN_HERE>"}

response = requests.get(url, headers=headers)

data = response.json()
print(data)
```
## Getting started with the server-side:

```sh
# Go to https://infura.io/ and get your XRP API key.
# It looks like this: 
# https://rinkeby.infura.io/v3/3fe7c90a4ec34aae900a7900d3fb48dc
# You can use mine for test, but it's free so please create your own at https://infura.io/
# Put your key in 'src/config.json' under 'RippleNetwork'
```

```sh
# Install dependencies
npm install
```

```sh
# Start developing
npm run dev
```

```sh
# Start production server
npm start
```

### Config

```js
{
  "port": 8080, // port to launch app to
  "bodyLimit": "1kb", // max size of request json object
  "RippleNetwork": "" // Infura API key
}
```

## Endpoints

`/createWallet`

```sh
GET localhost:8080/createWallet
```

```js
# response
{
  "address": CREATED_WALLET,
  "privateKey": PRIVATE_KEY
}
```

`/getBalance/SOME_XRP_ADDRESS`

```sh
GET localhost:8080/getBalance/SOME_XRP_ADDRESS
```

```js
# response
{
  "XRPAddress": SOME_XRP_ADDRESS,
  "balance": BALANCE
}
```

`/transaction`

```sh
POST to localhost:8080/transaction
BODY
{
	"privateKey": YOUR_PRIVATE_KEY,
	"amount": AMOUNT,
	"destination": DESTINATION_WALLET
}
```

```js
# response
{
  "txHash": TRANSACTION_HASH
}
```
## Getting started with the client:

As a client we are using NFC Tools Pro to program and write the wallet "app" on the NFC chip.

The "app" has 25 tasks and total 828 bytes.

```sh
# Download 'XRP_profile.json' and save it on your phone somewhere.

# This file is the main app file needed.
```

```sh

## Security tips
- Whitelisting your nfc chip
- Using password encrypted private key (soon)
- Using SSL to communicate to app

We configured app to work on Rinkeby test net, so it’s safe to play with.

If you want to use it on Mainnet, just get that Infura API mainet end-point, and 
copy it to your 'src/config.json' file.

## License

MIT

## Contributions

Thanks to @wingleung and @Omodaka9375 for simple api code [https://github.com/wingleung/Ripple-wallet-api-example
](https://github.com/Omodaka9375/xEth-wallet-for-NFC)https://github.com/Omodaka9375/xEth-wallet-for-NFC


