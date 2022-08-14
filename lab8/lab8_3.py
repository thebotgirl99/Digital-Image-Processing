# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:14:48 2021

@author: HP
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

org = cv2.imread('C:/Users/HP/Desktop/M.Tech-SEM2/DIP/lab8/w.jpg')  #read the image
img= org.copy() #make a copy of the original image

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #convert the input colour image to a gray scale image
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)  #perform Otsu's thresholding

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)) #define the structuring element we need to perofrm the morphological operations. Here it is a 3x3 rectangle(filled with ones) 
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 3) #perform closing operation(dilation and then erosion) on the thresholded image using the structuring element, to eleminate any small holes in the image. 

sure_bg = cv2.dilate(opening,kernel,iterations=3) #dilation increases the object boundary to the background, so that we know for sure, what is the background of the image.

dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5) #distance transform finds the Euclidean distance to the closest background pixel for each of the foreground pixels. This is calculated to spearate the foreground from the background when objects are touching each other.

ret, sure_fg = cv2.threshold(dist_transform,0.45*dist_transform.max(),255,0) #perform thresholding operation on the distance transformed image with the threshold intenstiy value as 0.04 times the maximum pixel intesnity in the distance transfromed image.
#any pixel above the threshold value will be set to white. 

sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg) #The area where the foreground and background meet is the border. It is obtained bye subtracting foreground from background.

ret, markers = cv2.connectedComponents(sure_fg) #creare markers , where the regions which we know(the foreground) will be mrked with positive integers and label the background of the image with 0.

#the watershed function considers label 0 as unknown, hence increase all the markers by one so that the backgorund(Which is known) becomes 1 
markers = markers+1

#whatever regions are left unknown in the markers, label it as 0 for watershed function to detect it
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0] #the unknown regions, in our case the boundaries, will be modified to a value of -1 and will be marked/highlighted in red colour

plt.imshow(org) #plot all the images
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(thresh, 'gray')
plt.title("Otsu's threshold"), plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(opening, 'gray')
plt.title("opening"), plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(sure_bg, 'gray')
plt.title("Dilation"), plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(dist_transform, 'gray')
plt.title("Distance Transform"), plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(sure_fg, 'gray')
plt.title("Thresholded"), plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(unknown, 'gray')
plt.title("Unknown region"), plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(img, 'gray')
plt.title("Watershed"), plt.xticks([]), plt.yticks([])
plt.show()
