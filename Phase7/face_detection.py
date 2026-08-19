import cv2

face_cascade=cv2.CascadeClassifier("Haarcascades/opencv opencv master data-haarcascades/haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(image=gray,scaleFactor=1.1,minNeighbors=5)          # it returns list  of rectangles

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        # print(F"x={x}",F"y={y}",F"w={w}",F"h={h}")
    cv2.imshow("Webcam Face Detection",frame)
    if (cv2.waitKey(1) & 0xFF)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()