from ultralytics import YOLO
import torch
import numpy as np
import os

if not os.path.exists("yolov8n.pt"):
    YOLO("yolov8n")
else:
    model = YOLO("yolov8n.pt")

def detect_objects(image):
    results = model(image)
    boxes = results[0].boxes
    detected_classes = boxes.cls.tolist()
    class_names = results[0].names
    labels = list({class_names[int(c)] for c in detected_classes})
    return labels