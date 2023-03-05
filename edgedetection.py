import cv2

# Load the image
img = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to reduce noise
img = cv2.GaussianBlur(img, (3,3), 0)

# Perform Canny edge detection
edges = cv2.Canny(img, 50, 150)

# Display the original image and the edges
cv2.imshow('Original image', img)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()