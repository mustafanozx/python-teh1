import math

def pizzan_yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2
    sade_metreina = sade / 100

    pinta_ala = math.pi * sade_metreina ** 2

    return hinta / pinta_ala


halkaisija1 = float(input("Anna pizzan 1 halkaisija cm: "))
hinta1 = float(input("Anna pizzan 1 hinta: "))

halkaisija2 = float(input("Anna pizzan 2 halkaisija cm: "))
hinta2 = float(input("Anna pizzan 2 hinta: "))

yksikkohinta1 = pizzan_yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = pizzan_yksikkohinta(halkaisija2, hinta2)

print("Pizza 1:", yksikkohinta1, "€/m²")
print("Pizza 2:", yksikkohinta2, "€/m²")

if yksikkohinta1 < yksikkohinta2:
    print("Pizza 1 antaa paremman vastineen rahalle.")
elif yksikkohinta2 < yksikkohinta1:
    print("Pizza 2 antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat yhtä edullisia.")