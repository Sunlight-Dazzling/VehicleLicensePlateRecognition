# -*- coding: utf-8 -*-
"""
Created on Sun May 23 18:07:13 2021

@author: Administrator
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io,data
import os
from PIL import Image
import tensorflow as tf
import math
import cv2
import sys
from scipy import ndimage
import random
dir='E:/CarReconition/CarTrain/train_images/training-set/chinese-characters/31/'
for root, dirs, files in os.walk(dir, topdown=False):
    for name in files:
        image_path = dir + name
        image_tmp = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
        rotate_image = ndimage.rotate(image_tmp,random.randint(7,30))
        rotate_image = cv2.resize(rotate_image,(32,40))
        rotate_image_path = image_path[:-4]+"_3.bmp"
        print(rotate_image_path)
        cv2.imwrite(rotate_image_path,rotate_image)
        rotate_image = ndimage.rotate(image_tmp,random.randint(6,10))
        rotate_image = cv2.resize(rotate_image,(32,40))
        rotate_image_path = image_path[:-4]+"_4.bmp"
        print(rotate_image_path)
        cv2.imwrite(rotate_image_path,rotate_image)
        rotate_image = ndimage.rotate(image_tmp,random.randint(350,355))
        rotate_image = cv2.resize(rotate_image,(32,40))
        rotate_image_path = image_path[:-4]+"_5.bmp"
        print(rotate_image_path)
        cv2.imwrite(rotate_image_path,rotate_image)
        rotate_image2 = ndimage.rotate(image_tmp,random.randint(330,355))
        rotate_image2 = cv2.resize(rotate_image2,(32,40))
        rotate_image_path2 = image_path[:-4]+"_2.bmp"
        print(rotate_image_path)
        cv2.imwrite(rotate_image_path2,rotate_image2)
        rotate_image2 = ndimage.rotate(image_tmp,random.randint(5,15))
        rotate_image2 = cv2.resize(rotate_image2,(32,40))
        rotate_image_path2 = image_path[:-4]+"_1.bmp"
        print(rotate_image_path)
        cv2.imwrite(rotate_image_path2,rotate_image2)
        #img = cv2.imread(filename)
        #img = Image.open(filename)
        #灰度化图片
        #print(img)
        
        #img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        #plt.imshow(img_gray)
        #二值化图片
        '''ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
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
                if (black[m] if arg else white[m]) > (0.95 * black_max if arg else 0.95 * white_max):  # 0.95这个参数请多调整，对应下面的0.05
                    end_ = m
                    break
            return end_
         
        n = 1
        start = 1
        end = 2
        pathresult="E:\\CarReconition\\CarDivision\\result"
        while n < width-2:
            h1=0
            h2=0
            n += 1
            if (white[n] if arg else black[n]) > (0.05 * white_max if arg else 0.05 * black_max):
                # 上面这些判断用来辨别是白底黑字还是黑底白字
                # 0.05这个参数请多调整，对应上面的0.95
                start = n
                end = find_end(start)
                n = end
                #print("%d---%d",start,end)
                if end-start > 15:
                    cj = thresh[1:height, start:end]
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
                    print("%d---%d",h1,h2)
                    #print(cj.shape)
                    if not os.path.exists(pathresult):
                        os.makedirs(pathresult)    
                    filepath=pathresult+name+str(+n)+".bmp"
                    cj=cv2.resize(cj,(32,40))
                    cv2.imwrite(filepath,cj, [int( cv2.IMWRITE_JPEG_QUALITY), 95])
                    #cv2.imshow('caijian', cj)
                    #cv2.waitKey(0)
                        
        
        #plt.imshow(thresh)
        #cv2.imshow("Image", thresh)
        #cv2.waitKey (0)
        cv2.destroyAllWindows()'''