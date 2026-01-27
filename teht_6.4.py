def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa


# Pääohjelma
luvut = [3, 7, 2, 5, 10]

tulos = laske_summa(luvut)
print("Listan lukujen summa on:", tulos)
