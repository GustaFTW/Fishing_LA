import cv2 
import numpy as np
import matplotlib.pyplot as plt

# Ler a imagem
image = cv2.imread("pics/bob.jpg", cv2.IMREAD_COLOR)

if image is None:
    print("Erro ao carregar imagem")
    exit()

# Define a quantidade de colunas do histograma
nbins = 64

# Outros parametros
value_range = [0, 255]
histrange = [value_range]
uniform = True
accumulate = False


# Calcula as dimensões da imagem
height, width = image.shape[0], image.shape[1]

print("largura =", width)
print("altura =", height)

##
histw = nbins
histh = nbins // 2

##
histImgR = np.zeros((histh, histw, 3), dtype=np.uint8)
histImgG = np.zeros((histh, histw, 3), dtype=np.uint8)
histImgB = np.zeros((histh, histw, 3), dtype=np.uint8)

# Splita os canais de pixel da imagem
planes = cv2.split(image)

# Calcula o histograma de cada canal de pixel
# na prática é mais comum transformar a imagem em HSV e calcular o histograma no canal V

histB = cv2.calcHist([planes[0]], [0], None, [nbins], value_range, accumulate=accumulate)
histG = cv2.calcHist([planes[1]], [0], None, [nbins], value_range, accumulate=accumulate)
histR = cv2.calcHist([planes[2]], [0], None, [nbins], value_range, accumulate=accumulate)


histB = cv2.normalize(histB, histB, 0, histImgB.shape[0], cv2.NORM_MINMAX)
histG = cv2.normalize(histG, histG, 0, histImgG.shape[0], cv2.NORM_MINMAX)
histR = cv2.normalize(histR, histR, 0, histImgR.shape[0], cv2.NORM_MINMAX)


# Desenha o gráfico do histograma
for i in range(nbins):
    cv2.line(histImgR, (i, histh), (i, histh - int(histR[i])), (0, 0, 255), 1, 8, 0)
    cv2.line(histImgG, (i, histh), (i, histh - int(histG[i])), (0, 255, 0), 1, 8, 0)
    cv2.line(histImgB, (i, histh), (i, histh - int(histB[i])), (255, 0, 0), 1, 8, 0)

# Coloca o desenho do histograma na imagem
image[0:histh, 0:nbins] = histImgR
image[histh:2 * histh, 0:nbins] = histImgG
image[2 * histh:3 * histh, 0:nbins] = histImgB


# Mostra a imagem
cv2.imshow("image", image)
cv2.waitKey(0)
