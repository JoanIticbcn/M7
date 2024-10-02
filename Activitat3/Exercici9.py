#Versio 1
"""
llistaDeNotes = []
assignatures = ['Catala','Castella','Mates','Fisica','Tecno','Biologia']
nota=0
for i in range(len(assignatures)):
    nota = int(input("Entra la nota de "+assignatures[i]+" "))
    llistaDeNotes.append(nota)
for j in range(len(assignatures)):
    print(assignatures[j]," has tret un ",llistaDeNotes[j])
"""
#Versio 2
llistaDeNotes = {}
assignatures = ['Catala','Castella','Mates','Fisica','Tecno','Biologia']
notaAux =0
for i in range(len(assignatures)):
    notaAux = int(input("Entra la nota de "+assignatures[i]+" "))
    llistaDeNotes[assignatures[i]] = notaAux

print(llistaDeNotes.items())