import cv2

image = cv2.imread("pics/bolhas.png", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Erro ao abrir imagem")
    exit()

# Pega as dimensões da imagem
width, height = image.shape[1] - 1, image.shape[0] - 1
print(f"{width}x{height}")

# Cria uma cópia para comparar no final
image_original = image.copy()


# Para eliminar as bolhas na borda, é preciso percorrer as bordas
# Primeiro percorre-se a linha referente ao eixo X
for i in range(height):
    # Verifica se foi encontrado uma bolha
    if image[i, 0] == 255:
        
        # Define o seed invertendo as coordenadas
        p = (0, i)

        # Apaga a bolha
        cv2.floodFill(image, None, p, 0)

# Linha referente ao eixo Y
for i in range(width):
    # Verifica se foi encontrado uma bolha
    if image[0, i] == 255:
        
        # Define o seed invertendo as coordenadas
        p = (i, 0)

        # Apaga a bolha
        cv2.floodFill(image, None, p, 0)

# A linha de baixo
for i in range(width):
    # Verifica se foi encontrado uma bolha
    if image[height, i] == 255:
        
        # Define o seed invertendo as coordenadas
        p = (i, height)

        # Apaga a bolha
        cv2.floodFill(image, None, p, 0)

# A linha da direita
for i in range(height):
    # Verifica se foi encontrado uma bolha
    if image[i, width] == 255:
        
        # Define o seed invertendo as coordenadas
        p = (width, i)

        # Apaga a bolha
        cv2.floodFill(image, None, p, 0)

# Busca objetos presentes
nobjects = 0
for i in range(height):
    for j in range(width):
        if image[i, j] == 255:
            
            # Objeto encontrado
            nobjects += 1
            
            # Coordenadas invertidas para o floodfill
            p = (j, i)

            # Preenche objecto com o contador
            cv2.floodFill(image, None, p, nobjects)

# Preenche o fundo da imagem com pixel 255
cv2.floodFill(image, None, (0, 0), 255)

# Inicia um contador de bolha com buraco
bolha_buraco = 0

# Percorre novamente a imagem 
for i in range(height):
    for j in range(width):
        if image[i, j] == 0:
            # Incrementa o contador
            bolha_buraco += 1

            p = (j, i)
            # Apaga a bolha com buraco
            cv2.floodFill(image, None, p, 255)
            cv2.floodFill(image, None, (j - 1, i), 255)


print(f"A figura tem {nobjects} bolhas.")
print(f"E tem {bolha_buraco} bolhas com buraco.")
cv2.imshow("image", image)
cv2.imshow("imagem original", image_original)
cv2.imwrite("labelling.png", image)
cv2.waitKey(0)

