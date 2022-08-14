# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 15:03:50 2021

@author: sena
"""

import cv2
import numpy as np

image0 = cv2.imread('C:/Users/HP/Desktop/fruit.jpg')   #read the original image
image1 = cv2.cvtColor(image0, cv2.COLOR_RGB2GRAY)      #convert the color image to grayscale image

image=np.array (image1/255, dtype=float)               #convert the image into an array with values ranging from 0 to 1 
mean=0                                                 # specify the mean and variance required
var= 0.002
noise=np.random.normal (mean, var ** 0.5, image.shape) # generate some random gaussian noise on normalized image 
out=image + noise                                      # add the gaussian noise to the grayscale image
if out.min ()<0:                                       # the bounds for the image are 0 to 1. In case the minimum pixel value is less than 0, set the lower bound to -1
    low_clip=-1.
else:
    low_clip=0.
out=np.clip (out, low_clip, 1.0)                       # clip the image so that the intensity values lie within the given range
out=np.uint8 (out * 255)                               # convert the image back to it's original scale
avg = cv2.blur(out,(5,5))                              # apply the averaging filter with kernel size of 5
gaus = cv2.GaussianBlur(out,(5,5),0)                   # apply gaussian filter with kernel size of 5
med = cv2.medianBlur(out,5)                            # apply median filter with kernel size of 5
cv2.imshow('Original image',image0)                    # consequently display all the images
cv2.imshow('Gray image', image1)
cv2.imshow('Gaussian noise',out)
cv2.imshow('Averaging filter',avg)
cv2.imshow('Gaussian filter',gaus)
cv2.imshow('median filter',med)
cv2.waitKey()                                          #wait for specified time, if you press any key in that time, the program continues
      
 
