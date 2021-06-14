# -*- coding: utf-8 -*-
"""
Created on Mon May 24 21:27:29 2021

@author: Administrator
"""
import tensorflow as tf
import numpy as np
import math
import cv2
import sys
import os
from scipy import ndimage
import random
image_path='E:/CarReconition/CarTrain/train_images/training-set/chinese-characters/15/test44.bmp'
def distort_image():
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
    rotate_image_path2 = image_path[:-4]+"_2.png"
    print(rotate_image_path)
    cv2.imwrite(rotate_image_path2,rotate_image2)
    rotate_image2 = ndimage.rotate(image_tmp,random.randint(5,15))
    rotate_image2 = cv2.resize(rotate_image2,(32,40))
    rotate_image_path2 = image_path[:-4]+"_1.png"
    print(rotate_image_path)
    cv2.imwrite(rotate_image_path2,rotate_image2)

distort_image()
 
 

 