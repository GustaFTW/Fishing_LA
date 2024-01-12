import cv2
import numpy as np

# Ler a imagem
image = cv2.imread("pics/bob.jpg", cv2.IMREAD_COLOR)

if image is None:
    print("Erro ao carregar imagem")
    exit()

# Inicializa os parametros
planes = []
histR, histG, histB = None, None, None

# Niveis de cinza
nbins = 64

# Outros parametros
value_range = [0, 255]
hist_range = [value_range]
uniform = True
accumulate = False
key = 0

# Calcula as dimensões da imagem
height, width = image.shape[0], image.shape[1]

print("largura =", width)
print("altura =", height)

histw = nbins
histh = nbins // 2

histImgR = np.zeros((histh, histw, 3), dtype=np.uint8)
histImgG = np.zeros((histh, histw, 3), dtype=np.uint8)
histImgB = np.zeros((histh, histw, 3), dtype=np.uint8)

# Splita os canais de pixel da imagem
planes = cv2.split(image)

# Calcula o histograma de cada canal de pixel
histB = cv2.calcHist([planes[0]], [0], None, [nbins], hist_range, accumulate=accumulate)
histG = cv2.calcHist([planes[1]], [0], None, [nbins], hist_range, accumulate=accumulate)
histR = cv2.calcHist([planes[2]], [0], None, [nbins], hist_range, accumulate=accumulate)

cv2.normalize(histR, histR, 0, histImgR.shape[0], cv2.NORM_MINMAX)
cv2.normalize(histG, histG, 0, histImgG.shape[0], cv2.NORM_MINMAX)
cv2.normalize(histB, histB, 0, histImgB.shape[0], cv2.NORM_MINMAX)

histImgR.fill(0)
histImgG.fill(0)
histImgB.fill(0)

for i in range(nbins):
    cv2.line(histImgR, (i, histh), (i, histh - int(histR[i])), (0, 0, 255), 1, 8, 0)
    cv2.line(histImgG, (i, histh), (i, histh - int(histG[i])), (0, 255, 0), 1, 8, 0)
    cv2.line(histImgB, (i, histh), (i, histh - int(histB[i])), (255, 0, 0), 1, 8, 0)

histImgR.copyTo(image[0:histh, 0:nbins])
histImgG.copyTo(image[histh:2 * histh, 0:nbins])
histImgB.copyTo(image[2 * histh:3 * histh, 0:nbins])

cv2.imshow
