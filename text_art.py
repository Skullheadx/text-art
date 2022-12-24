from setup import *

def text_art(path): # 600, 800
    image = cv2.imread(os.path.join(frames_path,path))
    """
alpha 1  beta 0      --> no change  
0 < alpha < 1        --> lower contrast  
alpha > 1            --> higher contrast  
-127 < beta < +127   --> good range for brightness values
    """
    alpha = 2
    beta = 127
    image = alpha*image + beta
    scale = 3
    density = "Ñ@#W$9876543210?!abc;:+=-,._       "
    # density = '     .:-i|=+%O#@'
    # density = density[::-1]
    density_length = len(density)

    rows,cols,_ = image.shape
    output = []
    for i in range(0,rows,scale):
        line = ""
        for j in range(0,cols, scale):
            avg = np.average(image[i,j])
            avg = min(avg * 2, 255)
            density_index = math.floor(find_index(avg, 0, 255, 0, density_length - 1))
            line += density[density_index]
        output.append(line)
    cv2.rectangle(image, (0,0), (cols,rows), BLACK, -1)
    # cv2.imwrite(os.path.join(text_art_frames_path, path), image)

    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    font_size = 0.9
    thick = 1
    font_color = WHITE
    for i,text in enumerate(output[::-1]):
        (text_width, text_height) = cv2.getTextSize(text, font, font_size, thick)[0]
        text_height += i * scale
        mask = np.zeros((text_height, text_width), dtype=np.uint8)
        mask = cv2.putText(mask,text,(10,scale),font,font_size,font_color,thick,cv2.LINE_AA)
        mask = cv2.resize(mask, (image.shape[1], text_height))
        mask = cv2.merge((mask, mask, mask))
        if image[-text_height:, :, :].size == mask.size:
            image[-text_height:, :, :] = cv2.bitwise_or(image[-text_height:, :, :], mask)
        cv2.imwrite(os.path.join(text_art_frames_path, path), image)
    return path
