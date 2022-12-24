# text-art

Free for anyone to use to create their own text art creations.
If you choose to, pleasse credit the link to this repo.

DEPENDENCIES:
opencv-python
os
numpy
math
moviepy

---------------------------------------------------------------------------------------------------------
HOW TO USE:
1. Create folders in same folder as main.py:
input
output
frames
text_art_frames
text_art_txts

2. Place the .mp4 video you want to turn into text into the input folder.

3. Go to setup.py and edit the value of filename to the name of the file you want to be turned into text art.
filename = "FILENAMEHERE"

4. Run main.py with python and wait until the output appears in the output folder.
 
5. Enjoy your text art video!

---------------------------------------------------------------------------------------------------------
If you wish for higher quality or different text sizes, change the scale value in setup.py.

scale = 10

For example, setting the scale to 10 will mean that every 10th pixel will be turned into text. 
The smaller the value, the more pixels will be turned into text.
However, this may take more time to generate the video. Feel free to also change the density and font_size for interesting effects.
