# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:47:21 2021

@author: HP
"""

import cv2

image = cv2.imread("C:/Users/HP/Desktop/grape.jpg", 1) #Read the image 8 from the path where it is

def rotate_image(mat, angle): #define a function to rotate the image without cropping it
    
    height, width = mat.shape[:2] # Get the width and height of original image
    
    image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates of the centre of the image in reverse order

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.) #calculate the rotation matrix for the given angle

    abs_cos = abs(rotation_mat[0,0]) # Calculates the cos and sin of angle, taking absolutes of those.
    abs_sin = abs(rotation_mat[0,1])

    bound_w = int(height * abs_sin + width * abs_cos) # find the new width and height bounds after rotation
    bound_h = int(height * abs_cos + width * abs_sin)

    rotation_mat[0, 2] += bound_w/2 - image_center[0]  # subtract old image center (bringing it back to origin) and add the new image center coordinates
    rotation_mat[1, 2] += bound_h/2 - image_center[1]

    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))  # rotate image with the new bounds and translated rotation matrix to get the rotated image without cropping
    return rotated_mat

new_image= rotate_image(image, 45) #save the image returned by the rotate_image function in variable new_image and specify the image you read and angle you want to rotate by
near_img = cv2.resize(new_image,None, fx =10 , fy =10, interpolation = cv2.INTER_NEAREST) #Resize the image to (100,100) using nearest neighbor interpolation

bilinear_img = cv2.resize(new_image,None,fx =10, fy=10 , interpolation = cv2.INTER_LINEAR) #Resize the image to (100,100) using bilinear interpolation

bicubic_img = cv2.resize(new_image,None, fx =10, fy =10, interpolation = cv2.INTER_CUBIC) # #Resize the image to (100,100) using bicubic interpolation

cv2.imshow('ImageWindow', bicubic_img) #display the image
cv2.waitKey() #wait for specified time, if you press any key in that time, the program continues.




