import torch
from LeagueAI_helper import input_output, LeagueAIFramework, detection
import time
import cv2

IO = input_output(input_mode='desktop', SCREEN_WIDTH=1920, SCREEN_HEIGHT=1080)
dim = (500,500)
frame = IO.get_pixels(dim)

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5x')  # or yolov5m, yolov5x, custom

# Images
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, PIL, OpenCV, numpy, multiple

# Inference
results = model(img)

# Results
results.show()  # or .show(), .save(), .crop(), .pandas(), etc.