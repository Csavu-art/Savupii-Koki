import random

# Kolmenumeroinen koodi (0..9)
kolmenumeroinen = "".join(str(random.randint(0, 9)) for _ in range(3))

# Nelinumeroinen koodi (1..6)
nelinumeroinen = "".join(str(random.randint(1, 6)) for _ in range(4))

# Tulostus
print("Kolmenumeroinen koodi (0..9):", kolmenumeroinen)
print("Nelinumeroinen koodi (1..6):", nelinumeroinen)