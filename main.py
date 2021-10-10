#matplotlib
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import transpose
#skimage
from skimage import color
#numpy
import numpy as np


#Extraer el conjunto de muestras
def extractFingers(carpeta):
    #arreglo para el conjunto de muestras
    fingers = [0,0,0,0,0]

    for x in range(0,5):
        #Leer imagen 
        matrixFinger = plt.imread("./Images/sub"+str(carpeta)+"/"+str(carpeta)+str(x+1)+".jpg")
        #Convertir a gris
        grayFinger = color.rgb2gray(matrixFinger)
        #Convertir matriz a arreglo
        fingerInVector = np.concatenate(grayFinger)
        fingerInList = fingerInVector.tolist()
        fingers[x] = fingerInList
    #Convertir el conjunto de muestras en una matriz 
    fingerInMatrix = np.array(fingers)
    #transponemos la matriz del conjunto de muestras para que los dedos esten en las columnas
    transposeFingers = np.transpose(fingerInMatrix)
    #haciendo el SVD
    u,s,vh = np.linalg.svd(transposeFingers, full_matrices = False)
    #devolver matriz U 
    return u 
    
#Base de datos
dataBase = []

#Extraer todos los conjuntos de muestras y guardarlas en nuestro arreglo dataBase
for i in range(1,51):
    dataBase.append(extractFingers(i))

#Leer imagen 
matrixFinger = plt.imread("./Images/newFile/dedo.jpg")
#Convertir a gris
grayFinger = color.rgb2gray(matrixFinger)
#Convertir matriz a arregloss
fingerInVector = np.concatenate(grayFinger)
fingerInList = fingerInVector.tolist()
fingerInArray = [fingerInList]
fingerInArray = np.transpose(fingerInArray)

#sacar los residuos 
residuos = []
for i in dataBase:
    #usamos la funcion lstsq para obtener el residuo vectorial 
    x, residual,rank,singular = np.linalg.lstsq(i,fingerInArray,-1)
    #pasamos los residuos en formato lista
    residualList = residual.tolist()
    #metemos los residuos en un array para buscar al sujeto 
    residuos.append(residualList)

#El sujeto sera aquel cuya posicion en el arreglo tenga el numero minimo
sujeto = np.amin(residuos)

print(residuos)
if (sujeto > 100):
    print("El sujeto no se encuentra en la base de datos")
    exit()

print(sujeto)

#Buscando al sujeto 
for i in range(0,50):
    if (sujeto == residuos[i]):
        print("El dedo pertenece al sujeto "+str(i+1))
        break
