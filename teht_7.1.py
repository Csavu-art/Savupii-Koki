kuukausi = int(input("Anna kuukauden numero (1-12): "))
if 1<=kuukausi<=12:
    vuodenajat = ("talvi", "kevät", "kesä", "syksy")

    vuodenaika = vuodenajat[(kuukausi % 12) // 3]
    print("vuodenajat on:", vuodenaika)
else:

    print("Tarkista Kuukaudet uudelleen")
