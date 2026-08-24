leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))
grammat = (leiviskat * 20 * 32 + naulat * 32 + luodit) * 13.3
kilogrammat = int(grammat // 1000)
grammat_jaljella = grammat % 1000

print("Massa nykymittojen mukaan:", kilogrammat, "kilogrammaa ja", grammat_jaljella, "grammaa.")

