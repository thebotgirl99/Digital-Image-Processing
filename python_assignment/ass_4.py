# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:28:38 2021

@author: HP
"""

import cv2

image = cv2.imread('C:/Users/HP/Downloads/OneDrive_1_3-5-2021/1200px-Monarch_In_May.jpg',0)  #read the original image

gaus = cv2.GaussianBlur(image,(3,3),0)  #cause a gaussian blur(smoothening) to the image with kernel size of 3 

laplacian = cv2.Laplacian(image,cv2.CV_16S,ksize=3) #apply laplacian correction with kernel size 3 to the image
lap_gaus = cv2.Laplacian(gaus,cv2.CV_16S,ksize=3)   #apply laplacian correction with kernel size 3 to the image after it has been smoothened using gaussian blur

laplacian_abs = cv2.convertScaleAbs(laplacian)   #convert the transformed images back to their original scale(CV_8U)
lap_gaus_abs = cv2.convertScaleAbs(lap_gaus)

cv2.imwrite('laplacian_monarch.png',laplacian_abs)  #save the output images
cv2.imwrite('laplacian+gaussian_monarch.png',lap_gaus_abs) 
