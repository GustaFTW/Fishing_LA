import cv2
import numpy as np

# Load image
image = cv2.imread("pics/bob.jpg")
if image is None:
    print("Can't load the image")
    exit()
# Convert to hsv
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

# Create a CLAHE object
clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8, 8))

# Apply it to the V (value)
v_eq_clahe = clahe.apply(v)

# Merge the v value back into the image
hsv_eq_clahe = cv2.merge((h, s, v_eq_clahe))

# Convert the equalized HSV image back to original color
result_clahe = cv2.cvtColor(hsv_eq_clahe, cv2.COLOR_HSV2BGR)

# Making a normal hist equalization
v_eq = cv2.equalizeHist(v)

# Merge the image back
hsv_eq = cv2.merge((h, s, v_eq))

# Turn the image back into rgb
result_eq = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)


cv2.imshow("Original", image)
cv2.imshow("Clahe", result_clahe)
cv2.imshow("HSV Eq", result_eq)
cv2.waitKey(0)
