luvut = []

while True:
    syote = input("Anna luku: ")

    if syote == "":
        break

    luku = float(syote)
    luvut.append(luku)

luvut.sort(reverse=True)

for luku in luvut[:5]:
    print(luku)