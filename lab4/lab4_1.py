# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:54:04 2021
file: gamma correction
@author: Devasena
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

original = cv2.imread('C:/Users/HP/Desktop/M.Tech-SEM2/DIP/8.jpg' , 0) #read the original image
cv2.imshow('original',original) #display the original image

for gamma in [0.5, 2.5]: #perform the loop for different values of gamma
      
    adjusted = np.array(255*(original / 255) **gamma, dtype = 'uint8') # Apply the Gamma correction equation(output= input^gamma) by converting the gray level image to a range of [0,1], applying the correction and converting it back to the range [0,255]
    cv2.imshow("gamma corrected", adjusted)  #for each value of gamma display the corrected image
    cv2.waitKey(0)  #wait for specified time, if you press any key in that time, the program continues.
    hist = cv2.calcHist([adjusted],[0],None,[256],[0,256])
    plt.plot(hist)
    plt.show()



