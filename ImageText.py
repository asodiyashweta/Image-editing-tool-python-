# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:48:19 2018

@author: Meera Suthar
"""

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img=Image.open("Imagedemo.jpg")
draw=ImageDraw.Draw(img)

font = ImageFont.truetype("arial.ttf",28, encoding="unic")

ans=input("Enter text to display: ")

draw.text((200,400),ans,(255,255,255),font=font)
img.save("abc.jpg")

