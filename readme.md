# IRSLO vessel segmentation using PyTorch
## Introduction:
This code is designed to segment retinal infra-red scanning laser ophthalmoscope (IRSLO) images into their respective vessel maps.


## Installation:
Install Anaconda on your device (or any other python package manager of your choice, we recommend either Anaconda or Mamba)
Create an environment in conda (or mamba if that is your preference) using the `environment.yml` file in this directory, using the command `conda create -n SLO_segmentation_env -f environment.yml` in an Anaconda terminal.


## Usage:
Put images into the "SLO" folder
Follow the instructions in the segment_images.ipynb and run the relevant cells in that notebook
Your images will be in the folder "SLO_out" in .png format.


## Limitations:
 - This segmentation method is recommended for images from one device (the Heidelberg (R) Spectralis OCT) in .tif format. It has been tested on OD-centred (resolution 1536x1536 pixels) and macula-centred (resolution 768x768 pixels). Other resolutions, image formats (particularly those with lossy compression) and imaging devices may lead to variable results. It has been tested with JPEG compression and appears to work fine with medium- or good-quality compression, but your mileage may vary.
 - It is recommended to get a baseline segmentation time for multiple devices before running large batches (e.g. some higher-end CPUs perform segmentation faster than low-end GPUs).

## Permissions

This software is provided under MIT license and can be used, edited and redistributed for any purpose. We provide this software "as-is", with no warranty of any kind, and are not responsible for any damages or liability encountered through its use.

## Citation

In the event that this is used for published research, please cite [placeholder].