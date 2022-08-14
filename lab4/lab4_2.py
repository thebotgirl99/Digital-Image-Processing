# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:17:02 2021
file: contrast stretching
@author: Devasena
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

original = cv2.imread("C:/Users/HP/Desktop/moon.jpg", 0) #read the original image

norm_img = cv2.normalize(original, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F) # Do contrast stretching by normalization (min-max) inbuilt function

norm_img = (255*norm_img).astype(np.uint8) # scale the image to uint8 type

cv2.imshow('original',original)  # display both the original and stretched images
cv2.imshow('contrast stretched',norm_img)
cv2.waitKey(0)  #wait for specified time, if you press any key in that time, the program continues.

hist = cv2.calcHist([norm_img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()
