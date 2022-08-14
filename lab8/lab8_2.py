# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:04:17 2021

@author: HP
"""

import cv2

image= cv2.imread('C:/Users/HP/Desktop/page.jpg') #read the image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
image= cv2.GaussianBlur(image,(5,5),0) #remove noise from the image using a 5x5 gaussian kernal by blurring the image. We use gaussian blur as it avoids ringing effects.
ret,th1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY) #perform a global thresholding operation, with the threshold intensity limit as 127(which is constant throughout), any pixel greater than the threshold value will be set to white
th2 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)  #perform adaptive thresholding where, the threshold limit is the mean of the blockSize×blockSize neighborhood of a pixel minus a constant. Here the block zise is 11 and the constant value is 2. 
th3 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2) 
 #perform adaptive thresholding where, the threshold limit is the weighted sum of the blockSize×blockSize neighborhood of a point minus constant. Here the block zise is 11 and the constant value is 2. 
#since here, the threshold value is calculated for smaller regions, it leads to different values for different regions with respect to the change in lighting. Hence it's a local thresholding method.
cv2.imshow('original', image) #display all the images
cv2.imshow('global', th1)
cv2.imshow('local-mean', th2)
cv2.imshow('local-gaussian', th3)
cv2.waitKey() #wait for specified time, if you press any key in that time, the program continues
