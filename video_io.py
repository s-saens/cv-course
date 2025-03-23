import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)

    d = (w, h)

    return cv.resize(frame, d, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture(0)

def changeRes(c: cv.VideoCapture, w, h):
    c.set(3, w)
    c.set(4, h)

while True:

    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    if isTrue == False or cv.waitKey(2) & 0xFF == ord('q'):
        break

    cv.imshow("Video", frame)
    cv.imshow("Video_Resized", frame_resized)



capture.release()
cv.destroyAllWindows()