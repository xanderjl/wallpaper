#!/usr/bin/env python3

import os
import time
import ctypes
import urllib.request
from pathlib import Path

username = os.getlogin()
SPI_SETDESKWALLPAPER = 20
what_you_want = input('Input a theme (i.e. nature): ')
wallpaper = 'https://source.unsplash.com/2560x1440/?' + what_you_want
filepath = os.getcwd() + '\\wallpaper.jpg'


def download_image(url):
    full_name = 'wallpaper.jpg'
    urllib.request.urlretrieve(url, full_name)


download_image(wallpaper) # download image from unsplash
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0 ,filepath, 0) # set desktop background to unsplash image
time.sleep(1) # wait 1 second
os.remove(filepath) # delete image
