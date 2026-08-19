import cv2
import mediapipe as mp
import os
import json

# Constants
KNOWN_DISTANCE = 76.2  # centimeters
KNOWN_WIDTH = 14.3     # Average adult face width in cm (adjust for your use case)
FOCAL_LENGTH_FILE = "focal_length.json"

# Initialize Mediapipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Colors
WHITE = (255, 255, 255)

def save_focal_length(focal_length):
    with open(FOCAL_LENGTH_FILE, "w") as f:
        json.dump({"focal_length": focal_length}, f)

def load_focal_length():
    if os.path.exists(FOCAL_LENGTH_FILE):
        with open(FOCAL_LENGTH_FILE, "r") as f:
            data = json.load(f)
            return data.get("focal_length", 0)
    return 0

def FocalLength(measured_distance, real_width, width_in_rf_image):
    return (width_in_rf_image * measured_distance) / real_width

def DistanceFinder(focal_length, real_face_width, face_width_in_frame):
    if face_width_in_frame == 0:
        return 0
    return (real_face_width * focal_length) / face_width_in_frame

def main():
    cap = cv2.VideoCapture(0)
    focal_length = load_focal_length()
    focal_length_found = focal_length > 0

    print("Press 'c' to calibrate when a face is at known distance ({} cm).".format(KNOWN_DISTANCE))
    print("Press 'q' to quit.")

    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.7) as face_detection:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            h, w, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_detection.process(rgb_frame)

            if results.detections:
                for detection in results.detections:
                    bboxC = detection.location_data.relative_bounding_box
                    x = int(bboxC.xmin * w)
                    y = int(bboxC.ymin * h)
                    width = int(bboxC.width * w)
                    height = int(bboxC.height * h)

                    cv2.rectangle(frame, (x, y), (x + width, y + height), WHITE, 2)

                    if focal_length_found:
                        distance = DistanceFinder(focal_length, KNOWN_WIDTH, width)
                        cv2.putText(frame, f"{distance:.2f} cm", (x, y - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, WHITE, 2)
                    else:
                        cv2.putText(frame, "Press 'c' to calibrate", (30, 50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)

            else:
                cv2.putText(frame, "No face detected", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)

            cv2.imshow("Distance Estimation", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord('c') and results.detections:
                detection = results.detections[0]
                bboxC = detection.location_data.relative_bounding_box
                face_width_pixels = int(bboxC.width * w)
                focal_length = FocalLength(KNOWN_DISTANCE, KNOWN_WIDTH, face_width_pixels)
                focal_length_found = True
                save_focal_length(focal_length)
                print(f"[INFO] Calibrated focal length: {focal_length:.2f}")

            if key == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
