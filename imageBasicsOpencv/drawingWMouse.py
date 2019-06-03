import cv2
import numpy as np

#### Function ####

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 20, (255, 0, 0), -1)
cv2.namedWindow("my_drawing")
cv2.setMouseCallback("my_drawing", draw_circle)

#### Showing Image ####
img = np.zeros([512, 512, 3])
while True:
    if cv2.waitKey(20) & 0xFF == 27:
        break  
    cv2.imshow("my_drawing", img)
cv2.destroyAllWindows()    