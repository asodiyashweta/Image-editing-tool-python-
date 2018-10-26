# -*- coding: utf-8 -*-
"""
Created on Thu Aug 9 11:37:23 2018

@author: Meera Suthar
"""

import cv2
 

refPt = []
cropping = False
 
def click_and_crop(event, x, y, flags, param):
    global refPt, cropping
 
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
 
	
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
 
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)
        
        
    croped = image.crop(refPt[0], refPt[1])
    croped.save("abc1.jpg")
    
    if len(refPt) == 2:
        roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        cv2.imshow("ROI", roi)
        cv2.waitKey(0)

   
        
        
        
image = cv2.imread('Pic1.jpg')
cv2.imshow("image", image)
clone = image.copy()

cv2.setMouseCallback("image", click_and_crop)
 


while True:
	
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
 
	
	if key == ord("r"):
		image = clone.copy()
 
	
	elif key == ord("c"):
		break
 

if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    cv2.imshow("Croped Image", roi)
    cv2.waitKey(0)
 

cv2.destroyAllWindows()




















