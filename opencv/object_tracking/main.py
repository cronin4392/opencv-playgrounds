import cv2
from tracker import *

tracker = EuclideanDistTracker()

cap = cv2.VideoCapture("highway.mp4")

object_detecter = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    ret, frame = cap.read()

    roi = frame[340:720, 500:800]
    cv2.imshow("ROI", roi)

    mask = object_detecter.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)

        if area > 100:
            # cv2.drawContours(roi, [cnt], -1, (0,255,0), 2)
            x, y, width, height = cv2.boundingRect(cnt)
            detections.append([x,y,width,height])

    box_ids = tracker.update(detections)
    
    for box_id in box_ids:
        x, y, width, height, id = box_id
        cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(roi, (x, y), (x+width, y+height), (0, 255, 0), 3)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)
    if key == 120:
        break

cap.release()
cv2.destroyAllWindows()