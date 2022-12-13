
To recruiters:
:construction_worker: This README is still under construction, so for now it might be best to look at the smartCCTV noteboook. :construction_worker:

:construction: You have been warned! :construction:

## Table of contents

- [Overview](#overview)
  - [:duck: Intro](#intro)
  - [:seedling: Naive Change Detection](#naive-change-detection)
  - [:blossom: Improved change detection with Gaussian Mixture Models](#improved-change-detection-with-gaussian-mixture-models)
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

Additionally, we can make sure that our dilation and erosion are completely useful, we can make attempt to detect connected components. This would ensure for example that if we had a scene with a tree as a background on a windy day, the entire tree is recognised as one object instead of focusing on individual moving leaves.


Although this is quite, good dilation and erosion don't allow us to capture our intuitive idea of a background. For exmaple, if someone moves into a video and then stay still, they should be eventually be considered a part of the background. Okay, now you can move to the next chapter. 

### :blossom: Improved change detection with Gaussian Mixture Models

The motivating question for this section is: "What is the background?" Intuitively, most pixels are background pixels most of the time. When some change occurs, if it stays at a some pixels, then that change has actually become part of the background.  

Now, if we were to plot a histogram of the number of pixels at a certain intensity, the background pixels will be quite stable. 


<p align="center">
  <img src="data\readme_images\gaussianmodalmixture" alt="A connect four game in action with colours yellow and red" width="80%"/>
</p>

<p align="center">
  <img src="data\readme_images\gaussianmodalmixture2" alt="A connect four game in action with colours yellow and red" width="80%"/>
</p>


Looking at the examples above, we can see that we can fit some mixture of Gaussians to the histogram and thus determine a Gaussian mixture model for the whole distribution.

How does this help us?

Well, firstly each of the Gaussians in the mixture of Gaussians has some weighting $\omega$ and standard deviation $\sigma$ that contributes to the Gaussian Mixture Model. 

Our intuitive idea that most pixels are in the background most of the time corresponds to looking for the Gaussians with large $\omega$ (large blocks of near identical pixels) and small $\sigma$ (very small variation in the intensity of our pixel block). 

Therefore, given some pixel and some GMM over a time period, we can classify the pixel into a background pixel based on whether its 'best' Gaussian has large or small $\omega/\sigma$.

Clearly, there is a bit more to be discussed here but the intuitive idea is arguably more important. 

### :evergreen_tree: Connected Component Analysis

## My process

### Built with

- Python (and ofcourse the OpenCV library)

### What I learnt

1. I learnt that the application of Gaussian Mixture Models in change detection can be extremely useful. The key intuitive idea here was that we want the 'background' to be whatever stays at the same position for some extended amount of time. This allows for the background to be updated as different objects remain in frame.
2. I learnt about the mathematical basis of object tracking using optical flow. The limited assumptions about constant brightness and linearity prove to be powerful and useful assumptions. 

### Continued development

1. There are a few more things I would like to do with this project. For example, at present, we don't make use of the detected changes. We could make use of the detected changes to form appropriate bounding boxes to track any consistent changes. 

#### To-do
- Use action labelling CV library to label changes
- Put conditions in for a snippet of video to be saved and sent off 

