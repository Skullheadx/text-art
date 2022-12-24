import cv2
import os
import numpy as np
import math
from moviepy.editor import *

frames_path = "frames/"
text_art_frames_path = "text_art_frames/"
text_art_txts_path = "text_art_txts/"
input_path = "input/"
output_path = "output/"

is_video = True

filename = "Rick Astley - Never Gonna Give You Up (Official Music Video) (online-video-cutter.com).mp4"

input_filename = os.path.join(input_path, filename)
output_filename = os.path.join(output_path, filename)
output_filename_no_audio = os.path.join(output_path, "no audio " + filename)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# density = "Ñ@#W$9876543210?!abc;:+=-,._       "
density = '     .:-i|=+%O#@'
# density = density[::-1]
density_length = len(density)

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
scale = 10
font_size = 1
thick = 1

# scale = 10
# font_size = 1
# thick = 1


def get_number(filename: str):
    return int(filename[5:-4])


def find_index(num, min_num, max_num, min_range, max_range):
    n = num / (max_num - min_num + 1)
    return (max_range - min_range + 1) * n + min_range
