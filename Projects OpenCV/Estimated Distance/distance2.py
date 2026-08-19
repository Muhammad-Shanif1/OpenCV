import cv2

# Constants
KNOWN_DISTANCE = 76.2  # centimeters (distance from camera to object during calibration)
KNOWN_WIDTH = 14.3     # centimeters (actual width of the face/object)

# Load the Haar cascade for face detection
face_detector = cv2.CascadeClassifier('C:/Users/Muhammad Shanif/Desktop/openCV/Haarcascades/opencv opencv master data-haarcascades/haarcascade_frontalface_default.xml')

# Colors for drawing
WHITE = (255, 255, 255)

def FocalLength(measured_distance, real_width, width_in_rf_image):     # foculLength is the distance b/w lens and the camera sensor
    """
    Calculate the focal length of the camera.
    """
    focal_length = (width_in_rf_image * measured_distance) / real_width
    return focal_length

def Distance_finder(Focal_Length, real_face_width, face_width_in_frame):
    """
    Estimate the distance from the camera to the object.
    """
    if face_width_in_frame == 0:
        return 0
    distance = (real_face_width * Focal_Length) / face_width_in_frame
    return distance

def face_data(image):
    """
    Detect the face in the image and return its width in pixels.
    """
    face_width = 0
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), WHITE, 2)
        face_width = w
        break  # Use first detected face
    return face_width

def main():
    # Step 1: Capture reference image and get face width in pixels
    # For calibration, you should take a photo at KNOWN_DISTANCE and find face_width_in_rf_image.
    # Here, we will grab frames from webcam and ask the user to press 'c' to calibrate.

    cap = cv2.VideoCapture(0)

    focal_length_found = False
    focal_length = 0
    print("Press 'c' to calibrate focal length when face is at known distance ({} cm).".format(KNOWN_DISTANCE))
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        face_width_in_frame = face_data(frame)     # used to retreive width in pixels
        
        if not focal_length_found:
            cv2.putText(frame, "Press 'c' to calibrate", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)
        else:
            distance = Distance_finder(focal_length, KNOWN_WIDTH, face_width_in_frame)
            if distance != 0:
                cv2.putText(frame, f"Distance: {distance:.2f} cm", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)
            else:
                cv2.putText(frame, "Face Not Detected", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)
        
        cv2.imshow("Distance Measurement", frame)
        
        key = cv2.waitKey(1) & 0xFF
        
        # Calibrate focal length when user presses 'c'
        if key == ord('c') and not focal_length_found:
            if face_width_in_frame != 0:
                focal_length = FocalLength(KNOWN_DISTANCE, KNOWN_WIDTH, face_width_in_frame)
                focal_length_found = True
                print(f"Focal Length calibrated: {focal_length}")
            else:
                print("Face not detected. Try again.")
        
        # Exit on pressing 'q'
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
