# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:40:53 2021

@author: HP
"""
import cv2
import numpy as np

img = cv2.imread('C:/Users/HP/Downloads/OneDrive_1_3-5-2021/inputq1.jpeg',0) #read the original image
     
def pixelVal(pix, r1, r2):          #define a function to perform the piecewise linear operation
  if (0 <= pix and pix <= r1):      # if the pixel value lies between 0-r1, then return pixel 
   return pix
  elif (r1 < pix and pix <= r2):    # if the pixel value lies between r1-r2, then the output intensity is 15
   return 15
  else:
   return pix   # if the pixel value lies beyond r2, then return pixel 

r1 = 120 #set the input pixel intensity limits, r1 and r2
r2= 200


pixelVal_vec = np.vectorize(pixelVal) #return all the pixel values as a single array 
piecewise = pixelVal_vec(img, r1, r2)  #call the pixelVal function to apply piecewise linear operation to the read image

cv2.imwrite('outputq1.jpeg', piecewise)  #save the ouput image




