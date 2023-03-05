import os
import cv2
import numpy as np

# Set the maximum allowed image dimensions
max_width = 800
max_height = 600

# Get the list of image file names in the data folder
data_folder = 'data'
image_files = [f for f in os.listdir(data_folder) if os.path.isfile(os.path.join(data_folder, f))]

# Loop through the image files
for image_file in image_files:
    # Load the image
    img = cv2.imread(os.path.join(data_folder, image_file))

    # Resize the image if necessary
    height, width, channels = img.shape
    aspect_ratio = width / float(height)
    if width > max_width or height > max_height:
        if aspect_ratio > 1:
            new_width = max_width
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = max_height
            new_width = int(new_height * aspect_ratio)
        img = cv2.resize(img, (new_width, new_height))

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply edge detection using the Canny algorithm
    edges = cv2.Canny(gray, 100, 200)

    # Apply a Gaussian blur to the image to reduce noise
    blurred = cv2.GaussianBlur(edges, (5, 5), 0)

    # Apply thresholding to the image to isolate the number plate
    _, thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)

    # Find contours in the image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Sort the contours by area in descending order
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Loop through the contours and find the number plate
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        if len(approx) == 4:
            number_plate = approx
            break

    # Draw a bounding box around the number plate
    cv2.drawContours(img, [number_plate], -1, (0, 255, 0), 3)

    # Display the final image
    cv2.imshow('Number Plate Recognition', img)
    cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
