preu = int(input("Entra el preu en euros: "))
IVA = int(input("Entra el IVA % 4 10 21: "))

while IVA not in (4,10,21):
    print("Entra un valor correcte per a l'IVA només pot ser 4 10 o 21")
    IVA = int(input("Entra el IVA % 4 10 21: "))

preu_final = preu-(preu*IVA/100)
print(f"El preu final del producte un cop aplicat L'IVA es de {preu_final}€")