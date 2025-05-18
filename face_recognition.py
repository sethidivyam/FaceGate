import cv2
import face_recognition
import pickle
import numpy as np
import time

# Load trained encodings
with open("/Users/divyamsethi/Python/face_recognition/face_dataset/face_encodings.pickle", "rb") as f:
    encodings = pickle.load(f)

known_face_encodings = []
known_face_names = []

for name, face_encs in encodings.items():
    known_face_encodings.extend(face_encs)
    known_face_names.extend([name] * len(face_encs))

video_capture = cv2.VideoCapture(0)

prev_x, prev_y = None, None
static_count = 0  # Counter for non-moving faces

while True:
    ret, frame = video_capture.read()
    if not ret:
        continue

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame, model="hog")
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(distances)

        if distances[best_match_index] < 0.6:  # Confidence threshold
            name = known_face_names[best_match_index]
            
            # Get face position
            x, y = left, top

            if prev_x is not None and prev_y is not None:
                if abs(x - prev_x) < 10 and abs(y - prev_y) < 10:  
                    static_count += 1  # Face not moving
                else:
                    static_count = 0  # Reset if face moves
            
            prev_x, prev_y = x, y

            if static_count >= 5:  # If face doesn't move for 5 frames
                print("Fake Face Detected! (Photo)")
            else:
                print(f"Access Granted to {name}!")
                time.sleep(5)  # Simulate door unlocking
        else:
            print("Unauthorized Access!")

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()



'''
import cv2
import face_recognition
import pickle
import time
import numpy as np

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
    if not ret:
        continue

    # ✅ Resize frame to 1/4th size for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # ✅ Use HOG model (faster on CPU)
    face_locations = face_recognition.face_locations(rgb_small_frame, model="hog")
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(distances)  # ✅ Faster than `matches.index(True)`
        
        if distances[best_match_index] < 0.6:  # ✅ Use a confidence threshold
            name = known_face_names[best_match_index]
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
'''