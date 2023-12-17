import cv2
import math
import numpy as np
import art
import pyttsx3
from textblob import TextBlob
from object_detection import ObjectDetection

# Print the Vehicle Detection Sys... on the screen 
Title = art.text2art("Vehicle  Detection  System")
print(Title)

engine = pyttsx3.init()
# It will provide the options to select a voices
def set_voice():
    print("Select a voice:")
    print("1. Male Voice")
    print("2. Female Voice")    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        # Set a male voice index
        engine.setProperty('voice', engine.getProperty('voices')[0].id)
    elif choice == "2":
        # Set a female voice index (you may need to adjust the index based on available voices)
        engine.setProperty('voice', engine.getProperty('voices')[1].id)
    else:
        print("Invalid choice. Using the default voice.")

# Call the function to set a voice
set_voice()

# Adjust this value to control the speaking rate
engine.setProperty('rate', 135)  

# Define a function that will speak a string either in male or a female voice 
def cool_tag_line():
    tag_line = """Welcome to our Vehicle Detection and Counting System, crafted precisely by Awais and Ahmad.
Let's explore this path side by side!"""
    print(tag_line)
    engine.say(tag_line)
    # Wait for the queued speech to finish
    engine.runAndWait()

# Call the cool_tag_line function
cool_tag_line()

# Initialize Object Detection
od = ObjectDetection()

# Open the video file
video = cv2.VideoCapture("C:\\Users\\DELL\\OneDrive\\Desktop\\Project\\Highway.mp4")

# Check if the video is opened successfully
if not video.isOpened():
    print("Error: Could not open video file.")
    exit()

# Initialize Count and center points
Count = 0
Center_Points_Current_Frame = []
Center_Points_Previous_Frame = []

# Initialize Tracking Objects and Tracking Ids
Tracking_Objects = {}
Track_Id = 0

while True:
    # Read the video
    _ret, frame = video.read()
    Count += 1
    if not _ret:
        print("There are no more frames, so we quit")
        break

    # Detect Objects on frame and give information about those objects
    (class_ids, scores, boxes) = od.detect(frame)

    # Draw rectangles on the frame for detected objects
    for box in boxes:
        (x, y, w, h) = box
        # Draw the circle on vehicles with Center point (cx,cy) and given radius
        cx = int((x + x + w) / 2)
        cy = int((y + y + h) / 2)

        Center_Points_Current_Frame.append((cx, cy))
        print("Frame No. ", Count, " ", x, y, w, h)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Tracking starts from the third frame
    if Count <= 2:
        for pt in Center_Points_Current_Frame:
            for pt2 in Center_Points_Previous_Frame:
                # Calculate distance between points to determine if they match
                distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])

                # If the distance is below a threshold, assign the same ID
                if distance < 10:
                    Tracking_Objects[Track_Id] = pt
                    Track_Id += 1
    else:
        # Create copies of Tracking_Objects and Center_Points_Current_Frame for safe iteration
        Tracking_Objects_Copy = Tracking_Objects.copy()
        Center_Points_Current_Frame_Copy = Center_Points_Current_Frame.copy()

        # Iterate through existing tracked objects
        for object_id, pt2 in Tracking_Objects_Copy.items():
            Object_Exists = False

            # Iterate through current frame points to find matches
            for pt in Center_Points_Current_Frame_Copy:
                # Calculate distance between points to determine if they match
                distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])

                # Update IDs Position if the distance is below a threshold
                if distance < 10:
                    Tracking_Objects[object_id] = pt
                    Object_Exists = True

                    # If the point is in the current frame, remove it from the list
                    if pt in Center_Points_Current_Frame:
                        Center_Points_Current_Frame.remove(pt)
                        continue

            # Remove IDs which are lost (not found in the current frame)
            if not Object_Exists:
                Tracking_Objects.pop(object_id)

        # Add New IDs found in the current frame
        for pt in Center_Points_Current_Frame:
            Tracking_Objects[Track_Id] = pt
            Track_Id += 1

        # Draw circles and numbers for tracked objects
        for object_id, pt in Tracking_Objects.items():
            cv2.circle(frame, (int(pt[0]), int(pt[1])), 5, (255, 255, 0), -1)
            cv2.putText(frame, str(object_id), (int(pt[0]), int(pt[1]) - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Print tracking information for debugging
    print("Tracking Objects")
    print(Tracking_Objects)

    print("Current Frame Left Points")
    print(Center_Points_Current_Frame)

    # Show the frame with rectangles
    cv2.imshow("frame", frame)

    # Update previous frame points for the next iteration
    Center_Points_Previous_Frame = Center_Points_Current_Frame.copy()
    Center_Points_Current_Frame = []

    # Wait for a key press (3 milliseconds) and check if the ESC key is pressed to exit the loop
    key = cv2.waitKey(3)
    if key == 27:
        break

# Release the video capture object and close all OpenCV windows
video.release()
cv2.destroyAllWindows()