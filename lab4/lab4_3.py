# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:22:28 2021
file: gray level slicing with background
@author: Devasena
"""

import cv2 
import numpy as np
from matplotlib import pyplot as plt 
  
img = cv2.imread('C:/Users/HP/Desktop/M.Tech-SEM2/DIP/8.jpg',0)  #read the original image

h,w= img.shape #obtain the height and width of image
    
T1 = 200  #set the lower threshold value
  
T2 = 1000  #set the upper threshold value 
   
img_sliced = np.zeros((h,w), dtype = int) #create a new array of zeros to store the new image
   
for i in range(h): 
      
    for j in range(w): 
          
        if T1 < img[i,j] < T2:  
            img_sliced[i,j]= 255   #brighten the desired range of intensities 
        else: 
            img_sliced[i,j] = img[i,j] #leave the other areas of the image unchanged
   
cv2.imwrite('gray_level_sliced_with.png', img_sliced) # save the array as a png image

hist,bins = np.histogram(img_sliced.ravel(),256,[0,256]) #plot the histogram of the corrected image
plt.plot(hist)
plt.show()




