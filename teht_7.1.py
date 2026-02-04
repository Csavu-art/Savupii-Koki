kuukausi = int(input("Anna kuukauden numero (1-12): "))

vuodenajat = ("talvi", "kevät", "kesä", "syksy")

indeksi = (kuukausi % 12) // 3

print("Vuodenaika on:", vuodenajat[indeksi])
