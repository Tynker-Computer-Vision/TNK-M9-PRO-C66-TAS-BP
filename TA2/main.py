import numpy as np
import cv2

# Set confidence thresholds


modelConfiguration = 'cfg/yolov3.cfg'
modelWeights = 'yolov3.weights'

# Path to labels file


# Load labels from file


yoloNetwork = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)

image = cv2.imread('static/img1.jpg')

dimensions = image.shape[:2]
H = dimensions[0]
W = dimensions[1]


blob = cv2.dnn.blobFromImage(image, 1/255, (416, 416))
yoloNetwork.setInput(blob)


# Get names of unconnected output layers


# Forward pass through network


# Initialize lists to store bounding boxes, confidences, and class Ids


# Process each output from YOLO network


        # Get class scores and ID of class with highest score
        


        # If confidence threshold is met, save bounding box coordinates and class Id
        





    # default red color
   

cv2.imshow('Image', image)
cv2.waitKey(0)
