num = int(input("Entra un numero: "))

def sumarecursiva(n):
    if n==0:
        return 0
    return n+(sumarecursiva(n-1))

print(sumarecursiva(num))