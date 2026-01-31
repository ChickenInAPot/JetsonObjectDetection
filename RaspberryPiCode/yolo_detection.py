import cv2
import numpy as np
from ultralytics import YOLO

class YOLODetection:
    """
    A class used to detect game pieces in the image using a YOLO model.

    Attributes
    ----------
    model : YOLO
        The loaded YOLO model.

    Methods
    -------
    detect(frame: cv2.Mat) -> np.ndarray
        Detects game pieces in the given frame using the YOLO model.
    """

    def __init__(self, model_path: str):
        """
        Initialize the YOLODetection class.

        Parameters
        ----------
        model_path : str
            The path to the YOLO model file (.pt).
        """
        print(f"Loading YOLO model from {model_path}...")
        self.model = YOLO(model_path)
        print("YOLO model loaded successfully.")

    def detect(self, frame: cv2.Mat) -> np.ndarray:
        """
        Detects game pieces in the given frame using the YOLO model.
        Returns the bounding box of the detection with the highest confidence.

        Parameters
        ----------
        frame : cv2.Mat
            The frame to detect game pieces in.

        Returns
        -------
        np.ndarray or None
            The bounding box [x, y, w, h] of the best detection, or None if no detection.
        """
        # Run inference
        results = self.model(frame, verbose=False)

        best_box = None
        highest_conf = -1.0

        for result in results:
            boxes = result.boxes
            for box in boxes:
                conf = float(box.conf[0])
                if conf > highest_conf:
                    highest_conf = conf
                    # YOLO returns [x1, y1, x2, y2]
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                    w = x2 - x1
                    h = y2 - y1
                    best_box = np.array([x1, y1, w, h], dtype=np.int32)

        return best_box
