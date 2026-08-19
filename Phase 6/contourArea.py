import cv2
import numpy as np

# Create a black image
img = np.zeros((400, 400), dtype=np.uint8)

# Draw a white rectangle
cv2.rectangle(img, (50, 50), (300, 300), 255, -1)

# Find contours
contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Compute the area of the first contour
area = cv2.contourArea(contours[0])
# Since 1 cm = 37 px,
# then 1 cm² = 37 × 37 = 1369 px².
area_cm2 = area / 1369
print(f"Area in px: {area}")
print(f"Area in cm²: {area_cm2:.2f}")
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()