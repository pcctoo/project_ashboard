import requests

def rendmsg():
    respons = requests.get("https://api.adviceslip.com/advice")
    x = respons.status_code
    if int(x) == 200:
        b = respons.json()
        b = b['slip']
        b = b['advice']
        return b
    else:
        print(x)
