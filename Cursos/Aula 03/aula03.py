import cv2


image = cv2.imread("pics/bolhas.png", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("imagem nao carregou corretamente")

width = image.shape[1]
height = image.shape[0]
print(f"{width}x{height}")

p = (0, 0)

# busca objetos presentes
nobjects = 0
for i in range(height):
    for j in range(width):
        if image[i, j] == 255:
            # achou um objeto
            nobjects += 1
            # para o floodfill as coordenadas
            # x e y são trocadas.
            p = (j, i)
            # preenche o objeto com o contador
            cv2.floodFill(image, None, p, nobjects)

print(f"a figura tem {nobjects} bolhas")
cv2.imshow("image", image)
cv2.imwrite("labeling.png", image)
cv2.waitKey(0)
