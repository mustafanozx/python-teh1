import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="salasana"
)

icao1 = input("Anna ensimmäisen lentoaseman ICAO-koodi: ")
icao2 = input("Anna toisen lentoaseman ICAO-koodi: ")

sql = """
SELECT latitude_deg, longitude_deg
FROM airport
WHERE ident = %s
"""

kursori = yhteys.cursor()

kursori.execute(sql, (icao1,))
kentta1 = kursori.fetchone()

kursori.execute(sql, (icao2,))
kentta2 = kursori.fetchone()

if kentta1 and kentta2:
    etaisyys = geodesic(kentta1, kentta2).kilometers
    print("Lentokenttien välinen etäisyys on", round(etaisyys, 2), "km")
else:
    print("Lentoasemaa ei löytynyt.")

kursori.close()
yhteys.close()