import cv2
import face_recognition
import pickle
#import RPi.GPIO as GPIO
import time

# Load trained encodings
with open("/Users/divyamsethi/Python/face_recognition/face_dataset/face_encodings.pickle", "rb") as f:
    encodings = pickle.load(f)

known_face_encodings = []
known_face_names = []

for name, face_encs in encodings.items():
    known_face_encodings.extend(face_encs)
    known_face_names.extend([name] * len(face_encs))

# GPIO setup
RELAY_PIN = 17
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(RELAY_PIN, GPIO.OUT)
#GPIO.output(RELAY_PIN, GPIO.HIGH)

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = known_face_names[match_index]
            print(f"Access Granted to {name}!")

            #GPIO.output(RELAY_PIN, GPIO.LOW)  # Unlock door
            time.sleep(5)
            #GPIO.output(RELAY_PIN, GPIO.HIGH)  # Lock door again
        else:
            print("Unauthorized Access!")

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
#GPIO.cleanup()
