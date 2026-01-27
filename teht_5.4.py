kaupungit = ["Helsinki", "Tampere", "Vaasa", "Oulu", "Rovaniemi"]

for i in range(5):
    nimi = input("Anna kaupungin nimi: ")
    kaupungit.append(nimi)

print("Kaupungit ovat:")
for kaupunki in kaupungit:
    print(kaupunki)
