class Ihminen:

    def __init__(self, nimi, ikä):
        self.nimi = nimi
        self.ikä = ikä

    def tervehdi(self):
        print(f"moi, olen {self.nimi}!")

    def tulosta_ikä(self):
        print(self.ikä)


class Suomalainen(Ihminen):

    def __init__(self, nimi, ikä, sisu):
        self.sisu = sisu
        super().__init__(nimi, ikä)

    def tervehdi(self):
        print(f"morjenst, mää olen {self.nimi}!")


pena = Ihminen("pekka", 53)
pena.tervehdi()
pena.tulosta_ikä()

kake = Suomalainen("Kake", 27, 100)
kake.tervehdi()
kake.tulosta_ikä()