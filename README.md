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
   cp Makefile.config.example Makefile.config
   vim Makefile.config
   make -j8 && make pycaffe
   ```
ps: You should uncomment 'WITH_PYTHON_LAYER := 1' in Makefile.config before compiling.


3. Test:

   - Test code is in folder 'code'.
    - We provide two models trained with 10K and 30K training images. Download trained models and put them in folder 'code/models':
     - C2SNet10K.caffemodel: [BaiduYun]() or [GoogleDrive](https://drive.google.com/open?id=17j6pw_ML1SUN52LA50lpzWifPjKAnidJ)
     - C2SNet30K.caffemodel: [BaiduYun]() or [GoogleDrive](https://drive.google.com/open?id=1zflZLDciS5_Ttljenia_nkkBOZBM7VBs)
   - Put the test images in folder 'images', and run
   
   ```shell
   python run_demo.py
   ```
   -After that, the results will be genrated in folder 'res'.
### Citation
If C2SNet is useful for your research, please consider citing:

    @inproceedings{xin2018c2s,
      author = {Xin Li, Fan Yang, Hong Cheng, Wei Liu and Dinggang Shen},
      title = {Contour Knowledge Transfer for Salient Object Detection},
      booktitle = {ECCV},
      year = {2018}
    }

### Question
Please contact 'fanyang_uestc@hotmail.com'
