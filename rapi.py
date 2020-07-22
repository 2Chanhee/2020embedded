import cv2
import numpy as np
import tesseract as tsr

# Setup and Get Video
# Get video
cap = cv2.VideoCapture(0)
if !cv2.isOpen():
    print("Can not open Camera!")

# Original image size is (480, 640)
# We use shrink image
cap.set(3, 320)
cap.set(4, 240)

# Loop
while(True):
    ret, frame = cap.read()

    # We will use gray scale image
    gry = cv2.cvtColor(srk, cv2.COLOR_BGR2GRAY)
    
# Check direction for line tracing
def Direction(src):
    
    # Cut front image
    cut = scr[160:240] # cut.shape == [80, 320, 3]

    # Detect yellow line
    hsv = cv2.cvtColor(cut, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    h = cv2.inRange(h, 20, 35) # if detect yellow, then h's element is 255
    h = h/255

    # Make left/right mask
    # Change range!!
    mask = np.zeros[320]
    mask[  0:100] = 1
    mask[220:320] = 1
    temp = np.dot(h, mask)
    left  = sum(temp[  0:100])
    right = sum(temp[220:320])

    if left[0] > 20 :
        # Send message

    elif right[0] > 20 :
        # Send nessage
