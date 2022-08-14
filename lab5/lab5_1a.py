# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 15:18:50 2021

@author: HP
"""

import cv2
import numpy as np
import random
image0 = cv2.imread('C:/Users/HP/Desktop/fruit.jpg')   #read the original image
image1 = cv2.cvtColor(image0, cv2.COLOR_RGB2GRAY)      #convert the color image to grayscale image
prob=0.2                                               # set the probability value to 20%
output=np.zeros (image1.shape, np.uint8)               # generate an image array initally with zeros
thres=1-prob                                           # initialize the thresholding variable
for i in range (image1.shape [0]):                     #add salt and pepper noise by generating random dark pixels in bright areas and random white pixels in dark areas
  for j in range (image1.shape [1]):
      rdn=random.random()
      if rdn<prob:
        output [i][j]=0
      elif rdn>thres:
        output [i][j]=255
      else:
        output [i][j]=image1[i][j]                     # preserve the pixel intensities within the range of probablity and threshold values
avg = cv2.blur(output,(5,5))                           #apply the averaging filter with kernel size of 5
gaus = cv2.GaussianBlur(output,(5,5),0)                #apply gaussian filter with kernel size of 5
med = cv2.medianBlur(output,5)                         # apply median filter with kernel size of 5
cv2.imshow('Original image',image0)                    # consequently display all the images
cv2.imshow('Gray image', image1)
cv2.imshow('salt&pepper noise',output)
cv2.imshow('Averaging filter',avg)
cv2.imshow('Gaussian filter',gaus)
cv2.imshow('median filter',med)
cv2.waitKey()
#wait for specified time, if you press any key in that time, the program continues