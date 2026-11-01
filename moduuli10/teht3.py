class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f"Hissi on kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros < self.alin_kerros or kohdekerros > self.ylin_kerros:
            print("Tätä kerrosta ei ole.")
            return

        while self.kerros < kohdekerros:
            self.kerros_ylös()

        while self.kerros > kohdekerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.hissit = []

        for numero in range(hissien_lukumaara):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if 1 <= hissin_numero <= len(self.hissit):
            print(f"\nHissi {hissin_numero}:")
            self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)
        else:
            print("Tätä hissiä ei ole.")

    def palohälytys(self):
        print("\nPalohälytys! Kaikki hissit alimpaan kerrokseen.")

        for numero, hissi in enumerate(self.hissit, start=1):
            print(f"\nHissi {numero}:")
            hissi.siirry_kerrokseen(hissi.alin_kerros)


talo = Talo(1, 10, 3)

talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 8)
talo.aja_hissiä(3, 4)

talo.palohälytys()