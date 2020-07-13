# -*- coding: utf-8 -*-
"""Satu.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EJu1KVAE7FP9I9_8NyqHGPkDdjLoC9ft
"""

from google.colab import drive
drive.mount('/content/gdrive')

import os
print(os.listdir('/content/gdrive/My Drive/'))

!unzip '/content/gdrive/My Drive/CV-20200627T143437Z-001.zip' -d'/content/gdrive/My Drive/'

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from google.colab import files
from keras.preprocessing import image
import random 
import os
import shutil

os.makedirs('/content/gdrive/My Drive/CV/train_set/train_drawings')

os.makedirs('/content/gdrive/My Drive/CV/train_set/train_painting')
os.makedirs('/content/gdrive/My Drive/CV/train_set/test_painting')
os.makedirs('/content/gdrive/My Drive/CV/train_set/train_engraving')
os.makedirs('/content/gdrive/My Drive/CV/train_set/test_engraving')
os.makedirs('/content/gdrive/My Drive/CV/train_set/train_iconography')
os.makedirs('/content/gdrive/My Drive/CV/train_set/test_iconography')
os.makedirs('/content/gdrive/My Drive/CV/train_set/train_sculpture')
os.makedirs('/content/gdrive/My Drive/CV/train_set/test_sculpture')

def split_data(source,train_dir,test_dir,split_size):
   shuffled_source = random.sample(os.listdir(source),len(os.listdir(source)))
   train_list = shuffled_source[: int(split_size*len(os.listdir(source)))]
   test_list = shuffled_source[int(split_size*len(os.listdir(source))) :]
   
   for files in train_list:
    shutil.copyfile(os.path.join(source,files),os.path.join(train_dir,files))

   for files in test_list:
     shutil.copyfile(os.path.join(source,files),os.path.join(test_dir,files))

split_data('/content/gdrive/My Drive/CV/train_set/drawings/','/content/gdrive/My Drive/CV/train_set/train_drawings','/content/gdrive/My Drive/CV/train_set/test_drawings',0.9)
split_data('/content/gdrive/My Drive/CV/train_set/painting/','/content/gdrive/My Drive/CV/train_set/train_painting','/content/gdrive/My Drive/CV/train_set/test_painting',0.9)
split_data('/content/gdrive/My Drive/CV/train_set/engraving/','/content/gdrive/My Drive/CV/train_set/train_engraving','/content/gdrive/My Drive/CV/train_set/test_engraving',0.9)
split_data('/content/gdrive/My Drive/CV/train_set/iconography/','/content/gdrive/My Drive/CV/train_set/train_iconography','/content/gdrive/My Drive/CV/train_set/test_iconography',0.9)
split_data('/content/gdrive/My Drive/CV/train_set/sculpture/','/content/gdrive/My Drive/CV/train_set/train_sculpture','/content/gdrive/My Drive/CV/train_set/test_sculpture',0.9)

model = tf.keras.models.Sequential(
    [
                        tf.keras.layers.Conv2D(16,(3,3),activation = 'relu',input_shape = (300,300,3)),
                        tf.keras.layers.MaxPooling2D(2,2),
                        tf.keras.layers.Conv2D(32,(3,3),activation = 'relu'),
                        tf.keras.layers. MaxPooling2D(2,2),
                        tf.keras.layers.Conv2D(64,(3,3),activation = 'relu'),
                        tf.keras.layers.MaxPooling2D(2,2),
                        tf.keras.layers.Conv2D(64,(3,3),activation = 'relu'),
                        tf.keras.layers.MaxPooling2D(2,2),
                        tf.keras.layers.Flatten(),
                        tf.keras.layers.Dense(512,activation = 'relu'),
                        tf.keras.layers.Dense(64,activation = 'relu'),
                        tf.keras.layers.Dense(5,activation = 'softmax'),
                        
    ]
)