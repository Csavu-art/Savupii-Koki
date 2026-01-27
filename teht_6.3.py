def gallona_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    gallona = float(input("Anna bensiinimäärä gallonoina (negatiivinen lopettaa): "))

    if gallona < 0:
        break

    litrat = gallona_litroiksi(gallona)
    print("Määrä litroina:", litrat)
