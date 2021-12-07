import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)

dialated = cv.dilate(canny, (3, 3), iterations=1)

eroded = cv.erode(dialated, (3, 3), iterations=1)

resized = cv.resize(img, (500, 500))

cropped = img[50:200, 200:400]
cv.imshow('Image', cropped)

# cv.setWindowProperty('Cat', cv.WND_PROP_TOPMOST, 1)
cv.waitKey(0)