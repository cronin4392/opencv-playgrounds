import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# blank[200:300, 300:400] = 0,255,0

# draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255, 0), thickness=-1)

# draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)

# draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)

# draw text
cv.putText(blank, 'Hello', (blank.shape[1]//2, blank.shape[0]//2), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 0), 2)
cv.imshow('Drawing', blank)

# img = cv.imread("Resources/Photos/cat.jpg")
# cv.imshow('Cat', img)

cv.waitKey(0)