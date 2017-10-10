#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 05:17:48 2017

@author: jeetkanjani7
"""

import numpy as np
import os

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.abspath(os.path.join(CUR_DIR, '../../data/dogs_cats/train'))
TXT_DIR = os.path.abspath(os.path.join(CUR_DIR, '../../data/dogs_cats'))
dog_images = [image for image in os.listdir(DATA_DIR) if 'dog' in image]
cat_images = [image for image in os.listdir(DATA_DIR) if 'cat' in image]
              
dog_train = dog_images[:int(len(dog_images)*0.7)]
dog_test = dog_images[int(len(dog_images)*0.7):]
cat_train = cat_images[:int(len(cat_images)*0.7)]
cat_test = cat_images[int(len(cat_images)*0.7):]

with open('{}/train.txt'.format(TXT_DIR), 'w') as f:
    for image in dog_train:
        f.write('{} 0\n'.format(image))
    for image in cat_train:
        f.write('{} 1\n'.format(image))
    f.close()
 
with open('{}/text.txt'.format(TXT_DIR), 'w') as f:
    for image in dog_test:
        f.write('{} 0\n'.format(image))
    for image in cat_test:
        f.write('{} 1\n'.format(image))
    f.close()
    