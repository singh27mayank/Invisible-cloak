# importing important lib
import cv2
import time
#for camturing bg
cap = cv2.VideoCapture(1)#capture with webcam (0)
time.sleep(3)
#getting Bg image
while cap.isOpened():
    ret, background =cap.read() #reading Bg from webcam
    if ret:
        cv2.imshow("image",background)
        if cv2.waitKey(5)== ord('q'):
            cv2.imwrite("bg.jpg",background)
            break
cap.release()
cv2.destroyAllWindows()