# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 17:17:15 2021

@author: HP
"""

import cv2
from matplotlib import pyplot as plt

image = cv2.imread('C:/Users/HP/Downloads/OneDrive_1_3-5-2021/lowContrast.png',0)  #read the original image

plt.hist(image.ravel(),256,[0,256])  #plot the histogram of the original image
plt.savefig('lowcont_hist_before.png')  #save the original histogram plot

equalize = cv2.equalizeHist(image)  #perform histogram equalisation on the input image to stretch out the intensity range

cv2.imwrite('lowcontrast_equalized.png',equalize)  #save the output image

plt.hist(equalize.ravel(),256,[0,256])  #plot the histogram of the equalized image  
plt.savefig('lowcont_hist_after.png') #save the equalized histogram plot



