import random

salainen = random.randint(1, 10)

arvaus = int(input("Arvaa luku väliltä 1–10: "))

while arvaus != salainen:
    if arvaus < salainen:
        print("Liian pieni arvaus")
    else:
        print("Liian suuri arvaus")

    arvaus = int(input("Arvaa uudelleen: "))

print("Oikein!")
