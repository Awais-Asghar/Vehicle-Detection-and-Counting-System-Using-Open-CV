# Vehicle Detection Using Open CV
 Vehicle detection with OpenCV is a computer vision process involving the acquisition of images or video frames, followed by pre-processing for noise reduction through resizing and filtering. Object detection models like SSD or YOLO are employed to identify potential vehicle regions in the input. Relevant features are then extracted from these regions, and classifiers, such as Support Vector Machines or neural networks, are used to determine if a region contains a vehicle. Post-processing techniques refine the results, eliminating false positives. Finally, the detected vehicles are visualized by drawing bounding boxes around them, providing an automated solution for locating and identifying vehicles in images or video streams.
Certainly! Below is a basic README text that you can include with your code. Please customize it further based on your specific project details.

# Vehicle Detection and Counting System

## Overview

This Python script is designed for real-time vehicle detection and counting using YOLOv4, OpenCV, pyttsx3, and a custom object detection module. The system identifies vehicles in a video stream, assigns unique IDs for tracking, and provides a voice-guided interface.

## Installation

### Prerequisites

Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Install Required Libraries

```bash
pip install opencv-python pyttsx3 numpy art textblob
```

### Download YOLOv4 Weights

Download the YOLOv4 weights fils below the provided link and give the address of that files in object_detection.
https://github.com/AlexeyAB/darknet
Place the weights and cfg files in the object_detection directory .

## Usage

1. Open the script in a code editor.

2. Customize the video file path:

   ```python
   video = cv2.VideoCapture("C:\\Users\\DELL\\OneDrive\\Desktop\\Project\\Highway.mp4")
   ```

3. Modify the YOLOv4 weights path:

   ```python
   od = ObjectDetection(weights_path="path/to/yolov4.weights")
   ```

4. Run the script:

   ```bash
   python vehicle_detection.py
   ```

## Configuration

- **Changing the Voice:**
  - In the `set_voice()` function, update the voice indices based on your preference.

- **Adjusting Speaking Rate:**
  - Modify the speaking rate by changing the value in `engine.setProperty('rate', 135)`.

- **Object Detection Module:**
  - Customize the object detection logic in the `ObjectDetection` module based on specific project requirements.

Feel free to adapt the README according to your project's structure and additional configuration options.

##Output:
![2](https://github.com/Awais-Asghar/Vehicle-Detection-and-Counting-System-Using-Open-CV/assets/136043829/31e56d19-6a15-4207-96b9-1a4c20aed75d)
