pituus = float(input("Anna pituus senttimetrinä:"))

if pituus < 37:
    puuttuu = 37-pituus
    print("Pituus on alle 37 senttimetriä palautta sen veteen.")
    print("Pituutta puuttuu", puuttuu, "senttimetriä.")

else:
    print("Pituus on 37 senttimetriä tai enemmän.")
    print("pituus on hyväksytty.")

