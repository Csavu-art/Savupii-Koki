pituus = float(input("Anna kuhan pituus senttimetreinä: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print("Kuha on alamittoinen. Laske kuha takaisin järveen.")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu:.1f} cm.")
else:
    print("Kala on hyvä vietäväksi")
