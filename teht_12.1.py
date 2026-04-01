import requests

try:
    vastaus = requests.get("https://api.chucknorris.io/jokes/random")
    data = vastaus.json()
    print(data["value"])
except requests.exceptions.RequestException:
    print("Vitsin hakeminen epäonnistui.")