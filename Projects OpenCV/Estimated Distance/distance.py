import cv2
import numpy as np

# ---- Constants ----
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 360

# Replace with your object’s real width (in inches or cm)
OBJECT_WIDTH_IN_REAL_UNITS = 3.75  
# Replace with your calibrated focal length (in pixels)
FOCAL_LENGTH = 728  

# ---- Functions ----
def get_distance(width_in_pixels):
    if width_in_pixels == 0:
        return float('inf')
    return (OBJECT_WIDTH_IN_REAL_UNITS * FOCAL_LENGTH) / width_in_pixels


def preprocess_frame(frame):
    """Convert frame to HSV and threshold for yellow color"""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Adjust these HSV ranges to match your yellow object
    lower_yellow = np.array([20, 100, 100])   # (H,S,V)
    upper_yellow = np.array([30, 255, 255])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    return mask


def find_largest_contour(contours):
    if not contours:
        return None
    largest = max(contours, key=cv2.contourArea)
    return largest


def process_frame(frame):
    mask = preprocess_frame(frame)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest = find_largest_contour(contours)
    if largest is not None:
        x, y, w, h = cv2.boundingRect(largest)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Distance calculation
        distance = get_distance(w)

        # Centroid
        M = cv2.moments(largest)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cX, cY), 5, (0, 255, 0), -1)
            cv2.putText(frame, f"({cX},{cY})", (cX + 10, cY), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Labels
        cv2.putText(frame, f"Width: {w} px", (x, y - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(frame, f"Distance: {distance:.2f} in", (x, y - 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    return frame


# ---- Main loop ----
cap = cv2.VideoCapture(0)  # use webcam index (0 or 1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = process_frame(frame)

    cv2.imshow("Yellow Object Detection", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
