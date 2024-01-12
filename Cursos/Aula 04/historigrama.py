import cv2
import numpy as np


image = cv2.imread("pics/foto.png", cv2.IMREAD_COLOR)
width, height = 0, 0
# cap = cv2.VideoCapture(0)
planes = []
histR, histG, histB = None, None, None
nbins = 64
range = [0, 255]
histrange = [range]
uniform = True
accumulate = False
key = 0

# cap.open(0)

# if not cap.isOpened():
#     print("câmeras indisponíveis")
#     exit()

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
height, width = image.shape[0], image.shape[1]

print("largura =", width)
print("altura =", height)

histw = nbins
histh = nbins // 2
histImgR = np.zeros((histh, histw, 3), dtype=np.uint8)
histImgG = np.zeros((histh, histw, 3), dtype=np.uint8)
histImgB = np.zeros((histh, histw, 3), dtype=np.uint8)

planes = cv2.split(image)
histB = cv2.calcHist()

cv2.normalize(histR, histR, 0, histImgR, )

# while True:
#     _, image = cap.read()
#     planes = cv2.split(image)
#     histB = cv2.calcHist([planes[0]], [0], None, [nbins], range, accumulate=accumulate)
#     histG = cv2.calcHist([planes[1]], [0], None, [nbins], range, accumulate=accumulate)
#     histR = cv2.calcHist([planes[2]], [0], None, [nbins], range, accumulate=accumulate)

#     cv2.normalize(histR, histR, 0, histImgR.shape[0], cv2.NORM_MINMAX)
#     cv2.normalize(histG, histG, 0, histImgG.shape[0], cv2.NORM_MINMAX)
#     cv2.normalize(histB, histB, 0, histImgB.shape[0], cv2.NORM_MINMAX)

#     histImgR.fill(0)
#     histImgG.fill(0)
#     histImgB.fill(0)

#     for i in range(nbins):
#         cv2.line(histImgR, (i, histh), (i, histh - int(histR[i])), (0, 0, 255), 1, 8, 0)
#         cv2.line(histImgG, (i, histh), (i, histh - int(histG[i])), (0, 255, 0), 1, 8, 0)
#         cv2.line(histImgB, (i, histh), (i, histh - int(histB[i])), (255, 0, 0), 1, 8, 0)

#     histImgR.copyTo(image[0:histh, 0:nbins])
#     histImgG.copyTo(image[histh:2 * histh, 0:nbins])
#     histImgB.copyTo(image[2 * histh:3 * histh, 0:nbins])

#     cv2.imshow("image", image)
#     key = cv2.waitKey(30)
#     if key == 27:
#         break