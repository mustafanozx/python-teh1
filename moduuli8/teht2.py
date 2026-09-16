import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="salasana"
)

maakoodi = input("Anna maakoodi: ")

sql = """
SELECT type, COUNT(*)
FROM airport
WHERE iso_country = %s
GROUP BY type
"""

kursori = yhteys.cursor()
kursori.execute(sql, (maakoodi,))

tulokset = kursori.fetchall()

for rivi in tulokset:
    print(rivi[0], rivi[1])

kursori.close()
yhteys.close()