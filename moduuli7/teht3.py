lentoasemat = {}

while True:
    toiminto = input("Valitse: uusi, haku tai lopeta: ")

    if toiminto == "uusi":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")

        lentoasemat[icao] = nimi

    elif toiminto == "haku":
        icao = input("Anna ICAO-koodi: ")

        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")

    elif toiminto == "lopeta":
        break

    else:
        print("Virheellinen valinta.")