# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 08:39:22 2021

@author: Devasena
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('C:/Users/HP/Desktop/v.jpg',0)  #read the grayscale image

#find frequency domain of image, it is a three-dimensional array, freq[:, :, 0] is the real part, freq[:, :, 1] is the imaginary part
freq = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
#initially output of freq is at top left corner bring it to centre 
shift_im = np.fft.fftshift(freq)

#find the magnitude spectrum of the image to observe areas of low/high frequency 
magnitude = np.log(1+ cv2.magnitude(shift_im[:,:,0],shift_im[:,:,1]))

#plot the images and observe the result
plt.imshow(image, cmap = 'gray')
plt.title('original image'), plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(magnitude, cmap = 'gray')
plt.title('Magnitude'), plt.xticks([]), plt.yticks([])
plt.show()

