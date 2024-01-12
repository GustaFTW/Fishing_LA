import cv2

image = cv2.imread("pics/biel.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Erro ao abrir imagem")


# Pega as coordenadas ditas pelo usuario
p1 = tuple(map(int, input("Digite as coordenadas do ponto P1: ").split()))
p2 = tuple(map(int, input("Digite as coordenadas do ponto P2: ").split()))


# Copia a imagem
result = image.copy()
# Pega as coordenadas entre esses pontos usando slicing
roi = result[p1[0]:p2[0], p1[1]:p2[1]]
roi = cv2.bitwise_not(roi, roi)

cv2.imshow("Imagem original", image)
cv2.imshow("Imagem regiao invertida", result)
cv2.waitKey(0)
