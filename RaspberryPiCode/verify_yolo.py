
import sys
import os
import cv2
import numpy as np
# Add current directory to path so we can import modules
sys.path.append(os.getcwd())

from yolo_detection import YOLODetection

def main():
    # Use path relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # model is in parent directory of RaspberryPiCode
    model_path = os.path.join(script_dir, "..", "best 1.pt")
    # images are in TestingImages in parent directory
    image_path = os.path.join(script_dir, "..", "TestingImages", "2024-Ring", "frame0.png")

    if not os.path.exists(model_path):
        print(f"Error: Model not found at {model_path}")
        return
    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        return

    print(f"Testing YOLODetection...")
    print(f"Model: {model_path}")
    print(f"Image: {image_path}")

    try:
        detector = YOLODetection(model_path)
        frame = cv2.imread(image_path)
        if frame is None:
            print("Failed to load image via cv2.")
            return

        rect = detector.detect(frame)
        
        if rect is not None:
            print(f"Detection Successful! Bounding Box: {rect}")
            print(f"Format: [x, y, w, h]")
        else:
            print("No detection found (this might be expected if the image doesn't contain the object or model needs tuning).")
            print("But the code pipeline executed successfully.")

    except Exception as e:
        print(f"Exception occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
