from random import random
numeroSecret = int(random() * 100+1)
nIntents = 20
numeroEntrada =0

def verificar_numero(n):
    if n>numeroSecret:
        print("El numero es massa gran")
    else:
        if n<numeroSecret :
            print("El numero es massa petit")
        else:
            print("Has guanyat")
            exit(0)

while numeroEntrada!=numeroSecret and nIntents>0:
    numeroEntrada = int(input("Entra un numero del 1 al 100: "))
    verificar_numero(numeroEntrada)
    nIntents-=1
    print("Et queden ",nIntents," intents")

