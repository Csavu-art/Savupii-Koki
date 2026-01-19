#tehtävä 3, kanta kertaa korkeus
kanta = float(input("Anna suorakulmion kolmion kanta:"))
korkeus = float(input("Anna suorakulmion korkeus:"))

#lasketaan pinta.ala
ala = (kanta * korkeus)

print(f"suorakulmion ala on {ala}")
piiri = (2 * kanta + 2 * korkeus)
print(f"suorakulmion piiri on {piiri}")