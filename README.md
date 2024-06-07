# MindKey-Unlock-the-Decentralized-Web-Universal-Knowledge

![Gemini_Generated_Image_bbvecbbvecbbvecb](https://github.com/MiChaelinzo/MindKey-Unlock-the-Decentralized-Web-Universal-Knowledge/assets/68110223/31a14aa6-7484-4a84-96a3-5ff2802da72e)


# Example of Get Records for a Domain

<img width="446" alt="Screenshot 2024-06-07 101035" src="https://github.com/MiChaelinzo/MindKey-Unlock-the-Decentralized-Web-Universal-Knowledge/assets/68110223/f5c57af0-5260-4320-a231-e161fa508677">

import requests

domain_name = "YOUR_domainName_PARAMETER"
url = "https://api.unstoppabledomains.com/resolve/domains/" + domain_name

headers = {"Authorization": "Bearer <YOUR_TOKEN_HERE>"}

response = requests.get(url, headers=headers)

data = response.json()
print(data)

