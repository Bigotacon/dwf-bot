import requests

headers = {
    'authority': 'app.cloudsearchapp.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://dwarvenforge.com',
    'referer': 'https://dwarvenforge.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

params = {
    'type': 'shopify',
    'shop': 'dwarven-forge.myshopify.com',
}

data = '{"q":null,"lang":"en","facet":true,"filters":[],"limits":{"products":0,"categories":0,"pages":0},"conditions":{"collection_handle":["all-products"]}}'

response = requests.post('https://app.cloudsearchapp.com/api/v1/search', params=params, headers=headers, data=data).json()
#print(response)
for item in response['facets']:
    print(item['name'])