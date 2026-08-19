import cv2

cap=cv2.VideoCapture(0)      # 0 if we want to use internal webcam  &  1 if we want to use external webcam

while True:
    ret,frame=cap.read()    # ret=True/False    frame=image
    if not ret:
        print("Could not read frame")
        break
    cv2.imshow("Webcam Feed",frame)
    if (cv2.waitKey(1) & 0xFF) ==ord('q'):
        print("Quitting....")
        break
cap.release()
cv2.destroyAllWindows()    


# waitkey(!):
    # This function waits for a key press for 1 millisecond.
    # If no key is pressed within 1 millisecond, it returns -1.
    # It returns a 32-bit integer representing the ASCII value of the key that was pressed.

# & 0xFF:
    # This is a bitwise AND operation with 0xFF (which is 255 in decimal or 11111111 in binary).
    # It is used to extract only the last 8 bits (lowest byte) from the key press.
    # Why? Because some platforms (especially Windows) may return more than just the ASCII value (extra bits), and we only care about the actual key code.

# ord('q')
    # The ord() function returns the ASCII value of a character.
    # ord('q') = 113