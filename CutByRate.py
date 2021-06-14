# -*- coding: utf-8 -*-
"""
Created on Fri May 28 21:39:21 2021

@author: Administrator
"""
#按照比例分割字符
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io,data

import os
string='test6'
img = cv2.imread('E:/CarReconition/CarDivision/Train/'+string+'.bmp')
#print(img)
#灰度化图片
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#plt.imshow(img_gray)
#二值化图片
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
print(thresh)
print(thresh.shape)
plt.imshow(thresh)
m=int(thresh.shape[1]/7)
print(m)
n=thresh.shape[0]
#单个字符获取
pathresult="E:/CarReconition/Test/divsion/"
num=70
cj=thresh[7:n-7,20:m]
print(cj.shape)
plt.imshow(cj)
if not os.path.exists(pathresult):
    os.makedirs(pathresult)   
num=num+1
filepath=pathresult+str(num)+".bmp"
cj=cv2.resize(cj,(32,40))
cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])

cj=thresh[7:n-7:,m:m*2]
print(cj.shape)
plt.imshow(cj)
if not os.path.exists(pathresult):
    os.makedirs(pathresult)   
num=num+1
filepath=pathresult+str(num)+".bmp"
cj=cv2.resize(cj,(32,40))
cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])

cj=thresh[7:n-7:,m*2+30:m*3+30]
print(cj.shape)
plt.imshow(cj)
if not os.path.exists(pathresult):
    os.makedirs(pathresult)   
num=num+1
filepath=pathresult+str(num)+".bmp"
cj=cv2.resize(cj,(32,40))
cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])

cj=thresh[7:n-7:,m*3+23:m*4+23]
#cj=thresh[7:n-7:,m*4+10:m*5+10]
#cj=thresh[7:n-7:,m*5+5:m*6+5]
#cj=thresh[7:n-7:,m*6:m*7]
print(cj.shape)
plt.imshow(cj)
if not os.path.exists(pathresult):
    os.makedirs(pathresult)   
num=num+1
filepath=pathresult+str(num)+".bmp"
cj=cv2.resize(cj,(32,40))
cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])

cj=thresh[7:n-7:,m*4+10:m*5+10]
print(cj.shape)
plt.imshow(cj)
if not os.path.exists(pathresult):
    os.makedirs(pathresult)   
num=num+1
filepath=pathresult+str(num)+".bmp"
cj=cv2.resize(cj,(32,40))
cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])

cj=thresh[7:n-7:,m*5+5:m*6+5]
#cj=thresh[7:n-7:,m*6:m*7]
print(cj.shape)
plt.imshow(cj)
if not os.path.exists(pathresult):
    os.makedirs(pathresult)   
num=num+1
filepath=pathresult+str(num)+".bmp"
cj=cv2.resize(cj,(32,40))
cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])

cj=thresh[7:n-7:,m*6:m*7]
print(cj.shape)
plt.imshow(cj)
if not os.path.exists(pathresult):
    os.makedirs(pathresult)   
num=num+1
filepath=pathresult+str(num)+".bmp"
cj=cv2.resize(cj,(32,40))
cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])

