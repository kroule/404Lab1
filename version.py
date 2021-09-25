import requests

print(requests.__version__)

r = requests.get("https://raw.githubusercontent.com/kroule/404Lab1/main/version.py")
print(r.text)
