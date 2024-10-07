import numpy as np

def exercici4():
    array4 = np.random.randint(80,size=(3,4))
    array4 = array4.reshape(4,3)
    np.append(array4,array4[1,2],axis=0)
    return array4