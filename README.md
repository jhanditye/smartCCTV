
To recruiters:
:construction_worker: This README is still under construction, so for now it might be best to look at the smartCCTV noteboook. :construction_worker:

:construction: You have been warned! :construction:

## Table of contents

- [Overview](#overview)
  - [:duck: Intro](#intro)
  - [:seedling: Naive Change Detection](#naive-change-detection)
  - [:blossom: Improved change detection with Gaussian Mixture Models](#improved-change-detection-with-gaussian-mixture-models)
  - [:evergreen_tree: Connected Component Analysis](#connected-component-analysis)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learnt](#what-i-learnt)
  - [Continued development](#continued-development)
    - [To-do](#to-do)


## Overview

### :duck: Intro 

A computer vision project on creating all the key features of a smart CCTV system. The main focus of this project though will be on making sure that our method of change detection produces as clear results as possible. Tracking objects after detecting changes is reasonably manageable but the most important thing initially is clean the data and salvage as much useful information from each frame as possible.

### :seedling: Naive Change Detection

The most obvious method for change detection between two frames of the same dimensions is to simply substract the RGB values of each image at each pixel. The good thing is that we have atleast one solution now so we simply to optimise it. What are its faults?

The key assumption of this method which would make it work well is that the images have very small amounts of noise. This assumption is not likely to hold for general cameras and so it would be better to have a more robust method of detection. 

We can attempt reduce the levels of noise with simple image morphology techniques : namely erosion and dilation here.

Erosion works to remove isolated points whilst dilation works to fill gaps and bolden the outlines of images. Erosion tends to reduce the size of an object whilst dilation increase it. Performing these operations one after (referred to as closing and opening) has a good effect towards cleaning up images as it marks the outlines of shapes reasonably well and removes a large descent amount of background noise. Some good exmaples can be seen below:


<p align="center">
  <img src="https://user-images.githubusercontent.com/78427605/207094867-230df5df-0f44-48e4-a64e-0b2f6bb6a0f4.png" alt="A connect four game in action with colours yellow and red" width="80%"/>
</p>




Although this is quite, good dilation and erosion don't allow us to capture our intuitive idea of a background. For exmaple, if someone moves into a video and then stay still, they should be eventually be considered a part of the background. Okay, now you can move to the next chapter. 

### :blossom: Improved change detection with Gaussian Mixture Models

Given that we want to extract the difference the background and foreground 
### :evergreen_tree: Connected Component Analysis

## My process

### Built with

- Python (and ofcourse the OpenCV library)

### What I learnt

1. I learnt that the application of Gaussian Mixture Models in change detection can be extremely useful. The key intuitive idea here was that we want the 'background' to be whatever stays at the same position for some extended amount of time. This allows for the background to be updated as different objects remain in frame.
2. I learnt about the mathematical basis of object tracking using optical flow. The limited assumptions about constant brightness and linearity prove to be powerful and useful assumptions. 

### Continued development

1There are a few more things I would like to do with this project. For example, at present, we don't make use of the detected changes. We could make use of the detected changes to form appropriate bounding boxes to track any consistent changes. 

#### To-do
- Use action labelling CV library to label changes
- Put conditions in for a snippet of video to be saved and sent off 
