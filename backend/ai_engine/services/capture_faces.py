import cv2
import os
import uuid

def capture_faces(admission_number, capture_limit=200):
    print(f"Starting image capture for {admission_number}...")

    haar_cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(haar_cascade_path)

    dataset_dir = 'ai_engine/data'
    train_dir = os.path.join(dataset_dir, 'train', admission_number)
    val_dir   = os.path.join(dataset_dir, 'val', admission_number)

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    video_capture = cv2.VideoCapture(0)
    captured_count = 0

    print("Press 'C' to capture image | 'Q' to quit")

    while captured_count < capture_limit:
        ret, frame = video_capture.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)

        cv2.imshow("Capture Faces", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('c') and len(faces) > 0:
            for (x, y, w, h) in faces:
                face = gray[y:y+h, x:x+w]
                face = cv2.resize(face, (150,150))
                filename = f"{uuid.uuid4().hex}.jpg"

                target = train_dir if captured_count < int(capture_limit * 0.8) else val_dir
                cv2.imwrite(os.path.join(target, filename), face)

                captured_count += 1
                print(f"Captured {captured_count}/{capture_limit}")

        elif key == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    print("Dataset collection completed.")
