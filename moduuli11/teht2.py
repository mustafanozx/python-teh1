
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def aja(self, tunnit):
        self.matka += self.nopeus * tunnit


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankinkoko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankinkoko = tankinkoko


sahkoauto = Sähköauto("ABC-15", 180, 52.5)
bensaauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdyta(100)
bensaauto.kiihdyta(80)

sahkoauto.aja(3)
bensaauto.aja(3)

print("Sähköauto:", sahkoauto.matka, "km")
print("Polttomoottoriauto:", bensaauto.matka, "km")
