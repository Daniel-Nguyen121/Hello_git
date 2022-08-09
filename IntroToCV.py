# Import the lib
import cv2 as cv

# Reading the image using imread()
image = cv.imread('Image/pic_1.jpg')

cv.imshow('pic1', image)

cv.waitKey(0)
