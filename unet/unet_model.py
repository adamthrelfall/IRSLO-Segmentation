""" Full assembly of the parts to form the complete network """

import torch.nn.functional as F

from .unet_parts import *


class UNet(nn.Module):
	def __init__(self, n_channels, n_classes, bilinear=True, kernel_size = 5, mc = 512):
		super(UNet, self).__init__()
		self.n_channels = n_channels
		self.n_classes = n_classes
		self.bilinear = bilinear

		self.inc = DoubleConv(n_channels, mc//16, kernel_size = kernel_size)
		self.down1 = Down(mc//16, mc//8, kernel_size = kernel_size)
		self.down2 = Down(mc//8, mc//4, kernel_size = kernel_size)
		self.down3 = Down(mc//4, mc//2, kernel_size = kernel_size)
		factor = 2 if bilinear else 1
		self.down4 = Down(mc//2, mc // factor, kernel_size = kernel_size)
		self.up1 = Up(mc, mc//2 // factor, bilinear, kernel_size = kernel_size)
		self.up2 = Up(mc//2, mc//4 // factor, bilinear, kernel_size = kernel_size)
		self.up3 = Up(mc//4, mc//8 // factor, bilinear, kernel_size = kernel_size)
		self.up4 = Up(mc//8, mc//16, bilinear, kernel_size = kernel_size)
		self.outc = OutConv(mc//16, n_classes)

	def forward(self, x):
		x1 = self.inc(x)
		x2 = self.down1(x1)
		x3 = self.down2(x2)
		x4 = self.down3(x3)
		x5 = self.down4(x4)
		x = self.up1(x5, x4)
		x = self.up2(x, x3)
		x = self.up3(x, x2)
		x = self.up4(x, x1)
		logits = self.outc(x)
		return logits
