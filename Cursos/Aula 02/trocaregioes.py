import cv2

image = cv2.imread("pics/biel.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Erro ao carregar imagem")

height, width = image[0].shape, image[1].shape

# Calcula o tamanho das regiões
size = round(int(height[0]) / 2)
# print(size)

# Cria uma cópia da imagem
result = image.copy()

# Separa as regiões start:stop:step
q1 = result[:size, :size].copy()
print(f"Shape primeiro quadrante: {q1.shape}")
q2 = result[size:, :size].copy()
print(f"Shape segundo quadrante: {q2.shape}")
q3 = result[:size, size:].copy()
print(f"Shape terceiro quadrante: {q3.shape}")
q4 = result[size:, size:].copy()
print(f"Shape quarto quadrante: {q4.shape}")

# Troca com a imagem original
image[:size, :size] = q4
image[size:, :size] = q3
image[:size, size:] = q2
image[size:, size:] = q1

cv2.namedWindow("Imagem resultante", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Imagem resultante", image)
cv2.waitKey(0)