import cv2
import os
import numpy as np
import math
from moviepy.editor import *

frames_path = "C:/Users/admon/Documents/GitHub/text-art/frames/"
text_art_frames_path = "C:/Users/admon/Documents/GitHub/text-art/text_art_frames/"
output_filename = "output/output.mp4"
input_filename = "input/Rick Astley - Never Gonna Give You Up (Official Music Video).mp4"

BLACK = (0,0,0)
WHITE = (255,255,255)


def get_number(filename:str):
    return int(filename[5:-4])
def find_index(num, min_num, max_num, min_range, max_range):
    n = num / (max_num - min_num + 1)
    return (max_range - min_range + 1) * n + min_range