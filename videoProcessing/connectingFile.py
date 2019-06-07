import cv2
import time
cap = cv2.VideoCapture("../videos/video_1.mp4")
if cap.isOpened() == False:
    print("Error!")
while cap.isOpened():
    ret,  frame = cap.read()
    if ret == True:
        time.sleep(1/20)
        cv2.imshow("video", frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break        
cap.release()
cv2.destroyAllWindows()  
