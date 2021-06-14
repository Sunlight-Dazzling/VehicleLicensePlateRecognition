# -*- coding: utf-8 -*-
"""
Created on Tue May 25 14:45:46 2021

@author: Administrator
"""
#更改png为bmp
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
dir='E:/CarReconition/CarTrain/train_images/training-set/chinese-characters/20/'
for root, dirs, files in os.walk(dir, topdown=False):
    for name in files:
        image_path = dir + name
        if image_path[-4:]==".png":
            
            image_tmp = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
            rotate_image_path = image_path[:-4]+".bmp"
            cv2.imwrite(rotate_image_path,image_tmp)
            
'''
image_path='E:/CarReconition/CarTrain/train_images/training-set/chinese-characters/6/test2_1.png'
print(image_path[-4:])
if image_path[-4:]==".png":
    image_tmp = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    rotate_image_path = image_path[:-4]+".bmp"
    cv2.imwrite(rotate_image_path,image_tmp)
    '''