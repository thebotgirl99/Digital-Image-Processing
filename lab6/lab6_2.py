# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 08:57:54 2021

@author: Devasena
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('C:/Users/HP/Desktop/M.Tech-SEM2/DIP/apple.jpeg',0)  #read the grayscale image
 
#find frequency domain of image, it is a three-dimensional array, freq[:, :, 0] is the real part, freq[:, :, 1] is the imaginary part
freq = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
#initially output of freq is at top left corner bring it to centre 
shift_im = np.fft.fftshift(freq)
 
rows, cols = image.shape[:2]  #get the no. of rows and columns of image
mid_row, mid_col = int(rows / 2), int(cols / 2)  #find the centre pixel

radius=50  #specify the radius
 
# Build a mask, two channels, such that centre pixel range is 1, all others are 0
mask = np.zeros((rows, cols,2), np.float32)
mask[mid_row - radius:mid_row + radius, mid_col - radius:mid_col + radius] = 1

#multiply the frequency domain of image with the mask
filter_im = shift_im * mask
#shift the image back to original centre
ishift = np.fft.ifftshift(filter_im)
#find inverse fourier transform to get enhanced image
image_enhanced = cv2.idft(ishift)
image_enhanced = cv2.magnitude(image_enhanced[:, :, 0], image_enhanced[:, :, 1])

#plot the images and observe the result
plt.imshow(image, cmap = 'gray')
plt.title('input'), plt.xticks([]), plt.yticks([])
plt.show()  
plt.imshow(image_enhanced, cmap = 'gray')
plt.title('output'), plt.xticks([]), plt.yticks([])
plt.show()   
     