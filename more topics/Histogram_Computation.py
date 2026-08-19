import cv2
import matplotlib.pyplot as plt

# Load image in grayscale
img = cv2.imread('Imgs/triangle.png', cv2.IMREAD_GRAYSCALE)

# Calculate histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Plot histogram
plt.plot(hist)
plt.title('Grayscale Histogram')
plt.xlabel('Pixel value')
plt.ylabel('Frequency')
plt.show()
