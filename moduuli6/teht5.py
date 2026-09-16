def laske_summa(lista):
    summa = 0

    for luku in lista:
        summa = summa + luku

    return summa

luvut = [2, 4, 6, 8]

tulos = laske_summa(luvut)

print(tulos)