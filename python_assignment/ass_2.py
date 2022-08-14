# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:17:01 2021

@author: HP
"""

import cv2 
import numpy as np 
  
img = cv2.imread('C:/Users/HP/Downloads/OneDrive_1_3-5-2021/logndlinear.jpg') #read the original image

c = 255/(np.log(1 + img.max())) #find the value of the constant c 
log = c * np.log(1 + img) #apply log transformation to the image
log_transform= np.array(log, dtype = np.uint8) #store the transformed pixels in array and specify it's data type

cv2.imwrite('logq2.jpg', log_transform)  #save the ouput image

def pixelVal(pix, r1, s1, r2, s2):  #define a function to perform the contrast stretching operation
  if (0 <= pix and pix <= r1):      # if the pixel value lies between 0-r1, then the output is slope*r1 
   return (s1 / r1)*pix
  elif (r1 < pix and pix <= r2):    # if the pixel value lies between r1-r2, then the output is slope*(pixel value - r1) + intercept s1 
   return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
  else:
   return ((255 - s2)/(255 - r2)) * (pix - r2) + s2   # if the pixel value lies beyond r2, then the output is slope*(pixel value - r2) + intercept s2 

#set the values as r1=r2, s1=0 and s2=L-1 to get binary image
r1 = 70
s1 = 0
r2= 140
s2 = 255

pixelVal_vec = np.vectorize(pixelVal) #return all the pixel values as a single array 
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)  #call the pixelVal function to apply contrast stretching to the read image

cv2.imwrite('linearq2.jpeg', contrast_stretched) #save the ouput image