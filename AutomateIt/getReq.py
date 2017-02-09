import requests

payload = { 'q': 'tharnid' }
r = requests.get('https://github.com/search', params=payload)
print("Request URL: " , r.url)
