# 🚪 FaceGate – Intelligent Face Recognition Access System

**FaceGate** is a Python-based security system that detects, recognizes, and verifies individuals using face recognition.  
It includes **anti-photo spoofing** by detecting static faces over multiple frames, helping prevent unauthorized access using photos.

---

## 📌 Project Summary

FaceGate was developed to enhance access control security by combining facial recognition with liveness detection.  
It can be integrated into smart locks, attendance systems, or any access control application, ensuring only real, moving faces are granted access.

---

## 💡 Problem Statement

Traditional face recognition systems are vulnerable to spoofing attacks using printed photos or digital screens.  
The goal was to create a system that recognizes known faces **and** ensures the detected face is alive and moving, rejecting static imposters.

---

## 🔧 Features

- 🧠 **Face Recognition** – Identify individuals from a trained dataset
- 🛡 **Anti-Photo Spoofing** – Detects static faces over multiple frames
- 📷 **Real-Time Detection** – Uses webcam for live recognition
- 📂 **Dataset Support** – Train on multiple images per person
- ⏳ **Access Control Simulation** – Unlock delay for authorized faces
- ❌ **Unauthorized Detection** – Reject unknown faces immediately

---

## 🧰 Tech Stack

- **Python 3.x**
- **OpenCV** – Real-time video processing
- **face_recognition** – Face detection & encoding
- **NumPy** – Numerical operations
- **Pickle** – Model storage

---

## 🚀 How It Works

1. **Collect Images** – Use `take_photos.py` to capture face images per user
2. **Train Model** – Run `train_model.py` to encode and save facial data
3. **Run Recognition** – Use `face_recognition.py` to detect and grant access
4. **Anti-Spoofing** – If a face is static for multiple frames, it’s flagged as fake

---

## 🗂️ Project Structure

FaceGate/
├── dataset/ # Captured images
├── face_encodings.pickle # Trained face encodings
├── take_photos.py # Capture face images
├── train_model.py # Train encodings from dataset
├── face_recognition.py # Main recognition + anti-spoofing
├── requirements.txt # Dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 📥 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/FaceGate.git
   cd FaceGate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Collect dataset:

bash
Copy
Edit
python take_photos.py
Train model:

bash
Copy
Edit
python train_model.py
Run recognition:

bash
Copy
Edit
python face_recognition.py
📊 Output
Authorized Access – Displays name and simulates unlocking

Fake Face Detected – Flags static, unmoving faces

Unauthorized Access – Rejects unknown faces

✅ To-Do / Future Improvements
Add deepfake detection

Improve liveness detection with blink/mouth movement

Integrate with IoT door lock

Add GUI interface

📄 License
This project is licensed under the MIT License – free to use, modify, and distribute with attribution.

👨‍💻 Author
Divyam Sethi
🔗 GitHub
📧 Email

⭐️ Support
If you like FaceGate, please ⭐ the repo and share it with others!
