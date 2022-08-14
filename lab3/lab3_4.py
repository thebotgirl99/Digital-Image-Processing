# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 18:04:33 2021

@author: HP
"""

import cv2

image = cv2.imread("C:/Users/HP/Desktop/8.jpg", 1) #Read the image 8 from the path where it is

def rotate_image(mat, angle): #define a function to rotate the image without cropping it
    
    height, width = mat.shape[:2] # Get the width and height of original image
    
    image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates of the centre of the image in reverse order

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.) #calculate the rotation matrix for the given angle

    rotated_mat = cv2.warpAffine(mat, rotation_mat, (width, height))  # rotate image with the new bounds and translated rotation matrix to get the rotated image without cropping
    
    return rotated_mat

for i in range(4):
    new_image=rotate_image(image,90)
    image=new_image
  
cv2.imshow('ImageWindow', new_image) #display the image
cv2.waitKey() #wait for specified time, if you press any key in that time, the program continues.


