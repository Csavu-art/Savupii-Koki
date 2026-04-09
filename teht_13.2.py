from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)

# Tietokantayhteys
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="KiraTina9_DB",
    autocommit=True
)

@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        kokonaisluku = int(luku)

        if kokonaisluku <= 1:
            onko_alkuluku = False
        else:
            onko_alkuluku = True
            for x in range(2, kokonaisluku):
                if kokonaisluku % x == 0:
                    onko_alkuluku = False
                    break

        vastaus = {
            "Number": kokonaisluku,
            "isPrime": onko_alkuluku
        }

        return Response(
            response=json.dumps(vastaus),
            status=200,
            mimetype="application/json"
        )

    except ValueError:
        vastaus = {
            "status": 400,
            "text": "Virheellinen luku"
        }

        return Response(
            response=json.dumps(vastaus),
            status=400,
            mimetype="application/json"
        )


@app.route('/kentta/<icao>')
def kentta(icao):
    try:
        sql = f"SELECT ident, name, municipality FROM airport WHERE ident = '{kentta}' limit 5"
        kursori = yhteys.cursor()
        kursori.execute(sql, (icao,))
        tulos = kursori.fetchone()

        if tulos:
            vastaus = {
                "ICAO": tulos[0],
                "Name": tulos[1],
                "Municipality": tulos[2]
            }
            tilakoodi = 200
        else:
            vastaus = {
                "status": 404,
                "text": "Lentokenttää ei löytynyt"
            }
            tilakoodi = 404

        return Response(
            response=json.dumps(vastaus),
            status=tilakoodi,
            mimetype="application/json"
        )

    except mysql.connector.Error:
        vastaus = {
            "status": 500,
            "text": "Tietokantahaku epäonnistui"
        }

        return Response(
            response=json.dumps(vastaus),
            status=500,
            mimetype="application/json"
        )


app.run(use_reloader=True, host='127.0.0.1', port=3000)