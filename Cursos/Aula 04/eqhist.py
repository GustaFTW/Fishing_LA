import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGE_PATH = "pics/bob.jpg"

# Le a imagem em grayscale e em cores
image_gs = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
image_color = cv2.imread(IMAGE_PATH)

# ----------- Para a imagem em gs
# Aplica equalização do histograma 
imagem_equalizada_gs = cv2.equalizeHist(image_gs)

# Calcula o histograma da imagem em gs
histGS = cv2.calcHist([image_gs], [0], None, [256], [0, 256])

# Plota o gráfico do histograma
plt.figure()
plt.plot(histGS, color="black")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.title("Histogram Grayscale")
plt.xlim([0, 256])


# Mostra as imagens e a equalização em grayscale
cv2.imshow("Imagem equalizada", imagem_equalizada_gs)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.close("all")

# ------------ Agora para a imagem colorida
# Splita a imagem nos color channels
b_channel, g_channel, r_channel = cv2.split(image_color)

# Calcula o histograma da imagem
histB = cv2.calcHist([b_channel], [0], None, [256], [0, 255])
histG = cv2.calcHist([g_channel], [0], None, [256], [0, 255])
histR = cv2.calcHist([g_channel], [0], None, [256], [0, 255])

# Aplica equalização em cada um dos canais de cor
equalized_b_channel = cv2.equalizeHist(b_channel)
equalized_g_channel = cv2.equalizeHist(g_channel)
equalized_r_channel = cv2.equalizeHist(r_channel)


# Mescla os canais de volta na imagem rgb
imagem_equalizada_color = cv2.merge([equalized_b_channel, equalized_g_channel, equalized_r_channel])

# Plota o histograma
plt.figure()
plt.plot(histR, color="red", label="Red")
plt.plot(histG, color="green", label="Green")
plt.plot(histB, color="blue", label="Blue")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.title("RGB Histogram")
plt.xlim([0, 256])
plt.legend()



# Mostra as imagens e a equalização nos 3 canais de cores
cv2.imshow("Imagem original", image_color)
cv2.imshow("Imagem equalizada", imagem_equalizada_color)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
