import cv2

# Load pre-trained DNN model from OpenCV
net = cv2.dnn.readNetFromCaffe(cv2.data.haarcascades + "deploy.prototxt",
                               cv2.data.haarcascades + "res10_300x300_ssd_iter_140000.caffemodel")

# Initialize webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    
    # Convert frame to a blob for DNN processing
    blob = cv2.dnn.blobFromImage(frame, scalefactor=1.0, size=(300, 300), mean=(104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    # Process detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Confidence threshold
            box = detections[0, 0, i, 3:7] * [w, h, w, h]
            (x, y, x1, y1) = box.astype("int")
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("Face Detection", frame)

    # Exit on 'ESC' key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
