class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi}")
        print(f"Kirjoittaja   : {self.kirjoittaja}")
        print(f"Sivumäärä     : {self.sivumaara}")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi : {self.nimi}")
        print(f"Päätoimittaja  : {self.paatoimittaja}")


# pääohjelma
aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti = Kirja("Hytti nro 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
print()
hytti.tulosta_tiedot()