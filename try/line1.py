# This code is test code

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

cap.set(3, 320)
cap.set(4, 240)

def Direction(src):
    cut = src[120:240]

    hsv = cv2.cvtColor(cut, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    h = cv2.inRange(h, 20, 33)
    h = h
    
    s = cv2.inRange(s, 80, 180)
    s = s
    
    h = cv2.bitwise_and(h, h, mask = s)
    h = h/255
    

    mask = np.zeros(320)
    mask[  0: 80] = 1
    mask[240:320] = 1
    
    temp = np.dot(h, mask)
    left  = sum(temp[ 0:50])
    right = sum(temp[90:120])
    #print(temp.shape)
    #print(left, end = '\r')
    if left > 500 :
        print("left! \r", end = '')
    elif right > 500:
        print("right!\r", end = '')

# main
while(True):
    ret, frame = cap.read()
    '''
    cv2.imshow('Debug', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) == ord('w'):
        cv2.imwrite('./test.png', frame)'''
    Direction(frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    h = cv2.inRange(h, 20, 33)
    img_mask = cv2.bitwise_and(hsv, hsv, mask = h)
     
    s = cv2.inRange(s, 80, 180)
    img_mask = cv2.bitwise_and(img_mask,img_mask , mask = s)
    img_mask = cv2.cvtColor(img_mask, cv2.COLOR_HSV2BGR)

    cv2.imshow('Debug', img_mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) == ord('w'):
        cv2.imwrite('./test.png', frame)

cv2.destroyAllWIndow()


