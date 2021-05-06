#matplotlib
import matplotlib.pyplot as plt
#skimage
import skimage as io 
from skimage import color,data
from skimage.filters import threshold_otsu
from skimage.filters import gaussian
#numpy
import numpy as np
#PIL
from PIL import Image

#Funcion para ver dos imagenes
def plot_comparison(original, filtered, title):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8,6), sharex=True, sharey=True)
    ax1.imshow(original, cmap = plt.cm.gray)
    ax1.set_title("Original")
    ax1.axis("off")
    ax2.imshow(filtered, cmap = plt.cm.gray)
    ax2.set_title(title)
    ax2.axis("off")

#Extraer una mano
def extractHand(carpeta):
    #arreglo para la mano
    handy = [0,0,0,0,0]

    for x in range(0,5):
        #Leer imagen 
        matrixFinger = plt.imread("./Images/sub"+str(carpeta)+"/"+str(carpeta)+str(x+1)+".jpg")
        #Suavizar
        #gaussianFinger = gaussian(matrixFinger, multichannel= False)
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
    #transponemos la matriz U para sacar la columna
    transposeU = np.transpose(u)
    #devolver matriz U 
    return transposeU[0] 
    
#Base de datos
dataBase = []

#Extraer todas las manos y guardarlas en nuestro arreglo dataBase
for i in range(1,51):
    dataBase.append(extractHand(i))

#rint(dataBase[0])

handy = [0,0,0,0,0]

for x in range(0,5):
    #Leer imagen 
    matrixFinger = plt.imread("./Images/newFile/"+str(x+1)+".jpg")
    #Suavizar
    #gaussianFinger = gaussian(matrixFinger, multichannel= False)
    #Convertir a gris
    grayFinger = color.rgb2gray(matrixFinger)
    #Convertir matriz a arreglo
    fingerInVector = np.concatenate(grayFinger)
    fingerInList = fingerInVector.tolist()
    handy[x] = fingerInList
#Convertir la mano en una matriz
handyInMatrix = np.array(handy)
transposeHandy = np.transpose(handyInMatrix) 

#sacar los residuos 
residuos = []
for i in range(0,50):
    #usamos la funcion lstsq para obtener el residuo vectorial 
    x, residual,rank,singular = np.linalg.lstsq(transposeHandy,dataBase[i],-1)
    #pasamos los residuos en formato lista
    residualList = residual.tolist()
    #metemos los residuos en un array para buscar al sujeto 
    residuos.append(residualList)

#El sujeto sera aquel cuya posicion en el arreglo tenga el numero
sujeto = np.amin(residuos)
print(sujeto)

#Buscando al sujeto 
for i in range(0,50):
    if (sujeto == residuos[i]):
        print("La mano pertenece al sujeto "+str(i+1))
        break



#lstsq


