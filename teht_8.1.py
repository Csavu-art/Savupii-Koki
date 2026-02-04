import mysql.connector


yhteys = mysql.connector.connect(
    host="localhost",
    user="root",
    password="salasana",
    database="lentokentat"
)

icao = input("Anna ICAO-koodi: ").strip().upper()

kursori = yhteys.cursor()

sql = "SELECT name, municipality FROM airport WHERE ident = %s"
kursori.execute(sql, (icao,))

tulos = kursori.fetchone()

if tulos:
    print(f"Lentokentän nimi: {tulos[0]}")
    print(f"Sijaintikunta: {tulos[1]}")
else:
    print("Lentoasemaa ei löytynyt.")

kursori.close()
yhteys.close()
