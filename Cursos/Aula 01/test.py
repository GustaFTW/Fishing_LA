import cv2

image_path = "C:\\Users\\Gusta\\Documents\\CPQD\\biel.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()