# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 14:06:30 2021

@author: HP
"""

import cv2
import numpy as np
from numpy.fft import fft2, ifft2  #import the 2D fast fourier transform module from numpy
import matplotlib.pyplot as plt

img = cv2.imread("C:/Users/HP/Desktop/1.jpg",0) #read the original image
gaus = cv2.blur(img,(7,7))             #apply gaussian blur to the image with kernel size of 7

kernel = np.ones((5,5)) / 25   #now create a kernel for the degradation function 
dummy = np.copy(gaus)          # now copy the gaussian blurred image to another variable called dummy
dummy = fft2(dummy)            #calculate the fourier transform of the blurred image
kernel = fft2(kernel, s = img.shape)     #calculate the fourier transform of the degradation function
kernel = np.conj(kernel) / (np.abs(kernel) ** 2 + 10e-2)  #calculate the weiner function
dummy = dummy * kernel               #now multiply the degraded image with the weiner function
dummy = np.abs(ifft2(dummy))         #perfrom the inverse fourier transfrom on the enhanced image


plt.imshow(img, cmap = 'gray')   #display the original image
plt.title('original'), plt.xticks([]), plt.yticks([])
plt.show()

plt.imshow(gaus, cmap = 'gray')   #display the blurred image
plt.title('blurred'), plt.xticks([]), plt.yticks([])
plt.show()

plt.imshow(dummy, cmap = 'gray')  #display the deblurred image
plt.title('deblurred'), plt.xticks([]), plt.yticks([])
plt.show()
