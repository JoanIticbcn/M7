import numpy as np

def exercic1():
    array1 = np.array(range(50))
    array2 = np.diag(array1)
    np.savetxt('exercici1.npy', array2)
    return array2