import cv2
import numpy as np

#### Function ####

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(newImg, (x, y), 20, (0, 255, 0), 2)    
cv2.namedWindow("my_drawing")
cv2.setMouseCallback("my_drawing", draw_circle)

#### Showing Image ####
img = cv2.imread("../DATA/dog_backpack.jpg")
newImg = cv2.resize(img, (960, 540))
while True:
    if cv2.waitKey(20) & 0xFF == 27:
        break  
    cv2.imshow("my_drawing", newImg)
cv2.destroyAllWindows()    