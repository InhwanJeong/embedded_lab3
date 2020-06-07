import cv2
import numpy as np

def diffImage(i):
    diff0 = cv2.absdiff(i[0], i[1])
    diff1 = cv2.absdiff(i[1], i[2])
    return cv2.bitwise_and(diff0, diff1)

def getGrayCamImg(cam):
    img = cam.read()[1]
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def updateCameraImage(cam, i):
    i[0] = i[1]
    i[1] = i[2]
    img = cam.read()[1]
    i[2] = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
       
def start(i):
    thresh = 32
    while True:
        diff = diffImage(i)
        ret,thrimg=cv2.threshold(diff, thresh, 1, cv2.THRESH_BINARY)
        count = cv2.countNonZero(thrimg)
        if (count > 1):
            nz = np.nonzero(thrimg)
            cv2.rectangle(diff,(min(nz[1]),min(nz[0])),(max(nz[1]),max(nz[0])),(255,0,0),2)
            cv2.rectangle(img,(min(nz[1]),min(nz[0])),(max(nz[1]),max(nz[0])),(0, 0, 255),2)
            cv2.imwrite('capture.jpg',img)
        cv2.imshow('Detecting Motion', diff)
        
        # process next image
        i0 = i1
        i1 = i2
        img = cam.read()[1]
        i2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        key = cv2.waitKey(10)
        if key == 27:
            break
