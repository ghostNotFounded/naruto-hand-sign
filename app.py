import cv2
import numpy as np
from tensorflow.keras.models import load_model
import time

model = load_model('./models/best_VGG_Classifier.keras')

input_shape = (190, 320, 3)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

font = cv2.FONT_HERSHEY_SIMPLEX
prev_time = 0

map = {
    0: "bird",
    1: "boar",
    2: "dog",
    3: "dragon",
    4: "hare",
    5: "horse",
    6: "monkey",
    7: "ox",
    8: "ram",
    9: "rat",
    10: "snake",
    11: "tiger",
    12: "zero"
}

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    resized_frame = cv2.resize(frame, (input_shape[1], input_shape[0]))

    input_frame = resized_frame
    input_frame = np.expand_dims(input_frame, axis=0)

    predictions = model.predict(input_frame, verbose=False)
    predicted_label = np.argmax(predictions)
    
    predicted_name = map.get(predicted_label)

    fps_text = f"FPS: {int(fps)}"
    label_text = f"Prediction: {predicted_name}"

    cv2.putText(frame, fps_text, (10, 30), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    if predictions[0][predicted_label] > 0.9:
        cv2.putText(frame, label_text, (10, 70), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("Webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
