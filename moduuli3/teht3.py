sukupuoli = input("Anna sukupuoli (mies/nainen): ")

hemoglobiiniarvon = float(input("Anna hemoglobiiniarvo g/l: "))

if sukupuoli == "mies":
    if hemoglobiiniarvon < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvon <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

elif sukupuoli == "nainen":
    if hemoglobiiniarvon < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvon <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
        
