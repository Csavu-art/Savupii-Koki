import random

N = int(input("Anna arvottavien pisteiden määrä: "))

n = 0  # ympyrän sisälle osuvien pisteiden määrä

i = 0
while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y < 1:
        n += 1

    i += 1

pi_arvio = 4 * n / N
print(f"Piin likiarvo on: {pi_arvio}")
