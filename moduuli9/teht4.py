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


autot = []

for numero in range(1, 11):
    huippunopeus = random.randint(100, 200)
    auto = Auto(f"ABC-{numero}", huippunopeus)
    autot.append(auto)

kilpailu_jatkuu = True

while kilpailu_jatkuu:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))

    for auto in autot:
        auto.kulje(1)

    for auto in autot:
        if auto.kuljettu_matka >= 10000:
            kilpailu_jatkuu = False

print(
    f"{'Rekisteritunnus':<18}"
    f"{'Huippunopeus':>15}"
    f"{'Nopeus':>12}"
    f"{'Matka':>15}"
)
print("-" * 60)

for auto in autot:
    print(
        f"{auto.rekisteritunnus:<18}"
        f"{auto.huippunopeus:>10} km/h"
        f"{auto.nopeus:>7} km/h"
        f"{auto.kuljettu_matka:>12} km"
    )