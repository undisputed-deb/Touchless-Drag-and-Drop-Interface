import cv2
from cvzone.HandTrackingModule import HandDetector
from drag_image import DragImage

# Setup
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

detector = HandDetector(detectionCon=0.8, maxHands=2)

# Initial images
dragList = [
    DragImage("images/box.png", [100, 100]),
]

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Mirror

    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        fingers = detector.fingersUp(hands[0])

        # Gesture 1: Create new object if all fingers up
        if fingers == [1, 1, 1, 1, 1]:
            dragList.append(DragImage("images/box.png", [300, 300]))

        cursor = lmList[8]
        pinch_distance, _ = detector.findDistance(lmList[8], lmList[12])

        grabbing = pinch_distance < 40  # Fingers close = grab

        for dragImg in dragList:
            dragImg.update(cursor, grabbing, pinch_distance)

    # Draw
    for dragImg in dragList:
        isGrabbed = dragImg.dragging
        img = dragImg.draw(img, isGrabbed)

    cv2.imshow("Touchless Drag and Drop", img)
    cv2.waitKey(1)
