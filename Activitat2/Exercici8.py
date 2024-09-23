cadena = str(input("Entra de 1 a 3 paraules separades amb un espai: "))
cadena = cadena.split(' ')
counter =0
try:
    for paraula in cadena:
        counter = counter+1

    if counter<1 or counter>3:
        print("Has posat menys de 1 o mes de 3 paraules")
    else:
        for word in cadena:
            print(len(word)," ",word[0]," ",word[len(word)-1])

except:
    print("No has entrat cap paraula")