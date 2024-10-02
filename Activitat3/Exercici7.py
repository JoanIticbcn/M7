contactes = {"Joan":14}
nom = str(input("Entra el nom del contacte "))
edat = int(input("Entra l'edat del contacte "))
while nom !='':
    if contactes.__contains__(nom):
        print("El nom introduit ja existeix a la llista de usuaris")
    else:
        contactes[nom] = edat
    nom = str(input("Entra el nom: del contacte "))
    if nom=='' :
        break
    edat = int(input("Entra l'edat del contacte "))
print(contactes)