from flask import Flask, Response
import json

app = Flask(__name__)


def onko_alkuluku(luku):
    if luku < 2:
        return False

    for i in range(2, luku):
        if luku % i == 0:
            return False

    return True


@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        luku = int(luku)
        tulos = onko_alkuluku(luku)

        tilakoodi = 200
        vastaus = {
            "Number": luku,
            "isPrime": tulos
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Parametri ei ole kokonaisluku"
        }

    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, status=tilakoodi, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(virhe):
    vastaus = {
        "status": 404,
        "teksti": "Virheellinen päätepiste"
    }
    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)