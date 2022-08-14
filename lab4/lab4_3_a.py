# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:11:05 2021
file: gray level slicing without background
@author: Devasena
"""

import cv2 
import numpy as np
from matplotlib import pyplot as plt 
  
img = cv2.imread('C:/Users/HP/Desktop/alb.jpg',0)  #read the original image

h,w = img.shape  #obtain the height and width of image

T1 = 100  #set the lower threshold value
   
T2 = 180  #set the upper threshold value

img_sliced = np.zeros((h,w), dtype = int) #create a new array of zeros to store the new image
   
for i in range(h): 
      
    for j in range(w): 
          
        if T1 < img[i,j] < T2:  
            img_sliced[i,j]= 255  #brighten the desired range of intensities
        else: 
            img_sliced[i,j] = 0   #change the other areas of the image to black

cv2.imwrite("gray_level_sliced_without.png", img_sliced)  #save the array as a png image

hist,bins = np.histogram(img_sliced.ravel(),256,[0,256])  #plot the histogram of the corrected image
plt.plot(hist)
plt.show()

