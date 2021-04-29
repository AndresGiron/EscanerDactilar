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

#Leer imagen 
matrixPhoto = plt.imread("./Images/sub2/21.jpg")
#Convertir a gris
grayPhoto = color.rgb2gray(matrixPhoto)
#Declarar tresh 
thresh = threshold_otsu(grayPhoto)
#Binary(TRUE/FALSE)
binary = grayPhoto > thresh
#Binary(0/255)


binary_255_0 = np.zeros((200,200))

def convertir_binario(binaryEN):
    for x in range(np.shape(binaryEN)[0]):
        for y in range(np.shape(binaryEN)[1]):
            if binaryEN[x][y]:
                binary_255_0[x][y] = 255
                print(binary_255_0[x][y])
            else:
                binary_255_0[x][y] = 0
                print(binary_255_0[x][y])
    return 0

convertir_binario(binary)

print(binary_255_0)

#Gaussian (Aplicar suavizado gaussiano a una imagen)
#gaussian_photo = gaussian(binary, multichannel=False)

#Funcion para mostrar la imagen 
def showImage(image,title = "Fingerprint", cmap_type = "gray"):
    plt.imshow(image, cmap = cmap_type)
    plt.title(title)
    plt.axis("off")
    plt.show()

#Funcion para ver dos imagenes
def plot_comparison(original, filtered, title):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8,6), sharex=True, sharey=True)
    ax1.imshow(original, cmap = plt.cm.gray)
    ax1.set_title("Original")
    ax1.axis("off")
    ax2.imshow(filtered, cmap = plt.cm.gray)
    ax2.set_title(title)
    ax2.axis("off")

#mostrando la imagen 
plot_comparison(matrixPhoto,binary_255_0,"Binary")
plt.show()
#mostrando la matriz
#print(binary)


