Leiviska_Naula = 20
Naula_Luoti = 32
Luoti_Grammaa = 13.3

leiviskaet = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

kokonaisluodit = leiviskaet * Leiviska_Naula * Naula_Luoti + naulat * Naula_Luoti + luodit

grammat = kokonaisluodit * Luoti_Grammaa

kilogrammat = int(grammat // 1000)
jaannos_grammat = grammat % 1000

print(f"Massa nykymittojen mukaan: {kilogrammat} kilogrammaa ja {jaannos_grammat:.2f} grammaa.")