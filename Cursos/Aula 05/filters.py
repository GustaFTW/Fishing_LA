import cv2

# Load the image
image = cv2.imread("pics/bob.jpg")




# Apply the filter
gaussian = cv2.GaussianBlur(image, (5, 5), 0)
median = cv2.medianBlur(gaussian, 5)
horizontal = cv2.flip(image, 0)
vertical = cv2.flip(image, 1)
laplace = cv2.Laplacian(image, cv2.CV_64F, ksize=3)
laplace = cv2.convertScaleAbs(laplace)


# Display the image
cv2.imshow("Original", image)
cv2.imshow("Gaussian", gaussian)
cv2.imshow("Median", median)
cv2.imshow("Laplace", laplace)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Flipped H", horizontal)
cv2.imshow("Flipped V", vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()
