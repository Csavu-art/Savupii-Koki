luvut = []

while True:
    syote = input("Anna luku (Enter lopettaa): ")

    if syote == "":
        break

    luvut.append(int(syote))

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
for i in range(min(5, len(luvut))):
    print(luvut[i])
