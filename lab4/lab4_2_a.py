# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:51:15 2021
file: contrast stretching alternative
@author: Devasena
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/HP/Downloads/OneDrive_1_3-5-2021/inputq1.jpeg',0) #read the original image
org= np.asarray(img)
def pixelVal(pix, r1, s1, r2, s2):  #define a function to perform the contrast stretching operation
  if (0 <= pix and pix <= r1):      # if the pixel value lies between 0-r1, then the output is slope*r1 
   return (s1 / r1)*pix
  elif (r1 < pix and pix <= r2):    # if the pixel value lies between r1-r2, then the output is slope*(pixel value - r1) + intercept s1 
   return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
  else:
   return ((255 - s2)/(255 - r2)) * (pix - r2) + s2   # if the pixel value lies beyond r2, then the output is slope*(pixel value - r2) + intercept s2 

L = img.max()  #set the values as r1=r2, s1=0 and s2=L-1 to get binary image
r1 = 140
s1 = 30
r2= 200
s2 = L-1

pixelVal_vec = np.vectorize(pixelVal) #return all the pixel values as a single array 
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)  #call the pixelVal function to apply contrast stretching to the read image
fin= np.asarray(contrast_stretched)
plt.title("Contrast Stretched")
plt.imshow(contrast_stretched,'gray') #plot the image and show
plt.show()
plt.plot(org,fin)
plt.show()
hist,bins = np.histogram(contrast_stretched.ravel(),256,[0,256])
plt.plot(hist)
plt.show()