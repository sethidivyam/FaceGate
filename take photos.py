import cv2
import os

person_name = "Rachna"  # Change for different users
save_path = f"/Users/divyamsethi/Python/face_recognition/face_dataset/{person_name}"

if not os.path.exists(save_path):
    os.makedirs(save_path)

video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

count = 0
face_counts = 50 # Capture 40 images
while count < face_counts: 
    ret, frame = video_capture.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        face = frame[max(0, y):max(0, y+h), max(0, x):max(0, x+w)]  # Corrected cropping
        if face.shape[0] > 0 and face.shape[1] > 0:  # Check if face is valid
            count += 1
            cv2.imwrite(f"{save_path}/{count}.jpg", face)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Capturing Faces", frame)

    if cv2.waitKey(1) & 0xFF == ord("q") or count >= face_counts:
        break

video_capture.release()
cv2.destroyAllWindows()


'''
import cv2
import os

person_name = "Divyam"  # Change for different users
save_path = f"face_dataset/{person_name}"

if not os.path.exists(save_path):
    os.makedirs(save_path)

video_capture = cv2.VideoCapture(0)
count = 0

while count < 20:  # Capture 20 images
    ret, frame = video_capture.read()
    if not ret:
        break

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        count += 1
        cv2.imwrite(f"{save_path}/{count}.jpg", face)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Capturing Faces", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
'''