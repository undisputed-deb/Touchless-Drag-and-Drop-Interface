import cv2
from cvzone.HandTrackingModule import HandDetector
from drag_image import DragImage

# Setup
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

detector = HandDetector(detectionCon=0.8)

# Load images
dragList = [
    DragImage("images/box.png", [100, 100]),
]

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Mirror the camera

    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        cursor = lmList[8]  # Index finger tip
        length, info = detector.findDistance(lmList[8], lmList[12])


        grabbing = length < 40  # Close fingers = grabbing
        for dragImg in dragList:
            dragImg.update(cursor, grabbing)

    for dragImg in dragList:
        img = dragImg.draw(img)

    cv2.imshow("Touchless Drag and Drop", img)
    cv2.waitKey(1)
