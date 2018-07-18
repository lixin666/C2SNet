#!/usr/bin/env python
# Martin Kersner, martin@company100.com
# 2016/01/12

import numpy as np
from scipy.misc import imresize

def preprocess_image(img, img_sz):
  meanImg = np.array([104.00698793, 116.66876762, 122.67891434]) # order = bgr
  
  resized = imresize(img, (img_sz, img_sz), interp='bilinear')
  resized = resized[...,[2,1,0]] - meanImg # convert color channer rgb->bgr and subtract mean 
  preprocessed_img = resized.transpose((2, 0, 1))

  return preprocessed_img

