import cv2
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# x = width // 2
# y = height // 2
# w = width // 4
# h = height // 4

# CALL FUNCTION RECTANLE
def draw_rec(event, x, y, flags, params):
    global pt1, pt2, topLeftClick, botRightClick
    if event == cv2.EVENT_LBUTTONDOWN:
        if topLeftClick & botRightClick:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeftClick = False
            botRightClick = False
        if topLeftClick == False:
            pt1 = (x, y)
            topLeftClick = True
        elif botRightClick == False:
            pt2 = (x, y)
            botRightClick = True
            
# GLOBAL VARIABLES
pt1 = (0,0)
pt2 = (0,0)
topLeftClick = False
botRightClick = False
# CONNECT TO CALLBACK
cv2.namedWindow("Test")
cv2.setMouseCallback("Test", draw_rec)
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 4)
    if topLeftClick:
        cv2.circle(frame, center=pt1, radius=5, color=(255, 0, 0), thickness=-1)
    if topLeftClick & botRightClick:
        cv2.rectangle(frame, pt1, pt2, (0, 255, 0), 5)    
    cv2.imshow('Test', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()        