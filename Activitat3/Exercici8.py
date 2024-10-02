numeroUsuari= input()
total=0
mitjana=0
numeroUsuari = list(numeroUsuari.split())

for i in range(len(numeroUsuari)):
    numeroUsuari[i] =int(numeroUsuari[i])
    total+=numeroUsuari[i]

mitjana=total/len(numeroUsuari)
print("Numeros de l'usuari ",numeroUsuari)
print("Total ",total)
print("Mitjana ",mitjana)
