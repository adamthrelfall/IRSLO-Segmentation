# IRSLO vessel segmentation using PyTorch
## Introduction:
This code is designed to segment retinal infra-red scanning laser ophthalmoscope (IRSLO) images into their respective vessel maps.


## Installation:
###For everyone:
Install Anaconda on your device (or any other python package manager of your choice, we recommend either Anaconda or Mamba).
If on Windows, open an `Anaconda Powershell Prompt` from the start menu. If you are on a Unix system, open the terminal and type `conda` to activate anaconda.
Navigate to the folder that the repository was cloned into, using the command `cd /path/to/directory` (this can usually be copied and pasted from the address bar of Windows file explorer or the relevant Unix equivalent).
 - Double check the installation using the command `ls *.yml` - you should see `environment.yml` and `environment_cpu.yml` if you are in the correct environment
### If you have an NVidia GPU:
Create an environment in conda using the `environment.yml` file in this directory, using the command `conda create SLO_seg_env -f environment.yml`.
### If you do not have an Nvidia GPU:
Create an environment in conda using the `environment_cpu.yml` file in this directory, using the command `conda create SLO_seg_env -f environment_cpu.yml`.

## Usage:
Change directory to the relevant folder using the command above (`cd /path/to/directory`).
Make sure that your environment is active with the command `conda activate SLO_seg_env`. The line you see in the terminal should start with `(SLO_seg_env)`.
Put images into the `SLO` folder.
Use the command `jupyter notebook`, which will open a python instance that can be used to run the file.
Double-click the file  `segment_images.ipynb` to open it.
Follow the instructions in the segment_images.ipynb and run the relevant cells in that notebook, using either the shortcut `Shit-Enter` or the button in the top right corner.
Your images will be generated and saved in the folder "SLO_out" in .png format.


## Limitations:
 - This segmentation method is recommended for images from one device (the Heidelberg (R) Spectralis OCT) in .tif format. It has been tested on OD-centred (resolution 1536x1536 pixels) and macula-centred (resolution 768x768 pixels). Other resolutions, image formats (particularly those with lossy compression) and imaging devices may lead to variable results. It has been tested with JPEG compression and appears to work fine with medium- or good-quality compression, but your mileage may vary.
 - It is recommended to get a baseline segmentation time for multiple devices before running large batches (e.g. some higher-end CPUs perform segmentation faster than low-end GPUs).

## Permissions

This software is provided under MIT license and can be used, edited and redistributed for any purpose. We provide this software "as-is", with no warranty of any kind, and are not responsible for any damages or liability encountered through its use.

## Citation

In the event that this is used for published research, please cite [placeholder].