import cv2 as cv
import numpy
if __name__=='__main__':
    img = cv.imread('./sample/test.jpg')[:,:,::-1]
    assert type(img) == numpy.ndarray
    print("Type is correct 😂😂😂😂")
