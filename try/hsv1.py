# This code is test code

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#ret, frame = cap.read()

#if ret == False :
#    print('Camera is not open!')
#    exit()

cap.set(3, 2560)
cap.set(4, 1920)

#print(frame.shape)
while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame, dsize = (320, 240), interpolation = cv2.INTER_NEAREST)    
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
