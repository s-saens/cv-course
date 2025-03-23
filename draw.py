import cv2 as cv
import numpy as np
import math

blank = np.zeros((500, 500, 3), dtype='uint8')
blank[:] = 255, 255, 255
cv.imshow('Blank', blank)

clicked = False
initialPosition = (0,0)

def mouseButton(ev, x, y, flags, params):
    if ev == cv.EVENT_LBUTTONDOWN:
        params[0] = True
        params[1] = (x, y)
    elif ev == cv.EVENT_LBUTTONUP:
        params[0] = False
        k = math.dist(params[1], (x, y))
        cv.circle(blank, params[1], int(k), (0, 0, 0), thickness=-1)
        cv.imshow('Blank', blank)

cv.setMouseCallback('Blank', mouseButton, [clicked, initialPosition])

cv.waitKey(0)