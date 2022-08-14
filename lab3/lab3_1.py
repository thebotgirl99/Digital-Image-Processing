# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 13:04:12 2021

@author: HP
"""

import cv2 

image = cv2.imread("C:/Users/HP/Desktop/calvinHobbes.jpeg", 1)
#Read the image calvinHobbes from the path where it is

height, width = image.shape[:2] # Get the width and height of original image

print('original image size is', height, width) 
# You will get image size as (225,225) hence the scaling factor should be 2.25 to get (100,100)

near_img = cv2.resize(image, None, fx =2.25, fy =2.25, interpolation = cv2.INTER_NEAREST)
#Resize the image to (100,100) using nearest neighbour interpolation

bilinear_img = cv2.resize(image, None, fx =2.25, fy=2.25, interpolation = cv2.INTER_LINEAR) 
#Resize the image to (100,100) using bilinear interpolation

bicubic_img = cv2.resize(image, None, fx =2.25, fy =2.25, interpolation = cv2.INTER_CUBIC) 
#Resize the image to (100,100) using bicubic interpolation

cv2.imshow('ImageWindow', near_img) #display the images
cv2.imshow('ImageWindow', bilinear_img)
cv2.imshow('ImageWindow', bicubic_img)

cv2.waitKey() 
#wait for specified time, if you press any key in that time, the program continues

