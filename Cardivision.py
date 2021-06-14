# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:05:58 2021

@author: Administrator
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io,data

import os
#将图片转为灰度图像
#img = cv2.imread('E:/CarReconition/test.bmp', cv2.COLOR_RGB2GRAY)

#将原图做个备份
#sourceImage = img.copy()
#cv2.imshow('sourceImage', img)
'''
img=cv2.imread('E:/CarReconition/test.bmp',cv2.COLOR_RGB2GRAY)
#print(img)
cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey (0)
cv2.destroyAllWindows()
'''
string='test'
img = cv2.imread('E:/CarReconition/CarDivision/Train/'+string+'.jpg')
#print(img)
#灰度化图片
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#plt.imshow(img_gray)
#二值化图片
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
#print(thresh)
#print(thresh.shape)

white = []  # 记录每一列的白色像素总和
black = []  # ..........黑色.......
height = thresh.shape[0]
width = thresh.shape[1]
white_max = 0
black_max = 0
# 计算每一列的黑白色像素总和
for i in range(width):
    s = 0  # 这一列白色总数
    t = 0  # 这一列黑色总数
    for j in range(height):
        if thresh[j][i] == 255:
            s += 1
        if thresh[j][i] == 0:
            t += 1
    white_max = max(white_max, s)
    black_max = max(black_max, t)
    white.append(s)
    black.append(t)
    #print(s)
    #print(t)
    
arg = False  # False表示白底黑字；True表示黑底白字
if black_max > white_max:
    arg = True
 
# 分割图像
def find_end(start_):
    end_ = start_+1
    for m in range(start_+1, width-1):
        if (black[m] if arg else white[m]) > (0.92 * black_max if arg else 0.92 * white_max):  # 0.95这个参数请多调整，对应下面的0.05
            end_ = m
            break
    return end_
n = 1
start = 1
end = 2
pathresult="./Train/26/"
m = 0
count=0
while n < width-2:
    h1=0
    h2=0
    n += 1
    if (white[n] if arg else black[n]) > (0.08 * white_max if arg else 0.08 * black_max):
        # 上面这些判断用来辨别是白底黑字还是黑底白字# 0.05这个参数请多调整，对应上面的0.95
        start = n
        end = find_end(start)
        n = end
        if end-start > 5:
            while (count < 8):
                count = count + 2
                cj = thresh[1:height, start-count:end]
                
                #cj = thresh[1:height, start-20:end+20]
                for i in range(7,cj.shape[0]-7):
                    s1 = 0  # 每一行白色总数
                    for j in range(cj.shape[1]):
                        if cj[i][j] == 255:
                            s1 += 1
                    if s1 != 0:
                        if h1 == 0:
                            h1=i
                        else: 
                            h2=i
                cj=cj[h1:h2,0:end]
                
                #cj=cj[h1:h2+count,10:end+5]
                #cj=cj[h1-5:h2+count,0:end+5]
                #cj=cj[h1-4:h2+count,0:end+5]
                #cj=cj[h1:h2+count,0:end+8]
                #cj=cj[h1:h2+count,0:end+10]
                #cj=cj[h1-2:h2+count,6:end+10]
                #cj=cj[h1-4:h2+count,4:end+8]
                #cj=cj[h1-7:h2+count,2:end+10]
                #cj=cj[h1:h2+count,1:end+9]
                #cj=cj[h1-2:h2+count,6:end+7]
                print(cj.shape)
                if not os.path.exists(pathresult):
                    os.makedirs(pathresult)   
                m=m+1
                filepath=pathresult+string+str(m)+".bmp"
                cj=cv2.resize(cj,(32,40))
                cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])
                
            '''cj = thresh[1:height, start-5:end]
            for i in range(7,cj.shape[0]-7):
                #print("i=======%d",i)
                s1 = 0  # 每一行白色总数
                for j in range(cj.shape[1]):
                    if cj[i][j] == 255:
                        s1 += 1
                #print(s1)
                if s1 != 0:
                    if h1 == 0:
                        h1=i
                    else: 
                        h2=i
            cj=cj[h1:h2,0:end]
            #print("%d---%d",h1,h2)
            #print(cj.shape)
            if not os.path.exists(pathresult):
                os.makedirs(pathresult)   
            m=m+1
            filepath=pathresult+string[:-1]+str(m)+".bmp"
            cj=cv2.resize(cj,(32,40))
            cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])'''
cv2.destroyAllWindows()
