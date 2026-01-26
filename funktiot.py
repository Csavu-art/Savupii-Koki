#Funktio
#haluttu määrä
def tervehdi(kerrat):
    for i in range(kerrat):
        print("Hei, miten menee")
        print("tämä tervehdys tehdään")
        print("funktiossa")


# pääohjelma
print("pääohjelma alkaa")
tervehdi(1) #funktiokutsu
print("... pääohjelma jatkuu")
tervehdi(10)
print("pääohjelma loppuu")


#laskee suorakulmaisen kolmion alan kun annetaan kanta ja korkeus
def laske_kolmion_ala(kanta, korkeus):
    ala = (kanta * korkeus) / 2
    return ala

# Pääohjelma
ka = float(input("anna suorakulmaisen kolmion kanta:"))
ko = float(input("anna suorakulmaisen kolmion korkeus:"))

tulos = laske_kolmion_ala(ka, ko)
print(f"kolmion ala on {tulos}")

def tulosta(luku):
    luku += 1000
    print(f"parametrin arvo funktiossa: {luku}")

x = 10
tulosta(x)
print(f"pääohjrlman muuttujan arvo: {x}")

def tulosta(lista):
    for nimi in lista:
        print(nimi)
    lista.clear()

x = ["Pekka, Liisa. Xavier"]
tulosta(x)
print(f"pääohjelman muuttujan arvo: {x}")