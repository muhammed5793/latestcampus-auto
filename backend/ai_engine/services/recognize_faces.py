import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from attendance.services import mark_attendance


MODEL_PATH = "ai_engine/model.h5"
TRAIN_DIR = "ai_engine/data/train"
CONFIDENCE_THRESHOLD = 0.6


def get_class_labels():
    return sorted(os.listdir(TRAIN_DIR))


def recognize_and_mark():
    if not os.path.exists(MODEL_PATH):
        print("❌ model.h5 not found. Train first.")
        return

    model = load_model(MODEL_PATH)
    class_labels = get_class_labels()

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (150, 150))
            face = np.stack([face]*3, axis=-1) / 255.0
            face = face.reshape(1, 150, 150, 3)

            preds = model.predict(face, verbose=0)
            idx = preds.argmax()
            confidence = preds.max()

            if confidence < CONFIDENCE_THRESHOLD:
                label = "Stranger"
            else:
                admission_number = class_labels[idx]
                label = f"{admission_number} ({confidence*100:.2f}%)"

                # 🔥 AUTO ATTENDANCE
                mark_attendance(admission_number, confidence)

            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(
                frame, label, (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2
            )

        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
