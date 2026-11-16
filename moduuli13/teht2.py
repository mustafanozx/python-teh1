
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


@app.route("/kentta/<icao>")
def hae_kentta(icao):

    yhteys = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="M20042004",
        database="flight_game"
    )

    kursori = yhteys.cursor()

    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao.upper(),))

    tulos = kursori.fetchone()

    kursori.close()
    yhteys.close()

    if tulos:
        return jsonify({
            "ICAO": icao.upper(),
            "Name": tulos[0],
            "Municipality": tulos[1]
        })

    return jsonify({"error": "Lentokenttää ei löytynyt"}), 404


app.run(port=3000)
