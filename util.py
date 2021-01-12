import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import keras
import seaborn as sns
import pickle
import random
import sys
import time
import os
from os.path import isfile
from PIL import Image as pil_image

fig = plt.figure(figsize=(8, 8), dpi=100, facecolor='w', edgecolor='k')
train_imgs = os.listdir("C:/Users/chaas/Wildlife-Identification/whale-data/train")
for idx, img in enumerate(np.random.choice(train_imgs, 12)):
    ax = fig.add_subplot(4, 20//5, idx+1, xticks=[], yticks=[])
    im = pil_image.open("C:/Users/chaas/Wildlife-Identification/whale-data/train" + img)
    plt.imshow(im)
    
#src = 
#video_inp = '../data/' + src + '.MP4'
#img_out = '../data/img/' + src + '.jpg'