#!/usr/bin/env python

# --------------------------------------------------------
# This is the code for paper: 
# Contour Knowledge Transfer for Salient Object Detection (ECCV18)
#
# Written by Fan Yang
# --------------------------------------------------------

"""
See README.md for installation instructions before running.
"""

import _init_paths
from utils.timer import Timer
import numpy as np
from scipy.misc import imresize
import scipy.io as sio
import caffe, os, sys, cv2
import argparse
from utils.blob import im_list_to_blob

PIXEL_MEANS = np.array([[[104.00698793, 116.66876762, 122.67891434]]])

def _get_image_blob(im,TEST_MAX_SIZE):
    """Converts an image into a network input.

    Arguments:
        im (ndarray): a color image in BGR order

    Returns:
        blob (ndarray): a data blob holding an image
    """
    im_orig = im;
    im_shape = im_orig.shape
    processed_ims = []

    im = cv2.resize(im, (TEST_MAX_SIZE, TEST_MAX_SIZE))

    # substract the color mean
    im = im.astype(np.float32, copy=True)
    im -= PIXEL_MEANS

    processed_ims.append(im)

    # Create a blob to hold the input images
    blob = im_list_to_blob(processed_ims)

    return blob, im_shape

def _get_c2s_map(probmap, im_shape):
    """Convert network output to contour maps."""
     
    probmap = np.squeeze(probmap) 
    height = im_shape[0]
    width = im_shape[1]
    probmap = cv2.resize(probmap, (im_shape[1], im_shape[0])) 

    return probmap

def c2snet_detection(net, im):
    timer = Timer()
    timer.tic()

    # Convert image to network blobs
    blobs = {'data': None}
    blobs['data'], im_shape = _get_image_blob(im,224) 
    blobs_out = net.forward(data=blobs['data'].astype(np.float32, copy=False))
    probmap = blobs_out['saliencymap']
    contourrmap = blobs_out['probmap']   
    # Convert network output to image
    probmap = _get_c2s_map(probmap, im_shape)
    contourrmap = _get_c2s_map(contourrmap, im_shape)
    timer.toc()
    print ('Detection took {:.3f}s').format(timer.total_time)
    
    return probmap, contourrmap

if __name__ == '__main__':

    prototxt = 'models/C2SNet_deploy.prototxt'
    caffemodel = 'models/C2SNet_30K.caffemodel'

    if not os.path.isfile(caffemodel):
        raise IOError(('{:s} not found.\n').format(caffemodel))

    # GPU Setting
    caffe.set_mode_gpu()
    caffe.set_device(0)

    net = caffe.Net(prototxt, caffemodel,caffe.TEST)
    print 'Net is initialized.\n'

    print '\n\nLoaded network {:s}'.format(caffemodel)
    dataset_dir='images'
    list_file=os.listdir(dataset_dir)
    for name in list_file:
    	print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    	print 'Infer for {}'.format(name)
        # Load the test image
        name = name[:-4]
        im_file = os.path.join(dataset_dir, name + '.jpg')
        im = cv2.imread(im_file)
	# Run Saliency Branch inference
    	salmap, contourmap = c2snet_detection(net, im)
	salmap=(salmap-salmap.min())/(salmap.max()-salmap.min())
    	res_file = os.path.join('res', name + '_c2s.png')
	cv2.imwrite(res_file, (255*salmap).astype(np.uint8, copy=True))
        # Run Saliency Branch inference
	#contourmap=(contourmap-contourmap.min())/(contourmap.max()-contourmap.min())
        #contour_svfile = os.path.join('res', name + '_c.png')
	#cv2.imwrite(contour_svfile, (255*contourmap).astype(np.uint8, copy=True))
