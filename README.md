## Contour Knowledge Transfer for Salient Object Detection

by Xin Li, Fan Yang, Hong Cheng, Wei Liu and Dinggang Shen

### Introduction

This repository is for '[Contour Knowledge Transfer for Salient ObjectDetection]'.
### Installation

For installation, please follow the instructions of [Caffe](https://github.com/BVLC/caffe).

The code has been tested successfully on Ubuntu 14.04 with CUDA 8.0.

### Usage

1. Clone the repository:

   ```shell
   git clone https://github.com/lixin666/C2SNet.git
   ```

2. Build Caffe and pycaffe:

   ```shell
   cd caffe-master
   cp Makefile.config
   vim Makefile.config
   make -j8 && make pycaffe
   ```
ps: You should uncomment 'WITH_PYTHON_LAYER := 1' in Makefile.config before compiling.


3. Test:

   - Test code is in folder 'test'.
   - Download trained models and put them in folder 'test/models':
     - MSCNet.caffemodel: [BaiduYun](https://pan.baidu.com/s/1eSfaDto) or [GoogleDrive](https://drive.google.com/open?id=1wb71oU49G3gyor7vF1qDgPq0ePCFYHKG)
   - Put the test images in folder 'images', and run
   
   ```shell
   python test.py
   ```
   -After that, the results will be genrated in folder 'results'.
### Citation
If MSCNet is useful for your research, please consider citing:

    @inproceedings{li2017mscnet,
      author = {Xin Li and Fan Yang and Hong Cheng 
                and Junyu Chen and Leiting Chen},
      title = {Multi-Scale Cascade Network for Salient Object Detection},
      booktitle = {ACM MM},
      year = {2017}
    }

### Question
Please contact 'fanyang_uestc@hotmail.com'
