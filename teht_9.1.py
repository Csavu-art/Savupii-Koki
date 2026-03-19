import random


class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def tulosta_tiedot(self):
        print(f"rekisterinumero: {self.rekisteritunnus}")
        print(f"huippunopeus   : {self.huippunopeus}")
        print(f"nopeus         : {self.nopeus}")
        print(f"matka          : {self.matka}")

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, aika):
        self.matka += self.nopeus * aika


# pääohjelma
fiat = Auto("ABC-123", 142)
fiat.kiihdytä(130)
fiat.kiihdytä(70)
fiat.kiihdytä(50)
fiat.tulosta_tiedot()

fiat.kiihdytä(-200)
fiat.tulosta_tiedot()

ferrari = Auto("ABC-321", 350)

(fiat.tulosta_tiedot())
(ferrari.tulosta_tiedot())

print()

fiat.nopeus = 60
fiat.matka = 2000
fiat.kulje(1.5)
fiat.tulosta_tiedot()

print()
print("autokilpailu alkaa")
print()

autot = []

for i in range(1, 11):
    auto = Auto("ABC-" + str(i), random.randint(100, 200))
    autot.append(auto)

kilpailu_jatkuu = True

while kilpailu_jatkuu:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)

        if auto.matka >= 10000:
            kilpailu_jatkuu = False

for auto in autot:
    auto.tulosta_tiedot()
    print()