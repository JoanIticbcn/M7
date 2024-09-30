frase = str(input("Entra una frase: "))
frase= frase.replace(" ","")
laTupla = (frase)
print(laTupla)
fraseSenseRepetits=""

for char in frase:
    if char not in fraseSenseRepetits:
        fraseSenseRepetits+=char

print(fraseSenseRepetits)