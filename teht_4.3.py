pienin = None
suurin = None

syote = input("Anna luku (Enter lopettaa): ")

while syote != "":
    luku = float(syote)  # voi käyttää myös int(syöte)

    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku

    syote = input("Anna luku (Enter lopettaa): ")

if pienin is None:
    print("Et antanut yhtään lukua.")
else:
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")
