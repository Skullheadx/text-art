from setup import *
from text_art import text_art_video, text_art_image
from video import extract_frames, to_video, get_frames


def main(video=True) -> None:
    file_name = input_filename
    extract_frames(file_name)

    frames = get_frames(frames_path)
    if video:
        for path in frames:
            text_art_video(path)

        to_video(text_art_frames_path, get_frames(text_art_frames_path))
    else:
        for path in frames:
            text_art_image(path)


if __name__ == '__main__':
    main(video=is_video)
