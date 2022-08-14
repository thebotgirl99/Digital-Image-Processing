# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:26:24 2021

@author: HP
"""

import cv2

img = cv2.imread('C:/Users/HP/Downloads/OneDrive_1_3-5-2021/ChessBoardGrad.png', 0) #read the original image

#shading operation can be done by causing a gaussian blur with a large kernel size
estimator = cv2.GaussianBlur(img, (579, 579), 0) #the value of kernel size should be 3*sigma in both directions(totally 6*sigma) rounded to nearest odd value
corrected = (img-estimator)  #the enhanced image is found by subtracting the estimator(Gaussian kernel) from the original image

cv2.imwrite('shading.png', estimator)  #save the output images
cv2.imwrite('corrected.png', corrected)

