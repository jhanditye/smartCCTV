
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


### :blossom: Improved change detection with Gaussian Mixture Models
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
