import cv2

# Open a image 

img=cv2.imread("C:/Users/Muhammad Shanif/Desktop/openCV/Imgs/tom.webp")

if img is None:
    print("Img failed to load")
else:
    print("Img successfully loaded")


# A Line
    # p1=(50,50)     # x,y
    # p2=(150,150)
    # color=(255,0,0)       # RGB
    # thickness=4
    # cv2.line(img,p1,p2,color,thickness)
    # cv2.imshow("Line on Image",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


# Rectangle
    p1=(50,50)          # p1 is top-left corner point
    p2=(200,160)        # p2 is bottom-right corner point
    color=(255,0,0)       # RGB
    thickness=4
    cv2.rectangle(img,p1,p2,color,thickness)
    cv2.imshow("Rectangle on Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Circle
    # center=(120,100)          
    # radius=70        
    # color=(255,0,0)       # RGB
    # thickness=4
    # cv2.circle(img,center,radius,color,thickness)
    # cv2.imshow("Circle on Image",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()    
    
    
# Text on Image    
    # point=(40,100)     # top-left point          
    # text="Hello Tom!"      
    # font=cv2.FONT_HERSHEY_SIMPLEX
    # font_size=1.2  
    # color=(255,0,0)       # RGB
    # thickness=2
    # cv2.putText(img,text,point,font,font_size,color,thickness)
    # cv2.imshow("Texr on Image",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()    