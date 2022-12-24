from setup import *


def extract_frames(path: str) -> None:
    # Clear old frames
    for root, dirs, files in os.walk(frames_path):
        for file in files:
            os.remove(os.path.join(root, file))

    # Get input video
    video = cv2.VideoCapture(path)

    current_frame = 0
    while True:
        ret, image = video.read()
        # Save each frame
        if ret != 1:
            break
        cv2.imwrite(os.path.join(frames_path, f"frame{current_frame}.png"), image)
        current_frame += 1
    video.release()
    cv2.destroyAllWindows()


def to_video(frames: list) -> None:
    height, width, layers = cv2.imread(os.path.join(frames_path,frames[0])).shape
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    writer = cv2.VideoWriter(output_filename, fourcc, 33, (width, height))
    for frame in frames:
        writer.write(cv2.imread(os.path.join(frames_path,frame)))

    cv2.destroyAllWindows()
    writer.release()

def get_frames():
    frames = []
    for root, dirs, files in os.walk(frames_path):
        for file in files:
            frames.append(file)
    frames.sort(key=get_number)
    return frames
