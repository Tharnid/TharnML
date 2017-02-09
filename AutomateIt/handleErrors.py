import requests

try:
    r = requests.get("http://www.googles.com/")
except requests.exceptions.RequestException as e:
    print("Error Response:", e.message)
