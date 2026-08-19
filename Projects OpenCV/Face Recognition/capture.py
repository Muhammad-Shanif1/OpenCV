import cv2
import os

# Load Haar cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create dataset folder if it doesn't exist
dataset_path = 'Project/dataset'
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

# Input student name
name = input("Enter student's name: ")

# Create folder for student
student_folder = os.path.join(dataset_path, name)
if not os.path.exists(student_folder):
    os.makedirs(student_folder)

# Start webcam
cap = cv2.VideoCapture(0)
count = 0
max_images = 30  # Number of face images to capture

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f'Capturing {count}/{max_images}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))
        file_path = os.path.join(student_folder, f'{name}_{count}.jpg')
        cv2.imwrite(file_path, face)
        count += 1


    cv2.imshow("Collecting Face Data", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or count >= max_images:
        break

cap.release()
cv2.destroyAllWindows()

print(f"[INFO] {count} face images saved in {student_folder}")
