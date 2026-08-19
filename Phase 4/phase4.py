import cv2
import numpy as np
# Open a image 

img=cv2.imread("C:/Users/Muhammad Shanif/Desktop/openCV/Imgs/tom.webp")

if img is None:
    print("Img failed to load")
else:
    print("Img successfully loaded")

# Gaussian Blur
    # Replace center pixel by taking mean of all the nighbours pixels in kernal matrix.
    # kernalSize=(7,7)       # it always be a (odd,odd)
    # intensity_of_blurring=1 
    # blurred=cv2.GaussianBlur(img,kernalSize,intensity_of_blurring)
    # cv2.imshow("Orginal Image",img)
    # cv2.imshow("Blurred",blurred)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


# Median Blur       
    # Replace center pixel by taking median of all the nighbours pixels in kernal matrix.
    # kernalSize=11       # it always be a odd
    # blurred=cv2.medianBlur(img,kernalSize)
    # cv2.imshow("Orginal Image",img)
    # cv2.imshow("Blurred",blurred)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


# Sharpening    
    # Reverse of bluring. It shaprs the edges
    # it boost the center pixel by 5 times 
    # and down the color of the left,right,top,bottom pixels of the centered pixel by -1
    # and ingnores the borders pixels by 0 
    depth=-1        # -1 means : Use the same depth as the source image
    sharpen_kernal=np.array([
        [0,-1,0],
        [-1,5,-1],
        [0,-1,0]
    ]) 
    kernalSize=5       # it always be a odd
    blurred=cv2.medianBlur(img,kernalSize)
    sharped_img=cv2.filter2D(blurred,depth,sharpen_kernal)
    cv2.imshow("Blured Image",blurred)
    cv2.imshow("Sharped Image",sharped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


"""
In image processing, bit-depth (or "depth") refers to the type and range of values each pixel can hold. This affects:

How much detail you can store (more bits = more precision).

How much memory the image uses.

How filters and operations behave on that image.


Constant	    Meaning	Value           Range	        Used When You Need
CV_8U	    8-bit Unsigned Integer	    0 to 255	    Normal images (grayscale or color)
CV_16U	    16-bit Unsigned Integer	    0 to 65535	    High dynamic range (HDR) images

"""