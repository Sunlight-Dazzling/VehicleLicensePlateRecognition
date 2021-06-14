# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:58:36 2021

@author: Administrator
"""
#按照比例分割字符
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io,data

import os
string='test'
img = cv2.imread('E:/CarReconition/CarDivision/Train/'+string+'.jpg')
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
#cj=thresh[7:n-7,0:m]
#cj=thresh[:,m:m*2]
#cj=thresh[:,m*2+30:m*3+30]
#cj=thresh[:,m*3+23:m*4+23]
#cj=thresh[:,m*4+10:m*5+10]
#cj=thresh[:,m*5+5:m*6+5]
#cj=thresh[:,m*6:m*7]
#plt.imshow(cj)
pathresult="./Train/26/"
count=0
num=0
while count<10:
    count=count+2
    
    cj=thresh[7:n-7,5:m+count]
    print(cj.shape)
    plt.imshow(cj)
    if not os.path.exists(pathresult):
        os.makedirs(pathresult)   
    num=num+1
    filepath=pathresult+string+str(num)+".bmp"
    cj=cv2.resize(cj,(32,40))
    cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])
count=0
while count<10:
    count=count+2
    
    cj=thresh[10:n-10,8:m+count]
    print(cj.shape)
    plt.imshow(cj)
    if not os.path.exists(pathresult):
        os.makedirs(pathresult)   
    num=num+1
    filepath=pathresult+string+str(num)+".bmp"
    cj=cv2.resize(cj,(32,40))
    cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])
count=0
while count<10:
    count=count+2
    
    cj=thresh[15:n-15,10:m+count]
    print(cj.shape)
    plt.imshow(cj)
    if not os.path.exists(pathresult):
        os.makedirs(pathresult)   
    num=num+1
    filepath=pathresult+string+str(num)+".bmp"
    cj=cv2.resize(cj,(32,40))
    cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])
count=0
while count<10:
    count=count+2
    
    cj=thresh[15:n-count,10:m+count]
    print(cj.shape)
    plt.imshow(cj)
    if not os.path.exists(pathresult):
        os.makedirs(pathresult)   
    num=num+1
    filepath=pathresult+string+str(num)+".bmp"
    cj=cv2.resize(cj,(32,40))
    cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])
count=0
while count<15:
    count=count+3
    
    cj=thresh[15:n-count,10:m+count]
    print(cj.shape)
    plt.imshow(cj)
    if not os.path.exists(pathresult):
        os.makedirs(pathresult)   
    num=num+1
    filepath=pathresult+string+str(num)+".bmp"
    cj=cv2.resize(cj,(32,40))
    cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])

count=0
while count<15:
    count=count+3
    
    cj=thresh[6:n-6,6:m+count]
    print(cj.shape)
    plt.imshow(cj)
    if not os.path.exists(pathresult):
        os.makedirs(pathresult)   
    num=num+1
    filepath=pathresult+string+str(num)+".bmp"
    cj=cv2.resize(cj,(32,40))
    cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])
    
count=0
while count<15:
    count=count+3
    
    cj=thresh[8:n-8,6:m+count]
    print(cj.shape)
    plt.imshow(cj)
    if not os.path.exists(pathresult):
        os.makedirs(pathresult)   
    num=num+1
    filepath=pathresult+string+str(num)+".bmp"
    cj=cv2.resize(cj,(32,40))
    cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])
count=0
while count<15:
    count=count+3
    
    cj=thresh[15:n-15,6:m+count]
    print(cj.shape)
    plt.imshow(cj)
    if not os.path.exists(pathresult):
        os.makedirs(pathresult)   
    num=num+1
    filepath=pathresult+string+str(num)+".bmp"
    cj=cv2.resize(cj,(32,40))
    cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])
count=0
while count<15:
    count=count+3
    
    cj=thresh[9:n-9,12:m+count]
    print(cj.shape)
    plt.imshow(cj)
    if not os.path.exists(pathresult):
        os.makedirs(pathresult)   
    num=num+1
    filepath=pathresult+string+str(num)+".bmp"
    cj=cv2.resize(cj,(32,40))
    cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])

    