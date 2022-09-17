import cv2 as cv

# video files use this
def rescaleFrame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = [width, height]
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# live video use this
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

# Reading images
# img = cv.imread('Resources/Photos/cat_large.jpg')
# cv.imshow('Cat', img)

# Reading videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.2)
    cv.imshow('Video', frame_resized)

    if (cv.waitKey(20) & 0xFF==ord('d')):
        break

capture.release()
cv.destroyAllWindows()