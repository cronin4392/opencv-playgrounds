import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Picture', img)

cv.setWindowProperty('Picture', cv.WND_PROP_TOPMOST, 1)
cv.waitKey(0)