import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))

        for auto in self.autot:
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{self.nimi} – {self.pituus} km")
        print(
            f"{'Rekisteritunnus':<18}"
            f"{'Huippunopeus':>18}"
            f"{'Nopeus':>14}"
            f"{'Matka':>14}"
        )
        print("-" * 64)

        for auto in self.autot:
            print(
                f"{auto.rekisteritunnus:<18}"
                f"{auto.huippunopeus:>13} km/h"
                f"{auto.nopeus:>9} km/h"
                f"{auto.kuljettu_matka:>11} km"
            )

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True

        return False


autot = []

for numero in range(1, 11):
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(f"ABC-{numero}", huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0

while True:
    kilpailu.tunti_kuluu()
    tunnit += 1

    if kilpailu.kilpailu_ohi():
        break

    if tunnit % 10 == 0:
        print(f"\nAikaa kulunut: {tunnit} tuntia")
        kilpailu.tulosta_tilanne()

print(f"\nKilpailu päättyi! Aikaa kului {tunnit} tuntia.")
kilpailu.tulosta_tilanne()