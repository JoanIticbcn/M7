numEntrada = int(input("Entra un numero del 1 al 100: "))

if numEntrada>100 or numEntrada<10:
    exit(-1)
tupla = tuple(range(0,numEntrada+1))
print(tupla)