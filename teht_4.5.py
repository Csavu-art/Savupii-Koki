oikea_tunnus = "python"
oikea_salasana = "rules"

yritykset = 0
maksimi = 5

while yritykset < maksimi:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        print("Väärä tunnus tai salasana")
        yritykset += 1

if yritykset == maksimi:
    print("Pääsy evätty")
