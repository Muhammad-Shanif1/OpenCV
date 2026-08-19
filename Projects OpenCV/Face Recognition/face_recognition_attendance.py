import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import csv

# ========== STEP 1: Load and encode known faces ==========
known_face_encodings = []
known_face_names = []

dataset_dir = 'Project/dataset'

for person_name in os.listdir(dataset_dir):
    person_folder = os.path.join(dataset_dir, person_name)
    
    if not os.path.isdir(person_folder):
        continue

    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)
        image = face_recognition.load_image_file(image_path)

        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:
            known_face_encodings.append(encodings[0])
            known_face_names.append(person_name)
        else:
            print(f"[WARNING] No face found in {image_path}")

print(f"[INFO] Loaded encodings for {len(known_face_names)} students.")


# ========== STEP 2: Initialize attendance file ==========
attendance_file = 'attendance.csv'
recorded_names = set()

if not os.path.exists(attendance_file):
    with open(attendance_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Time'])


def mark_attendance(name):
    if name not in recorded_names:
        now = datetime.now()
        time_string = now.strftime('%Y-%m-%d %H:%M:%S')

        with open(attendance_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, time_string])

        recorded_names.add(name)
        print(f"[INFO] Attendance marked for {name} at {time_string}")


# ========== STEP 3: Real-time face recognition ==========
cap = cv2.VideoCapture(0)

print("[INFO] Starting webcam. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces and get encodings
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        # Mark attendance
        if name != "Unknown":
            mark_attendance(name)

        # Scale face location back to original frame size
        top, right, bottom, left = [v * 4 for v in face_location]

        # Draw rectangle and name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 0, 0), 2)

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("[INFO] Attendance session ended.")
