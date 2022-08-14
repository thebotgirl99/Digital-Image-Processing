# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 17:04:17 2021

@author: HP
"""
import cv2

img1= cv2.imread('C:/Users/HP/Desktop/fruit.jpg')  #read the original colour image
image1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)     #convert the GRB image to grayscale
ret,thresh1 = cv2.threshold(image1,127,255,cv2.THRESH_BINARY)   #perform thresholding operation on grayscale image to convert to binary image

#cv2.imshow('original', img1)   # display both the original and thresholded images
#cv2.imshow('thresholded', thresh1)
#cv2.waitKey()  #wait for specified time, if you press any key in that time, the program continues.

img2= cv2.imread('C:/Users/HP/Desktop/bwero.jpg')
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
mask1 = cv2.erode(img2, kernel1, iterations=1)  
opening = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel1)
#cv2.imshow('original', img2)
#cv2.imshow('eroded', mask1)
#cv2.imshow('opened', opening)
#cv2.waitKey()


img3= cv2.imread('C:/Users/HP/Desktop/bwdil.jpg')
kernel2 =  cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
mask2 = cv2.dilate(img3, kernel2, iterations=1)  
closing = cv2.morphologyEx(img3, cv2.MORPH_CLOSE, kernel2)
#cv2.imshow('original', img3)
#cv2.imshow('dilated', mask2)
#cv2.imshow('closed', closing)
#cv2.waitKey()


img4= cv2.imread('C:/Users/HP/Desktop/fp.jpg')
kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
opening2 = cv2.morphologyEx(img4, cv2.MORPH_OPEN, kernel3)
closing2 = cv2.morphologyEx(opening2, cv2.MORPH_CLOSE, kernel3)
cv2.imshow('original', img4)
cv2.imshow('opened', opening2)
cv2.imshow('ope and clos', closing2)
cv2.waitKey()

