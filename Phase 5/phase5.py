import cv2
import numpy as np

img=cv2.imread("/home/muhammad-shanif/Downloads/border.jpeg",cv2.IMREAD_GRAYSCALE)        # grayscale img used for processing

if img is None:
    print("Img failed to load")
else:
    print("Img successfully loaded")


# Canny Edge Detection
    # upper threshold must be greater than lower threshold
    # threshold's value be in the renge 0-255
    # lower bound for detecting edges and upper bound for strong edges..
    """
    Pixels with edge strength:
    < 50 -→ definitely not an edge
    > 150 -→ definitely an edge
    50–150 -→ kept only if connected to strong edge (i.e., a pixel above threshold2)
    """
    edges=cv2.Canny(img,threshold1=50,threshold2=150)
    cv2.imshow("Edges",edges)    
    cv2.imshow("Orignal Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



# Thresholding
    """
    For each pixel in the grayscale image:
    If the pixel value is greater than 120, it will be set to maxval
    If the pixel value is less than or equal to 120, it will be set to 0.
    This creates a binary image, where pixels are either 0 (black) or 250 (white).
    """

    """
    90  -> 0   black
    50  -> 0   black
    """

    # ret,thresh_img=cv2.threshold(img,thresh=120,maxval=255,type=cv2.THRESH_BINARY)
    # cv2.imshow("Threshold",thresh_img)    
    # cv2.imshow("Orignal Image",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


# Bitwise Operations
    # img1=np.zeros((300,300),dtype="uint8")      # 300×300 pixel image.
    # img2=np.zeros((300,300),dtype='uint8')      # 8-bit unsigned integer (0 to 255), standard for grayscale images.
    # cv2.circle(img1,(150,150),100,255,-1)                   # thickness=-1     it fills the whole circle
    # cv2.rectangle(img2,(100,100),(250,250),255,-1)          # thickness=-1     it fills the whole rectangle
    # bitwise_and=cv2.bitwise_and(img1,img2)
    # bitwise_or=cv2.bitwise_or(img1,img2)
    # bitwise_not=cv2.bitwise_not(img1)
    # bitwise_xor=cv2.bitwise_xor(img1,img2)
    # cv2.imshow("Circle",img1)    
    # cv2.imshow("Rectangle",img2)    
    # cv2.imshow("AND",bitwise_and)    
    # cv2.imshow("OR",bitwise_or)
    # cv2.imshow("NOT",bitwise_not)
    # cv2.imshow("XOR",bitwise_xor)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()