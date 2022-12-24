import os.path

from setup import *
from video import extract_frames, to_video, get_frames
from text_art import text_art


def main() -> None:
    # file_name = input("Enter name of file: ")
    file_name = input_filename
    extract_frames(file_name)
    frames = get_frames(frames_path)
    for image in frames:
        text_art(image)

    to_video(text_art_frames_path,get_frames(text_art_frames_path))


if __name__ == '__main__':
    main()
