# -*- coding: utf-8 -*-
"""
@author: Devasena
"""

import cv2
import numpy as np
import math      
import pyautogui    #the library responsible for controlling vlc media player   
cap = cv2.VideoCapture(0) #capture frames continously using a real time web camer
     
while(1):
        
    try:  #an error comes if it does not find anything in window as it cannot find contour of max area
          #therefore this try error statement
          
        ret, frame = cap.read()   #read the input images captured from the webcam frame by frame
        frame=cv2.flip(frame,1)   #flip the image about y axis to avoid confusion on which hand you are currently using
        
        roi=frame[100:300, 100:300] #define region of interest within the enitre frame captured. In our case, the area around our hand
        
        cv2.rectangle(frame,(100,100),(300,300),(0,255,0),0)    #create a rectangular box to visually define the region of interest
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)  #convert the real time RGB image to a HSV, which makes it easier to segment objects based on its colour
        
        #define the range of H, S and V values according to skin color
        lower_skin = np.array([0,20,70], dtype=np.uint8)  #this range represents a whitish-peach colour (colour of users hand can be adjusted)
        upper_skin = np.array([20,255,255], dtype=np.uint8) 
        
        mask = cv2.inRange(hsv, lower_skin, upper_skin) #this creates a binary image where your hand(white) is extracted from the background(black)
        kernel = np.ones((3,3),np.uint8)  #create an 8 bit 3x3 kernel filled with ones for dilation operation
        mask = cv2.dilate(mask,kernel,iterations = 2) #fill in the empty dark spots in the binary hand image thorugh dilation to make it clearly visible
        mask = cv2.GaussianBlur(mask,(5,5),100)  #blur the image to reduce noise
        
        contours,hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  #this gives the list of all the contours in the image
     
        cnt = max(contours, key = lambda x: cv2.contourArea(x))  #find contour of max area of interest, in this case, our hand
        
        #approximate the contour for better boundary detection 
        epsilon = 0.0005*cv2.arcLength(cnt,True)
        approx= cv2.approxPolyDP(cnt,epsilon,True)
        
        #make convex hull around hand
        hull = cv2.convexHull(cnt)
       
        #define area of hull and area of hand
        areahull = cv2.contourArea(hull)
        areacnt = cv2.contourArea(cnt)
        arearatio=((areahull-areacnt)/areacnt)*100 #find the percentage of area not covered by hand in convex hull
        
        #find the convex hull of the approximated hand and the defects
        hull = cv2.convexHull(approx, returnPoints=False)
        defects = cv2.convexityDefects(approx, hull)
        
        l=0  #define a variable to store the number of defects
        
        #find the no. of defects due to fingers
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])
            
            
            # find length of all sides of triangle formed between the two fingers
            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
            s = (a+b+c)/2
            ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
            
            #find distance between defect point and convex hull
            d=(2*ar)/a
            
            # apply cosine rule here
            angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
            
        
            # ignore angles > 90 and ignore points very close to convex hull(they generally come due to noise)
            if angle <= 90 and d>30:
                l += 1
                cv2.circle(roi, far, 3, [255,0,0], -1) #represent the defects as circular blue points
            
            #draw lines around hand within the region of interest
            cv2.line(roi,start, end, [0,255,0], 2)
            
            
        
        #print corresponding gestures which are in their ranges
        font = cv2.FONT_HERSHEY_SIMPLEX
        if l==0:
            if areacnt<2000:
                cv2.putText(frame,'Put hand in the box',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            else:
                if arearatio<12:
                    cv2.putText(frame,'0',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                else:
                    cv2.putText(frame,'1',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                    
        elif l==1:
            cv2.putText(frame,'2',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            pyautogui.typewrite(['space'], 0.5)

        elif l==2:
            cv2.putText(frame,'3',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            pyautogui.hotkey('ctrl', 'left')       
        elif l==3:
            cv2.putText(frame,'4',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            pyautogui.hotkey('ctrl', 'right')    
            
        elif l==4:
            cv2.putText(frame,'5',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        else :
            cv2.putText(frame,'reposition',(10,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            
        #show the actual image and the thresholded image of hand gestures
        cv2.imshow('mask',mask)
        cv2.imshow('frame',frame)
    except:   
        pass
        
    
    cv2.waitKey(25)
             
    
cv2.destroyAllWindows()
cap.release() #Closes video file or capturing device