import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    user="root",
    password="salasana",
    database="lentokentat",
)

maakoodi = input("Anna maakoodi (esim. FI): ").strip().upper()

kursori = yhteys.cursor()

sql = """
SELECT type, COUNT(*) AS lkm
FROM airport
WHERE iso_country = %s
GROUP BY type
ORDER BY lkm DESC
"""
kursori.execute(sql, (maakoodi,))
tulokset = kursori.fetchall()

if tulokset:
    print(f"\nLentokenttien lukumäärät maassa {maakoodi}:")
    for tyyppi, lkm in tulokset:
        print(f"{tyyppi}: {lkm}")
else:
    print("Ei löytynyt lentokenttiä tai maakoodi on väärä.")

kursori.close()
yhteys.close()
