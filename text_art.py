from setup import *


def add_text(grayscale: int, x: int, y: int, new_image: np.ndarray) -> None:
    density_index = math.floor(find_index(grayscale, 0, 255, 0, density_length - 1))
    text = density[density_index]
    font_color = (255, 255, 255, int(grayscale))

    cv2.putText(new_image, text, (x, y), font, font_size, font_color, thick, cv2.LINE_AA)


def text_art_video(path: str) -> str:
    image = cv2.imread(os.path.join(frames_path, path), 0)
    width, height = np.array(image).shape
    new_image = np.zeros((width, height), np.uint8)

    for index, i in np.ndenumerate(image):
        y, x = index
        if (x % scale) or (y % scale):
            continue
        add_text(image[index], x, y, new_image)

    cv2.imwrite(os.path.join(text_art_frames_path, path), new_image)
    return path


def text_art_image(path: str) -> None:
    image = cv2.imread(os.path.join(frames_path, path), 0)  # grayscale image
    line = ""
    for index, i in np.ndenumerate(image):
        y, x = index
        if (x % scale) or (y % scale):
            continue

        if y == 0 and x > 0:
            line += '\n'

    # Write to txt file
    with open(os.path.join(text_art_txts_path,f"frame{get_number(path)}.txt"), "w") as f:
        f.write(line)
