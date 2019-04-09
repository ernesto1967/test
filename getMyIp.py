import requests

response = requests.get("http://checkip.dyndns.org")
print("status:", response.status_code)
print("text:", response.text)