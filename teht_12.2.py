import requests

api_avain = "OMA_API_AVAIN"
paikkakunta = input("Anna paikkakunta: ")

url = "https://api.openweathermap.org/data/2.5/weather"

parametrit = {
    "q": paikkakunta,
    "appid": api_avain
}

try:
    vastaus = requests.get(url, params=parametrit)
    data = vastaus.json()

    if vastaus.status_code == 200:
        saakuvaus = data["weather"][0]["description"]
        lampotila_kelvin = data["main"]["temp"]
        lampotila_celsius = lampotila_kelvin - 273.15

        print(f"Sää paikkakunnalla {paikkakunta}: {saakuvaus}")
        print(f"Lämpötila: {lampotila_celsius:.1f} °C")
    else:
        print("Sään hakeminen epäonnistui.")
        print(data)
except requests.exceptions.RequestException:
    print("Yhteysvirhe.")