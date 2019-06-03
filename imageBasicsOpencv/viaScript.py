import cv2
img = cv2.imread("../DATA/dog_backpack.jpg")
newImg = cv2.resize(img, (960, 540))
while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break      
    cv2.imshow("Puppy", newImg)

cv2.destroyAllWindows()