#!/bin/bash

#based on https://devtalk.nvidia.com/default/topic/1042035/installing-opencv4-on-xavier/

WHEREAMI=$(pwd)
source scripts/jetson_variables.sh
sudo apt-get install -y build-essential \
    cmake \
    unzip \
    pkg-config \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libgtk-3-dev \
    libatlas-base-dev \
    gfortran \
    python3-dev \
    python3-venv


git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git

python3 -m venv opencv4
source opencv4/bin/activate
pip install wheel
pip install numpy
cd opencv && mkdir -p build && cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_EXTRA_MODULES_PATH=$WHEREAMI'/opencv_contrib/modules' \
    -D PYTHON_EXECUTABLE=$WHEREAMI'/opencv4/bin/python' \
    -D BUILD_EXAMPLES=ON ..

make -j6
sudo make install
sudo ldconfig
cd $WHEREAMI'/opencv4/lib/python3.6/site-packages'
ln -s /usr/local/lib/python3.6/site-packages/cv2.cpython-36m-aarch64-linux-gnu.so cv2.so