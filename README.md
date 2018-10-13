# OpenCV4 XAVIER
Build and install OpenCV4 for the NVIDIA Jetson XAVIER

These scripts build OpenCV version 4 pre for the NVIDIA Jetson XAVIER Development Kit. Please see Releases/Tags for earlier versions.

# Install 
To install run the following commands:

> ./buildOpenCV4.sh

This may take a while ...

Afterwards test your install

Activate your opencv-python environment out of the same folder:
> source opencv4/bin/activate  

Check OpenCV version
> python  
> import cv2  
> cv2.__version__  

You should see '4.0.0-pre'

# Run
Activate your opencv-python environment out of the same folder:
> source opencv4/bin/activate  

Run the example:
> ./Examples/cannyDetection.py 


## Notes
This setup will create a virtual python environment called 'opencv4' in your execution dir.
OpenCV4 will be pulled from git, build into OpenCVXAVIER/opencv/build and installed into /usr/local/share/opencv4/
The OpenCV install directory will be linked to this particular virtual environment 


## References

Most of this information is derived from:

https://devtalk.nvidia.com/default/topic/1042035/installing-opencv4-on-xavier/

https://github.com/jetsonhacks/buildOpenCVTX2

## Release Notes
Oct 13th 2018
* L4T 31.0.2
* CUDA 10.0
* OpenCV 4 pre



## License
MIT License

Copyright (c) 2017-2018 Jetsonhacks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
 
