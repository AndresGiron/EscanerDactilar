#matplotlib
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import transpose
#skimage
from skimage import color,data
#numpy
import numpy as np
#PIL
from PIL import Image

#Extraer una mano
def extractHand(carpeta):
    #arreglo para la mano
    handy = [0,0,0,0,0]

    for x in range(0,5):
        #Leer imagen 
        matrixFinger = plt.imread("./Images/sub"+str(carpeta)+"/"+str(carpeta)+str(x+1)+".jpg")
        #Convertir a gris
        grayFinger = color.rgb2gray(matrixFinger)
        #Convertir matriz a arreglo
        fingerInVector = np.concatenate(grayFinger)
        fingerInList = fingerInVector.tolist()
        handy[x] = fingerInList
    #Convertir la mano en una matriz
    handyInMatrix = np.array(handy)
    #transponemos la matriz de la mano para que los dedos esten en las columnas
    transposeHandy = np.transpose(handyInMatrix)
    #haciendo el SVD
    u,s,vh = np.linalg.svd(transposeHandy, full_matrices = False)
    #devolver matriz U 
    return u 
    
#Base de datos
dataBase = []

#Extraer todas las manos y guardarlas en nuestro arreglo dataBase
for i in range(1,51):
    dataBase.append(extractHand(i))

#Leer imagen 
matrixFinger = plt.imread("./Images/newFile/dedo.jpg")
#Convertir a gris
grayFinger = color.rgb2gray(matrixFinger)
#Convertir matriz a arregloss
fingerInVector = np.concatenate(grayFinger)
fingerInList = fingerInVector.tolist()
fingerInArray = [fingerInList]
fingerInArray = np.transpose(fingerInArray)


print(np.shape(fingerInArray))
print(np.shape(dataBase[0]))

#sacar los residuos 
residuos = []
for i in dataBase:
    #usamos la funcion lstsq para obtener el residuo vectorial 
    x, residual,rank,singular = np.linalg.lstsq(i,fingerInArray,-1)
    #pasamos los residuos en formato lista
    residualList = residual.tolist()
    #metemos los residuos en un array para buscar al sujeto 
    residuos.append(residualList)

#El sujeto sera aquel cuya posicion en el arreglo tenga el numero
sujeto = np.amin(residuos)

print(residuos)
if (sujeto > 0.0000000000000000001):
    print("El sujeto no se encuentra en la base de datos")
    exit()

print(sujeto)

#Buscando al sujeto 
for i in range(0,50):
    if (sujeto == residuos[i]):
        print("La mano pertenece al sujeto "+str(i+1))
        break