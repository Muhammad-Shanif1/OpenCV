import cv2

face_cascade=cv2.CascadeClassifier("Haarcascades/opencv opencv master data-haarcascades/haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("Haarcascades/opencv opencv master data-haarcascades/haarcascade_eye.xml")
smile_cascade=cv2.CascadeClassifier("Haarcascades/opencv opencv master data-haarcascades/haarcascade_smile.xml")


cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(image=gray,scaleFactor=1.1,minNeighbors=5)          # it returns list  of rectangles
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        region_gray=gray[y:y+h,x:x+w]    

        eyes=eye_cascade.detectMultiScale(region_gray,1.1,10)
        if len(eyes)>0:
            cv2.putText(frame,"Eyes Detected",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 255, 0),2)
        
        smile=smile_cascade.detectMultiScale(region_gray,1.7,30)
        if len(smile)>0:
            cv2.putText(frame,"Smiling",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 255, 0),2)
    
    
    cv2.imshow("Webcam Face Detection",frame)
    if (cv2.waitKey(1) & 0xFF)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()