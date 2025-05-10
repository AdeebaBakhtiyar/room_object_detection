# detect.py

from ultralytics import YOLO
import cv2

# ✅ Load the YOLO model globally
model = YOLO("yolov8n.pt")  # or your custom model path

def detect_objects(image):
    # Ensure the image is in the correct format
    if image is None:
        return []

    # Run detection
    results = model(image)
    labels = []

    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            labels.append(label)

    return labels
