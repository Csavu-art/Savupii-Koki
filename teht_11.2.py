class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos

        if self.nopeus < 0:
            self.nopeus = 0

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tuntimaara):
        self.matka += self.nopeus * tuntimaara


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki


# pääohjelma
sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.nopeus = 120
polttomoottoriauto.nopeus = 100

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauton matkamittari: {sahkoauto.matka} km")
print(f"Polttomoottoriauton matkamittari: {polttomoottoriauto.matka} km")