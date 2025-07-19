from ultralytics import YOLO
import cv2
import os
import time

# Load YOLO model
model = YOLO('yolov8n.pt')

# Input from real camera
cap = cv2.VideoCapture('/dev/video0')
width, height = 640, 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Create the output directory/file if it doesn't exist
output_path = "/tmp/stream.jpg"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

print("Starting YOLO stream output to MJPG-streamer at:", output_path)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("❌ Failed to grab frame from camera.")
        break

    # YOLO inference and annotation
    results = model(frame, imgsz=640)
    annotated_frame = results[0].plot()

    # Resize to match MJPG expectations
    annotated_frame = cv2.resize(annotated_frame, (width, height))

    # Save annotated frame as JPEG
    cv2.imwrite(output_path, annotated_frame)

    # Small sleep to avoid excessive writes
    time.sleep(0.05)

cap.release()
cv2.destroyAllWindows()
