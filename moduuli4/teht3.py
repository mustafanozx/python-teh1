syote = input("Anna luku: ")

pienin = None
suurin = None

while syote != "":
    luku = float(syote)

    if pienin is None or luku < pienin:
        pienin = luku

    if suurin is None or luku > suurin:
        suurin = luku

    syote = input("Anna luku: ")

print("Pienin luku:", pienin)
print("Suurin luku:", suurin)