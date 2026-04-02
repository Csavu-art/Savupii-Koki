from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):

    kokonaisluku = int(luku)
    onko_alkuluku = True
    for x in range(2, kokonaisluku):
        if kokonaisluku % x == 0:
            onko_alkuluku = False
            break

    vastaus = {
        "Number" : luku,
        "IsPrime" : onko_alkuluku
    }

    return vastaus


app.run(use_reloader=True, host='127.0.0.1', port=3000)