kentat = {}

while True:
    print("\nValitse toiminto:")
    print("1 = Syötä uusi lentoasema")
    print("2 = Hae lentoasema ICAO-koodilla")
    print("3 = Lopeta")

    valinta = input("Valinta: ").strip()

    if valinta == "1":
        icao = input("Anna ICAO-koodi: ").strip().upper()
        nimi = input("Anna lentoaseman nimi: ").strip()

        kentat[icao] = nimi
        print(f"Tallennettu: {icao} = {nimi}")

    elif valinta == "2":
        icao = input("Anna ICAO-koodi: ").strip().upper()

        if icao in kentat:
            print(f"{icao}: {kentat[icao]}")
        else:
            print("ICAO-koodia ei löydy.")

    elif valinta == "3":
        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")
