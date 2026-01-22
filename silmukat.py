import random

lkm = int(input("Kuinka monta kertaa heitetään?"))

summa = 0

for i in range(lkm):

    noppa = random.randint(1, 6)

    summa += noppa

    print(summa)
    print(f"EV = {summa / lkm}")