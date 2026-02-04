import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host="localhost",
    user="root",
    password="salasana",
    database="lentokentat",
)

def hae_koordinaatit(icao: str):
    kursori = yhteys.cursor()
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao,))
    rivi = kursori.fetchone()
    kursori.close()
    return rivi  # None jos ei löydy

icao1 = input("Anna 1. ICAO-koodi: ").strip().upper()
icao2 = input("Anna 2. ICAO-koodi: ").strip().upper()

p1 = hae_koordinaatit(icao1)
p2 = hae_koordinaatit(icao2)

if not p1:
    print(f"ICAO-koodia ei löytynyt: {icao1}")
elif not p2:
    print(f"ICAO-koodia ei löytynyt: {icao2}")
else:
    # p1 ja p2 ovat (lat, lon)
    etaisyys_km = geodesic(p1, p2).kilometers
    print(f"Lentokenttien {icao1} ja {icao2} välinen etäisyys on {etaisyys_km:.2f} km.")

yhteys.close()
