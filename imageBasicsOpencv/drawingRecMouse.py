import cv2
import numpy as np


#### Variables ####
# False while mouse button down and True while mouse button up
drawing = False
ix = -1 
iy = -1


#### Function ####

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            # cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)
            cv2.line(img, (ix, iy), (x, y), (255, 0, 0), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)
        cv2.line(img, (ix, iy), (x, y), (255, 0, 0), 2)
        

#### Showing Image ####
img = np.zeros([512, 512, 3], dtype=np.int8)
cv2.namedWindow("my_drawing")
cv2.setMouseCallback("my_drawing", draw_rectangle)

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break
    cv2.imshow("my_drawing", img)
cv2.destroyAllWindows()    