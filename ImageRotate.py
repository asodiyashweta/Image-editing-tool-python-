# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 12:23:10 2018

@author: Meera Suthar
"""
# import the necessary packages
import numpy as np
import imutils
import cv2


ans2=int(input("Enter degrees: "))

# load the image from disk
image = cv2.imread("Imagedemo.jpg")

rotated = imutils.rotate_bound(image, ans2)
cv2.imshow("Rotated (Correct)", rotated)
cv2.waitKey(0)

    
    
    
    
    
    
    
    
    
    
    