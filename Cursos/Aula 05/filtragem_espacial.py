import cv2
import numpy as np

# Read an image
image = cv2.imread("pics/bob.jpg")

def printmask(m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            print(m[i, j], end=",")
        print()


media = np.array([0.1111, 0.1111, 0.1111, 0.1111, 0.1111,
                  0.1111, 0.1111, 0.1111, 0.1111], dtype=np.float32)
gauss = np.array([0.0625, 0.125, 0.0625, 0.125, 0.25,
                  0.125, 0.0625, 0.125, 0.0625], dtype=np.float32)
horizontal = np.array([-1, 0, 1, -2, 0, 2, -1, 0, 1], dtype=np.float32)
vertical = np.array([-1, -2, -1, 0, 0, 0, 1, 2, 1], dtype=np.float32)
laplacian = np.array([0, -1, 0, -1, 4, -1, 0, -1, 0], dtype=np.float32)
boost = np.array([0, -1, 0, -1, 5.2, -1, 0, -1, 0], dtype=np.float32)

frameFiltered = None
mask = np.zeros((3, 3), dtype=np.float32)
result = None
width, height = 0, 0
absolut = 0
key = ''


width = image.shape[0]
height = image.shape[1]
print("largura=", width)
print("altura =", height)

cv2.namedWindow("filtroespacial", cv2.WINDOW_NORMAL)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)

mask = np.array(media, dtype=np.float32).reshape(3, 3)

absolut = 1  # calcs abs of the image

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_gray = cv2.flip(image_gray, 1)
cv2.imshow("original", image_gray)
frame32f = image_gray.astype(np.float32)
frameFiltered = cv2.filter2D(frame32f, -1, mask, borderType=cv2.BORDER_CONSTANT)
if absolut:
    frameFiltered = cv2.absdiff(frameFiltered, 0)

result = frameFiltered.astype(np.uint8)

cv2.imshow("filtroespacial", result)
cv2.waitKey(0)
cv2.destroyAllWindows()