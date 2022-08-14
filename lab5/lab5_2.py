# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 15:44:14 2021

@author: Devasena

"""
import cv2
import numpy as np

image = cv2.imread('C:/Users/HP/Desktop/M.Tech-SEM2/DIP/low_cont.jpg')    # read the original image

sobelx = cv2.Sobel(image,cv2.CV_8U,1,0,ksize=3)          # apply the sobel filter of kernel size 3, to the image in the horizontal direction
sobely = cv2.Sobel(image,cv2.CV_8U,0,1,ksize=3)          # apply the sobel filter of kernel size 3, to the image in the vertical direction
sobel = sobelx + sobely                                  # combine both the x and y directions to get final sobel filter

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])         # define the 3x3 kernel in the horizontal dirrection for prewitt filter
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])         # define the 3x3 kernel in the vertical dirrection for prewitt filter
prewittx = cv2.filter2D(image, -1, kernelx)              # apply the 2D filter using the above defined kernel in x and y directions
prewitty = cv2.filter2D(image, -1, kernely)
prewitt = prewittx + prewitty                            # combine both the x and y directions to get final prewitt filter

kernelu = np.array([[1,-3,1],[-3,9,-3],[1,-3,1]])
unknown= cv2.filter2D(image, -1, kernelu)

laplacian = cv2.Laplacian(image,cv2.CV_64F,ksize=3)      # apply laplacian filter with a kernel size 3 to the image

cv2.imshow('original', image)                            # consequently display all the images
cv2.imshow('sobelx',sobelx)                              
cv2.imshow('sobely',sobely) 
cv2.imshow('sobel',sobel)
cv2.imshow('prewittx',prewittx)
cv2.imshow('prewitty',prewitty)
cv2.imshow('prewitt',prewitt)
cv2.imshow('laplacian',laplacian)
cv2.imshow('unknown', unknown) 
cv2.waitKey()
#wait for specified time, if you press any key in that time, the program continues
