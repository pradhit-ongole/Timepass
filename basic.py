import cv2
import numpy as np

img = cv2.imread('messi.jpg')
px = img[100,100,0]
print(px)
