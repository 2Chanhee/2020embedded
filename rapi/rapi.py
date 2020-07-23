# This code is test code

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

cap.set(3, 640)
cap.set(4, 480)

# Variable for lineTracing
vertical  = False
horiznal  = False
#numOfLine = 0

# LineTracing
def LineTracing(src):

    degree = np.array([])
    line   = np.array([])
    # Convert BGR to Gray for reduce time
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # Detect line using hough transformation
    canny = cv2.Canny(src, 50, 200)
    line  = cv2.HoughLines(canny, 1, np.pi/180, 100)

    # Find vertical line
    if line.shape[0] > 0 :
        degree = np.squeeze(line[:,:,1], axis = 1)
        degree = 1.57 - degree
    if np.any( np.abs(degree) > 1.27 ) :
        vertical = True
        print('Straight!')

    elif np.any( degree < 0) :
        vertical = False
        print('Turn left!')

    else :
        vertical = False
        print('Turn right!')
    
    if vertical == True | ( np.any( np.abs(degree) )  < 0.3 ):
        horiznal = True
        print("Cross!!")

    print(line)
    return degree 

# main
while(True):
    ret, frame = cap.read()
   
    cv2.imshow("Debug", frame)
    a = cv2.waitKey(1)
    if a == ord('q'):
        break

    elif a == ord('w'):
        cv2.imwrite('./test.png', frame)
        print('done')

    elif a == ord('x'):
        a = LineTracing(frame)
        print(a)


cv2.destroyAllWIndow()


