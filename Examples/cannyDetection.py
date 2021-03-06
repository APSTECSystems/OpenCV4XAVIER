#!/usr/bin/env python
# MIT License

# Copyright (c) 2017-18 Jetsonhacks

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import argparse
import cv2
import numpy as np


def parse_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_device", dest="video_device",
                        help="Video device # of USB webcam (/dev/video?) [0]",
                        default=0, type=int)
    arguments = parser.parse_args()
    return arguments


# Open an external usb camera /dev/videoX
def open_camera_device(device_number):
    return cv2.VideoCapture(device_number)


def read_cam(video_capture):
    if video_capture.isOpened():
        video_capture.set(cv2.CAP_PROP_FPS,30)
        windowName = "CannyDemo"
        cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(windowName, 1280, 720)
        cv2.moveWindow(windowName, 0, 0)
        cv2.setWindowTitle(windowName, "Canny Edge Detection")
        showWindow = 3  # Show all stages
        showHelp = True
        font = cv2.FONT_HERSHEY_PLAIN
        helpText = "'Esc' to Quit, '1' for Camera Feed, '2' for Canny Detection, '3' for All Stages. '4' to hide help "
        helpText2 = "'5' to lower edge threshold, '6' to raise edge threshold, '7' to toggle fullscreen"
        edgeThreshold = 40
        showFullScreen = False
        while True:



            ret_val, frame = video_capture.read()

            frame = cv2.resize(frame, (640, 360))
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(hsv, (7, 7), 1.5 )
            edges = cv2.Canny(blur, 0, edgeThreshold)
            if showWindow == 3:  # Need to show the 4 stages
                # Composite the 2x2 window
                # Feed from the camera is RGB, the others gray
                # To composite, convert gray images to color. 
                # All images must be of the same type to display in a window
                #frameRs = cv2.resize(frame, (640, 360))
                #hsvRs = cv2.resize(hsv, (640, 360))
                vidBuf = np.concatenate((frame, cv2.cvtColor(hsv, cv2.COLOR_GRAY2BGR)), axis=1)
                #blurRs = cv2.resize(blur, (640, 360))
                #edgesRs = cv2.resize(edges, (640, 360))
                vidBuf1 = np.concatenate(
                    (cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR), cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)), axis=1)
                vidBuf = np.concatenate((vidBuf, vidBuf1), axis=0)

            if showWindow == 1:  # Show Camera Frame
                displayBuf = frame
            elif showWindow == 2:  # Show Canny Edge Detection
                displayBuf = edges
            elif showWindow == 3:  # Show All Stages
                displayBuf = vidBuf

            DebugText = "OpenCV Version: " + str(cv2.__version__) + " Edge Threshold: " + str(edgeThreshold)
            if showHelp == True:
                cv2.putText(displayBuf, helpText, (11, 20), font, 1.0, (32, 32, 32), 4, cv2.LINE_AA)
                cv2.putText(displayBuf, helpText, (10, 20), font, 1.0, (240, 240, 240), 1, cv2.LINE_AA)

                cv2.putText(displayBuf, helpText2, (11, 50), font, 1.0, (32, 32, 32), 4, cv2.LINE_AA)
                cv2.putText(displayBuf, helpText2, (10, 50), font, 1.0, (240, 240, 240), 1, cv2.LINE_AA)

                cv2.putText(displayBuf, DebugText, (10, 80), font, 1.0, (32, 32, 32), 4, cv2.LINE_AA)
                cv2.putText(displayBuf, DebugText, (11, 80), font, 1.0, (240, 240, 240), 1, cv2.LINE_AA)

            cv2.imshow(windowName, displayBuf)
            key = cv2.waitKey(10)
            if key == 27:  # Check for ESC key
                cv2.destroyAllWindows()
                break
            elif key == 49:  # 1 key, show frame
                cv2.setWindowTitle(windowName, "Camera Feed")
                showWindow = 1
            elif key == 50:  # 2 key, show Canny
                cv2.setWindowTitle(windowName, "Canny Edge Detection")
                showWindow = 2
            elif key == 51:  # 3 key, show Stages
                cv2.setWindowTitle(windowName, "Camera, Gray scale, Gaussian Blur, Canny Edge Detection")
                showWindow = 3
            elif key == 52:  # 4 key, toggle help
                showHelp = not showHelp
            elif key == 53:  # 5 , lower canny edge threshold
                edgeThreshold = max(0, edgeThreshold - 10)
                print('Canny Edge Threshold Maximum: ', edgeThreshold)
            elif key == 54:  # 6 , raise canny edge threshold
                edgeThreshold = edgeThreshold + 10
                print('Canny Edge Threshold Maximum: ', edgeThreshold)
            elif key == 55:  # 7, Toggle fullscreen; This is the F3 key on this particular keyboard
                # Toggle full screen mode
                if showFullScreen == False:
                    cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                else:
                    cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
                showFullScreen = not showFullScreen
            if cv2.getWindowProperty(windowName, 0) < 0:  # Check to see if the user closed the window
                # This will fail if the user closed the window; Nasties get printed to the console
                print("closed")
                break



    else:
        print("camera open failed")


if __name__ == '__main__':
    arguments = parse_cli_args()
    print("Called with args:")
    print(arguments)
    print("OpenCV version: {}".format(cv2.__version__))
    print("Device Number:", arguments.video_device)
    video_capture = open_camera_device(arguments.video_device)
    read_cam(video_capture)
    video_capture.release()
    cv2.destroyAllWindows()
