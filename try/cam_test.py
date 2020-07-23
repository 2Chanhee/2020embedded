import cv2
import picamera

#with picamera.PiCamera() as camera:
#    camera.resolution = (640, 480)

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

while(True):
    ret, frame = cap.read()
    cv2.imshow("test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
