# This code is test code

import cv2
import numpy as np

def findLine(src):
    #src = cv2.equalizeHist(src)
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s = cv2.inRange(s, 70, 255)
    hsv = cv2.bitwise_and(hsv, hsv, mask = s)
    src = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return src

cap = cv2.VideoCapture(0)
#ret, frame = cap.read()

#if ret == False :
#    print('Camera is not open!')
#    exit()

cap.set(3, 640)
cap.set(4, 480)

#print(frame.shape)
while(True):
    ret, frame = cap.read()
    #frame = cv2.resize(frame, dsize = (320, 240), interpolation = cv2.INTER_NEAREST)    
    frame = findLine(frame)
    cv2.imshow("Debug", frame)
    a = cv2.waitKey(1)
    if a == ord('q'):
        break

    elif a == ord('w'):
        cv2.imwrite('./test.png', frame)
        print('done')

    elif a == ord('x'):
        # a = LineTracing(frame)
        print(a)


cv2.destroyAllWIndow()
