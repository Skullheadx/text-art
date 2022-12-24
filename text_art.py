from setup import *


def text_art(path):  # 600, 800
    image = cv2.imread(os.path.join(frames_path, path), 0)
    """
alpha 1  beta 0      --> no change  
0 < alpha < 1        --> lower contrast  
alpha > 1            --> higher contrast  
-127 < beta < +127   --> good range for brightness values
    """
    # alpha =2
    # beta = 127
    # image = alpha*image + beta

    width, height = np.array(image).shape
    new_image = np.zeros((width, height), np.uint8)
    # print(width, height, new_image.shape)

    # density = "Ñ@#W$9876543210?!abc;:+=-,._       "
    density = '     .:-i|=+%O#@'
    # density = density[::-1]
    density_length = len(density)

    font = cv2.FONT_HERSHEY_COMPLEX_SMALL

    """
    density = '     .:-i|=+%O#@'
    scale = 10
    font_size = 1
    thick = 1
    
    density = '     .:-i|=+%O#@'
    scale = 20
    font_size =1
    thick = 3
    """

    scale = 10
    font_size = 1
    thick = 1
    # cv2.rectangle(image, (0,0), (height,width), BLACK, -1)
    # cv2.imwrite(os.path.join(text_art_frames_path, path), image)

    # line = ""
    for index, i in np.ndenumerate(image):
        y, x = index
        if (x % scale) or (y % scale):
            continue
        # if (x+y) % 25 != 0:
        #     continue
        # for k in np.nditer(i):

        density_index = math.floor(find_index(image[index], 0, 255, 0, density_length - 1))
        text = density[density_index]
        font_color = (255, 255, 255, int(image[index]))  #
        # line += text

        # (text_width, text_height) = cv2.getTextSize(text, font, font_size, thick)[0]
        # text_height += y * scale
        cv2.putText(new_image, text, (x, y), font, font_size, font_color, thick, cv2.LINE_AA)

        # if y == 0 and x > 0:
        #     line += '\n'
        #     pass

    # print(line)

    # image[-text_height:,:] = cv2.bitwise_or(image[-text_height:,:], mask)
    #
    cv2.imwrite(os.path.join(text_art_frames_path, path), new_image)
    # cv2.imshow('Grayscale Image', new_image)
    # cv2.waitKey(0)
    return path
