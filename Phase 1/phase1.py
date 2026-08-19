import cv2

# Open a image 

img=cv2.imread("C:/Users/Muhammad Shanif/Desktop/openCV/Imgs/tom.webp")

if img is None:
    print("Img failed to load")
else:
    print("Img successfully loaded")

# Display a image 
    # cv2.imshow("Image Showing",img)
    # cv2.waitKey(0)                         # it waits untill user press key to close pic
    # cv2.destroyAllWindows


# Saving a image
    # success=cv2.imwrite("output.jpg",img)
    # if success:
    #     print("Pic save successfully")
    # else:
    #     print("Pic not saved")


# To show img info or dimensions/shape
    # height,width,channels=img.shape
    # print(f"Height: {height}  width: {width}  channels: {channels}")        # channel is 3 for colored images
    

# To convert colored image to grayscale(black white)
    # gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)       # grayscale img used for processing
    # cv2.imshow("Grayscale image",gray)    
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # cv2.imwrite("gray_tom.jpg",gray)


# Resizing Images
# Syntax:  cv2.resize(src,(width,height),fx,fy,interpolation)        fx,fy,interpolutation are optional
    # r_img=cv2.resize(img,(300,300))
    # cv2.imshow("Resized Image",r_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # cv2.imwrite("resized img.jpg",r_img)


# Cropping/Slicing
    
    # crop_img=img[50:50,50:50]          #[start_y : end_y , start_x : end_x]
    # cv2.imshow("Cropped",crop_img)
    # cv2.imshow("Orignal",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


# Image Rotation
    # (h,w)=img.shape[:2]
    # center=(w//2,h//2)
    # M=cv2.getRotationMatrix2D(center,90,1.0)        # (center,angle,scale)        -- scaling refers to resizing the image — either enlarging or shrinking it.
    # rotated=cv2.warpAffine(img,M,(w,h))             # applies an affine transformation (like rotation, scaling, translation) to the image.

    # cv2.imshow("Orignal Pic",img)
    # cv2.imshow("Rotated Pic",rotated)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # cv2.imwrite("rotated_img.jpg",rotated)


# Image Flipping
    # flipped_horizontal=cv2.flip(img,1)
    # flipped_vertical=cv2.flip(img,0)
    # flipped_both=cv2.flip(img,-1)
    # cv2.imshow("Orignal",img)
    # cv2.imshow("Flipped_horizontal",flipped_horizontal)
    # cv2.imshow("Flipped_vertical",flipped_vertical)
    # cv2.imshow("Flipped_both",flipped_both)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

        