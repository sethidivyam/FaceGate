import os
import face_recognition
import pickle

dataset_path = "face_dataset"
encodings = {}

for person_name in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person_name)

    # ✅ Skip non-directory files like .DS_Store
    if not os.path.isdir(person_path):
        continue

    encodings[person_name] = []
    
    for image_name in os.listdir(person_path):
        image_path = os.path.join(person_path, image_name)

        try:
            # Load image and encode faces
            image = face_recognition.load_image_file(image_path)
            face_enc = face_recognition.face_encodings(image)

            if face_enc:  # ✅ Ensure a face is detected
                encodings[person_name].append(face_enc[0])

        except Exception as e:
            print(f"Error processing {image_name}: {e}")

# Save encodings
save_path = "/Users/divyamsethi/Python/face_recognition/face_dataset/face_encodings.pickle"
with open(save_path, "wb") as f:
    pickle.dump(encodings, f)

print("Training Completed. Encodings Saved!")
