import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="salasana"
)

icao = input("Anna lentoaseman ICAO-koodi: ")

sql = "SELECT name, municipality FROM airport WHERE ident = %s"

kursori = yhteys.cursor()
kursori.execute(sql, (icao,))

tulos = kursori.fetchone()

if tulos:
    print("Lentoasema:", tulos[0])
    print("Sijaintikunta:", tulos[1])
else:
    print("Lentoasemaa ei löytynyt.")

kursori.close()
yhteys.close()