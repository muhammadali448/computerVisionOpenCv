import cv2
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter("../videos/video_1.mp4v", fourcc, 20.0, (width,height))

while True:
    ret, frame = cap.read()
    writer.write(frame)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
writer.release()        
cv2.destroyAllWindows()        