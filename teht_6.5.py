def poista_parittomat(lista):
    uusi_lista = []

    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)

    return uusi_lista


# Pääohjelma
luvut = [1, 2, 3, 4, 5, 6, 7, 8]

karsittu = poista_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Karsittu lista:", karsittu)
