import cv2
import numpy as np
import matplotlib.pyplot as plt

##matriz = [[0,1,0],[0,1,0],[0,0,1]]
imagen = cv2.imread('img2.png')
## Mostrar la resolución de la imagen
print(imagen.shape)

## Mostrar la imagen
plt.imshow(imagen)
plt.show()

## Convertir imagen a matriz
matriz = imagen.reshape((imagen.shape[0]*imagen.shape[1],imagen.shape[2]))
## Mostrar la matriz
print(matriz)

## Contar los pixeles blancos
con = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 1:
            con += 1
            print('El pixel en la posicion ', i, ',', j, ' es negro')

print('Hay ', con, 'pixeles')


