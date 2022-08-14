# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:57:47 2021

@author: HP
"""

import cv2

image1 = cv2.imread('C:/Users/HP/Downloads/OneDrive_1_3-5-2021/Lenna.png',0)    # read the original images
image2 = cv2.imread('C:/Users/HP/Downloads/OneDrive_1_3-5-2021/ChessBoardGrad.png',0)

gaus1 = cv2.GaussianBlur(image1,(5,5),0)  #cause gaussian blur(smoothening) to the images with kernel size of 5
gaus2 = cv2.GaussianBlur(image2,(5,5),0)

laplacian1 = cv2.Laplacian(gaus1,cv2.CV_64F,ksize=3)  #apply laplacian correction with kernel size 3 to the images
laplacian_abs1 = cv2.convertScaleAbs(laplacian1)      #convert the transformed images back to their original scale(CV_8U)
laplacian2 = cv2.Laplacian(gaus2,cv2.CV_64F,ksize=3) 
laplacian_abs2 = cv2.convertScaleAbs(laplacian2)

sobelx1 = cv2.Sobel(image1,cv2.CV_8U,1,0,ksize=3)          # apply the sobel filter of kernel size 3, to the images in the horizontal direction
sobely1 = cv2.Sobel(image1,cv2.CV_8U,0,1,ksize=3)          # apply the sobel filter of kernel size 3, to the images in the vertical direction
sobelx2 = cv2.Sobel(image2,cv2.CV_8U,1,0,ksize=3)          
sobely2 = cv2.Sobel(image2,cv2.CV_8U,0,1,ksize=3)          

canny_edge1 = cv2.Canny(image1,80,170)   #apply canny edge detection to the images by specifying the two threshold values, minVal and maxVal
canny_edge2 = cv2.Canny(image2,50,250)

cv2.imwrite('laplacian_lenna.png',laplacian_abs1) #save the output images
cv2.imwrite('sobelx_lenna.png',sobelx1) 
cv2.imwrite('sobely_lenna.png',sobely1) 
cv2.imwrite('cannyedge_lenna.png',canny_edge1)
cv2.imwrite('laplacian_chess.png',laplacian_abs2)
cv2.imwrite('sobelx_chess.png',sobelx2) 
cv2.imwrite('sobely_chess.png',sobely2) 
cv2.imwrite('cannyedge_chess.png',canny_edge2)
