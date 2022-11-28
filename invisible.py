import cv2 #img processing
import numpy as np #numerical lib for handling img

cap = cv2.VideoCapture(0)
background =cv2.imread()#enter your background path in  (./bg.jpg )

while cap.isOpened():
    res, cur_frame = cap.read()
    if res:
        #conv rgb to hsv
        hsv_frame = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2HSV)

        #range for red colour
        #lower range
        l_red = np.array([0,120,70])
        u_red= np.array([10,255,255])
        mask1 = cv2.inRange(hsv_frame,l_red,u_red)

        #upper range
        l_red = np.array([170,120,70])
        u_red= np.array([100,255,255])
        mask2 = cv2.inRange(hsv_frame,l_red,u_red)

        #masking red
        red_mask= mask1 + mask2

        #for smooth edegs
        red_mask=cv2.morphologyEx(red_mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=10)
        red_mask=cv2.morphologyEx(red_mask,cv2.MORPH_DILATE,np.ones((3,3),np.uint8),iterations=1)

        #changing the red portion with bg
        part1= cv2.bitwise_and(background,background, mask= red_mask)

        #dectecting things which are not red
        red_free = cv2.bitwise_not(red_mask)

        #if obj is not present show curr frame
        part2= cv2.bitwise_and(cur_frame,cur_frame,red_mask)

        #final output
        cv2.imshow("magic Object", part1 + part2)
        if cv2.waitKey(5)== ord('q'):
            break
cap.release()
cv2.destroyAllWindows()