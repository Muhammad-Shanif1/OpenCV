import cv2
import numpy as np
img=cv2.imread("/home/muhammad-shanif/Downloads/border.jpeg") 

if img is None:
    print("Img failed to load")
else:
    print("Img successfully loaded")


# Contours
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # The underscore _ in Python is commonly used to ignore a value that you don’t plan to use.
    _,thresh=cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours=contours[1:]
    print("are=",cv2.contourArea(contour=contours[0]))
    print("len of contours=",len(contours))
    print("contour",contours[0])

     # Create a black image with same dimensions
    contour_img = np.zeros_like(img)
    cv2.drawContours(contour_img,contours,-1,(255,0,0),3)       # contourIndex=-1  means draw all contours
    cv2.imshow("Contours",contour_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
