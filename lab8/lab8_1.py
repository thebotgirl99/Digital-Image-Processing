# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 13:59:11 2021

@author: HP
"""

import cv2 

img= cv2.imread('C:/Users/HP/Desktop/noisy_leaf.jpg',1)  #read the image
image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(image,(5,5),0)  #remove noise from the image using a 5x5 gaussian kernal by blurring the image
ret,th = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) #perform Otsu's thresholding to the gaussian blurred image.
#here the otsu's thresholding function is passed as an extra flag to the generic cv2.threshold function. The threshold value is chosen automatically based on the histogram peaks of the input image.
cv2.imshow('original', img) #display the original and thresholded image
cv2.imshow('otsu thresholded', th)
cv2.waitKey() #wait for specified time, if you press any key in that time, the program continues




