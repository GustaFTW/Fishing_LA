import cv2
import numpy as np
# Load the image
image = cv2.imread("pics/bob.jpg")
if image is None:
    print("Couldn't load image")
    exit()

# Convert the image to hsv
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(image_hsv)
lower_yellow = np.array([15, 100, 100])
upper_yellow = np.array([45, 255, 255])

# Define the mask for the threshold
mask = cv2.inRange(image_hsv, lower_yellow, upper_yellow)

# Apply the mask using the and operation
yellow_regions = cv2.bitwise_and(image_hsv, image_hsv, mask=mask)

# Convert the image back into an rgb image
yellow_regions_rgb = cv2.cvtColor(yellow_regions, cv2.COLOR_HSV2BGR)

cv2.imshow("Original", image)
cv2.imshow("Yellow image", yellow_regions_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()




