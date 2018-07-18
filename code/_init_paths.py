import os.path as osp
import sys

def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)

# Add caffe to PYTHONPATH
caffe_path = osp.join('../caffe-master', 'python')
print caffe_path
add_path(caffe_path)
