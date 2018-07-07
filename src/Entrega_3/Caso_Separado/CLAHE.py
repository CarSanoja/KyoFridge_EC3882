# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 10:10:35 2017

@author: carlos
"""
import cv2

def CLAHE(image):
    image = cv2.cvtColor(image,cv2.COLOR_BGR2HLS)
    h,l,s= cv2.split(image)
    clahe=cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) 
    img= clahe.apply(l)
    img2=cv2.merge((h,img,s))
    return img2