# This code is test code

import cv2
import numpy as np
import mission

cap = cv2.VideoCapture(0)
#ret, frame = cap.read()

cap.set(3, 640)
cap.set(4, 480)

while(True):
    ret, frame = cap.read()
   
    cv2.imshow("Debug", frame)
    a = cv2.waitKey(1)
    print(mission.FindArea(frame))
    if a == ord('q'):
        break

    elif a == ord('w'):
        cv2.imwrite('./test.png', frame)
        print('done')

    elif a == ord('x'):
        a = LineTracing(frame)
        print(a)


cv2.destroyAllWIndow()
