import numpy as np

def exercici4():
    array4 = np.random.randint(80,size=(3,4))
    print("Array inicial 3x4 amb numeros aleatoris del 0 al 80")
    print(array4)
    array4 = array4.reshape(4,3)
    array4=np.append(array4,array4[-1,:],axis=1)
    print("Aquesta es la array de 4x3 on la ultima fila a passat a ser la ultima columna")
    print(array4)
    array4[:,-1] = array4[0,-1]
    print("Aquesta es la array de l'activitat final on els numeros de la ultima columna son tots els mateixos")
    print(array4)