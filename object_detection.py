import cv2
import numpy as np

class ObjectDetection:
    def __init__(self, weights_path="C:\\Users\\DELL\\OneDrive\\Desktop\\Project\\dnn_model\\yolov4.weights", cfg_path="C:\\Users\\DELL\\OneDrive\\Desktop\\Project\\dnn_model\\yolov4.cfg"):
        # Display initialization messages
        print("Loading Object Detection")
        print("Running OpenCV DNN with YOLOv4")

        # Set non-maximum suppression threshold
        self.nmsThreshold = 0.4
        # Set confidence threshold for object detection
        self.confThreshold = 0.5
        # Set image size for consistency
        self.image_size = 608

        # Load YOLOv4 network
        net = cv2.dnn.readNet(weights_path, cfg_path)

        # Enable GPU CUDA for faster inference
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        self.model = cv2.dnn_DetectionModel(net)

        # Initialize empty lists for classes and colors
        self.classes = []
        self.load_class_names()
        self.colors = np.random.uniform(0, 255, size=(80, 3))

        # Set input parameters for the model
        self.model.setInputParams(size=(self.image_size, self.image_size), scale=1/255)

    def load_class_names(self, classes_path="C:\\Users\\DELL\\OneDrive\\Desktop\\Project\\dnn_model\\classes.txt"):
        """
        Load class names from a file and store them in the 'classes' attribute.

        Args:
            classes_path (str): Path to the file containing class names.

        Returns:
            list: List of loaded class names.
        """
        with open(classes_path, "r") as file_object:
            for class_name in file_object.readlines():
                class_name = class_name.strip()
                self.classes.append(class_name)

        # Generate random colors for each class
        self.colors = np.random.uniform(0, 255, size=(80, 3))
        return self.classes

    def detect(self, frame):
        """
        Perform object detection on a given frame.

        Args:
            frame (numpy.ndarray): Input image frame for object detection.

        Returns:
            tuple: A tuple containing class IDs, confidence scores, and bounding boxes for detected objects.
        """
        return self.model.detect(frame, nmsThreshold=self.nmsThreshold, confThreshold=self.confThreshold)