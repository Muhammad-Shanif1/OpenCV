import cv2

# Load image
img = cv2.imread("C:/Users/Muhammad Shanif/Desktop/openCV/Imgs/circle1.png")
if img is None:
    print("Img failed to load")
else:
    print("Img successfully loaded")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)     # Tt returns list of corners of contour according to epsilon
        # arclength is the perimeter/length of the shape/curve.
        corners = len(approx)               # approx=[corner1,corner2,corner3,.......]
        if corners == 3:
            shape_name = "Triangle"
        elif corners == 4:
            # You could check if square or rectangle here by checking aspect ratio
            shape_name = "Rectangle"
        elif corners == 5:
            shape_name = "Pentagon"
        elif corners > 5:
            shape_name = "Circle"
        else:
            shape_name = "Unknown"

        cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)

        # Add label to the shape
        x = approx.ravel()[0]           # Gets the X position of the first corner of the shape
        y = approx.ravel()[1] - 10      # Gets the Y position and moves the label 10 pixels up
        cv2.putText(img, shape_name, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

    cv2.imshow("Contours", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()