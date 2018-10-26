# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:03:00 2018

@author: Meera Suthar
"""

import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import numpy as np
import imutils
import cv2



#img=mpimg('spiral_model.png')

img=mpimg.imread('Pic1.jpg')

plt.imshow(img)

plt.show()

bw=img.mean(axis=2)

#convert in b and w

plt.imshow(bw,cmap='gray')

plt.show()

W=np.zeros((20,20))

for i in range(20):
    for j in range(20):
        dist=(i-9.5)**2+(j-9.5)**2
        W[i,j]=np.exp(-dist/50)

plt.imshow(W,cmap='gray')

plt.show()

out=convolve2d(bw,W)

plt.imshow(out,cmap='gray')

plt.show()

out.shape

out=convolve2d(bw,W,mode='same')

plt.imshow(out,cmap='gray')

plt.show()
out.shape

bw.shape
out3=np.zeros(img.shape)

for i in range(3):
    out3[:,:,i]=convolve2d(img[:,:,i],W,mode='same')

#plt.imshow(out3)

#plt.show()

Hx=np.array([[-1,0,1],[-2,0,2],[-1,0,1]], dtype=np.float32)

Hy=Hx.T

Gx=convolve2d(bw,Hx)


img=Image.open("Imagedemo.jpg")
draw=ImageDraw.Draw(img)

font = ImageFont.truetype("arial.ttf",28, encoding="unic")

ans=input("Enter text to display: ")

draw.text((200,400),ans,(255,255,255),font=font)
img.save("abc.jpg")


ans2=int(input("Enter degrees: "))

# load the image from disk
image = cv2.imread("Imagedemo.jpg")

rotated = imutils.rotate_bound(image, ans2)
cv2.imshow("Rotated (Correct)", rotated)
cv2.waitKey(0)







