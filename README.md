# Vehicle Detection Using Open CV
 Vehicle detection with OpenCV is a computer vision process involving the acquisition of images or video frames, followed by pre-processing for noise reduction through resizing and filtering. Object detection models like SSD or YOLO are employed to identify potential vehicle regions in the input. Relevant features are then extracted from these regions, and classifiers, such as Support Vector Machines or neural networks, are used to determine if a region contains a vehicle. Post-processing techniques refine the results, eliminating false positives. Finally, the detected vehicles are visualized by drawing bounding boxes around them, providing an automated solution for locating and identifying vehicles in images or video streams.
Certainly! Below is a basic README text that you can include with your code. Please customize it further based on your specific project details.

# Vehicle Detection and Counting System

## Overview

This Python script is designed for real-time vehicle detection and counting using YOLOv4, OpenCV, pyttsx3, and a custom object detection module. The system identifies vehicles in a video stream, assigns unique IDs for tracking, and provides a voice-guided interface.

## Installation

You have to download the python version of the 3.11.4.

### Prerequisites

Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Install Required Libraries

```bash
pip install opencv-python
pip install numpy
pip install art
pip install pyttsx3
pip install textblob
pip install colorama
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

## Working

## Image Processing:

Firstly you to download the libraries by using the above commands and then you have to save all the images and video files where your main.py file is located. 
When you will run the code then you have to answer some questions. When program ask for image processing then you have to put the name of that file only e.g 1
It depens on your image name and extension of image should be .png. For video processing repeat the same process and extension of video file should be .mp4
It can detect cars in smog also.
![1](https://github.com/Awais-Asghar/Vehicle-Detection-and-Counting-System-Using-Open-CV/assets/136043829/4e577579-220f-4c5d-a764-463ab9779ffb)

![2](https://github.com/Awais-Asghar/Vehicle-Detection-and-Counting-System-Using-Open-CV/assets/136043829/f269e931-241b-45a4-9dcb-0a06ee40e750)


## Video Processing:


![3](https://github.com/Awais-Asghar/Vehicle-Detection-and-Counting-System-Using-Open-CV/assets/136043829/f1a406c6-d371-4a94-bbdb-0c91c6d5aee9)


### Main.exe
You can download the main.exe file from one drive
  https://drive.google.com/file/d/1TI8mxt4K1U2ikKh_PYyNcLXpf9D88KCJ/view?usp=sharing
