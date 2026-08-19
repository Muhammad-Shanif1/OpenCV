"""
Masking means selecting specific parts of an image by using another image (called a mask) 
that tells which pixels to keep and which to ignore.
"""


import cv2
import numpy as np

# Load image
image = cv2.imread("C:/Users/Muhammad Shanif/Desktop/openCV/Imgs/tom.webp")

# Create a black mask with same size as image
mask = np.zeros(image.shape[:2], dtype="uint8")     # gnoring the color channels.

# Draw a white circle on the mask
cv2.circle(mask, (150, 150), 100, 255, -1)  # center=(150,150), radius=100

# Apply mask using bitwise AND
masked_image = cv2.bitwise_and(image, image, mask=mask)

# Show result
cv2.imshow("Original", image)
cv2.imshow("Mask", mask)
cv2.imshow("Masked Image", masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
