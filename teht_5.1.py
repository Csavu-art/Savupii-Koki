import random

n = int(input("Kuinka monta arpakuutiota heitetään? "))

summa = 0
for i in range(n):
    summa += random.randint(1, 6)

print("Silmälukujen summa on:", summa)
