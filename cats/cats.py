# Built with python 3, dependencies installed with pip 
# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

# library to work with arrays 
# https://numpy.org/
import numpy as np

# library to interact with the operating system
import os

# library to generate random integer values
from random import seed
from random import randint

# gets path to be used in image creation mechanism, using os
dirname = os.path.dirname(__file__)

# sets final image dimensions as 480x480 pixels
# the original 24x24 pixel image will be expanded to these dimensions
dimensions = 480, 480

# tells how many times to iterate through the following mechanism
# which equals the number of cats
# e.g. 
# for x in range(0-200) 
# would generate 201 cats numbered 0-200
for x in range(0, 1000):

    # using ETH block number as starting random number seed
    b=11981207
    seed(x+b)

    #head color - randomly generate each number in an RGB color
    hd = (randint(0, 256), randint(0, 256), randint(0, 256))
    es = (randint(0, 256), randint(0, 256), randint(0, 256))
    c=randint(0,500)
    seed(c)

    #throat color - same as head color
    th = (randint(0, 256), randint(0, 256), randint(0, 256))
    d = randint(0,1000)
    seed(d)

    #eye "white" color
    # if random number between 1-1000 is 47 or less - Crazy Eyes!
    if d > 47:
        # normal eyes are always the same color
        ew = (240,248,255)
        ey = (0, 0, 0)
    else:
        # crazy eyes have the same (154, 0, 0) pupil and a random 'eye white' color
        ew = (randint(0, 256), randint(0, 256), randint(0, 256))
       
        ey = (0, 0, 0)
    e = randint(0,1000)
    seed(e)

    # beak color
    f = randint(0, 500)
    if f > 500:
        # if random number is 501-1000 >> grey beak
        bk = (152, 152, 152)
    elif 500 >= f > 47:
        # 48-500 >> gold beak
        bk = (204, 172, 0)
    elif 47 >= f > 7:
        # 8 >> 47 >> red beak
        bk = (204, 0, 0)
       
    else:
        # random number is 7 or less >> black beak
        bk = (0, 0, 0) 

    # background color
    bg = (238, 238, 238)
    # outline color
    ol = (0, 0, 0)
    rd = (246, 2, 12)
    rn = (randint(0, 256), randint(0, 256), randint(0, 256))
       
    
#cat
    pixel_cat1 = [
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ew, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ew, ew, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, ew, ew, ew, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, hd, hd, ol, ol, ol, ol, ol, ol, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bg, bg, bg, ol, ol, ol, hd, hd, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bg, bg, bg, ol, ol, ol, hd, hd, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, es, es, es, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, ey, ey, ey, hd, hd, ey, hd, hd, hd, hd, hd, ol, ol, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, ey, hd, hd, hd, ey, ey, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bk, bk, bk, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bk, bk, bk, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]

]
    cats1 = [
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  ol,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  ol,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  th,  ol,  bg,  bg,  bg,  bg,  ol,  hd,  th,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  th,  th,  ol,  ol,  ol,  ol,  hd,  th,  th,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  th,  th,  hd,  hd,  hd,  hd,  hd,  th,  th,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  th,  ol,  hd,  hd,  hd,  th,  ol,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  bg,  ol,  hd,  hd,  hd,  bg,  ol,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  ol,  ol,  ol,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  bk,  bk,  hd,  hd,  hd,  ol,  ol,  ol,  ol,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  bk,  bk,  hd,  hd,  ol,  ol,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  ey,  hd,  hd,  hd,  ol,  ol,  ol,  ol,  ol,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  ey,  hd,  ey,  hd,  ey,  hd,  hd,  hd,  ol,  bg,  ol,  ol,  ol,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  ey,  ey,  hd,  ey,  ey,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg]]

    pixel_cat2 = [
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],     
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, bk, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, bk, bk, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, bk, bk, bk, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, hd, hd, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bg, bg, bg, ol, ol, ol, hd, hd, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bg, bg, bg, ol, ol, ol, hd, hd, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bk, bk, bk, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, bk, bk, bk, hd, hd, hd, ol, ol, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, hd, hd, ey, hd, hd, hd, hd, hd, ey, ey, ey, ey, ey, hd, hd, hd, hd, ey, hd, hd, hd, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, ey, ey, ey, ey, ey, hd, hd, hd, hd, ey, ey, ey, ey, ey, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, th, th, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, th, th, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg] ]

    cats2 = [
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg],    
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg],    
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg],    
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  ol,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  ol,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  th,  ol,  bg,  bg,  bg,  bg,  ol,  hd,  th,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  th,  th,  ol,  ol,  ol,  ol,  hd,  th,  th,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  th,  th,  hd,  hd,  hd,  hd,  hd,  th,  th,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  th,  ol,  hd,  hd,  hd,  th,  ol,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  bg,  ol,  hd,  hd,  hd,  bg,  ol,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, ol,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  bk,  bk,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  ol,  ol,  ol, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  ol,  hd,  hd,  hd,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  bk,  bk,  hd,  hd,  ol,  ol,  ol,  ol,  ol,  ol,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, ol,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  ol,  hd,  hd,  hd,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  ey,  hd,  hd,  hd,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ey,  hd,  ey,  hd,  ey,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  ol,  ol, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ey,  ey,  hd,  ey,  ey,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg]]

    pixel_cat3 = [
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, hd, hd, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bg, bg, bg, ol, ol, ol, hd, hd, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bg, bg, bg, ol, ol, ol, hd, hd, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bk, bk, bk, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, bk, bk, bk, hd, hd, hd, ol, ol, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, hd, hd, ey, hd, hd, hd, hd, hd, ey, ey, ey, ey, ey, hd, hd, hd, hd, ey, hd, hd, hd, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, ey, ey, ey, ey, ey, hd, hd, hd, hd, ey, ey, ey, ey, ey, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, th, th, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, th, th, th, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg] ]

    cats3 = [
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg],     
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  ol,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  ol,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  th,  ol,  bg,  bg,  bg,  bg,  ol,  hd,  th,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  th,  th,  ol,  ol,  ol,  ol,  hd,  th,  th,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  th,  th,  hd,  hd,  hd,  hd,  hd,  th,  th,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  th,  ol,  hd,  hd,  hd,  th,  ol,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  bg,  ol,  hd,  hd,  hd,  bg,  ol,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, ol,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  bk,  bk,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  ol,  ol,  ol, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  bk,  bk,  hd,  hd,  ol,  ol,  ol,  ol,  ol,  ol,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, ol,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  ey,  hd,  hd,  hd,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ey,  hd,  ey,  hd,  ey,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  ol,  ol, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  ey,  ey,  hd,  ey,  ey,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  ol,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  ol,  ol,  ol,  ol,  hd,  hd,  ol,  ol,  ol,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg]
    ]

    pixel_cat4 = [
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],     
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, ol, ol, rd, rd, rd, ol, ol, ol, ol, bg, ol, ol, ol, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, rd, rd, rd, rd, rd, rd, rd, rd, ol, ol, rd, rd, ol, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, ol, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, rd, rd, rd, rd, rd, rd, rd, rd, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, rd, rd, rd, rd, rd, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, rd, rd, rd, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, hd, hd, hd, ol, ol, ol, hd, hd, hd, ol, ol, ol, ol, ol, ol, hd, hd, ol, ol, ol, ol, ol, ol, hd, hd, hd, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, ol, ol, ol, hd, hd, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ol, ol, ol, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, es, es, es, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, ey, ey, ey, hd, hd, ey, hd, hd, hd, hd, hd, ol, ol, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, ey, hd, hd, hd, ey, ey, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bk, bk, bk, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bk, bk, bk, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]

 
]
    cats4 = [
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  ol,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  ol,  ol,  ol,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  th,  ol,  hd,  hd,  hd,  th,  ol,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  bg,  ol,  hd,  hd,  hd,  bg,  ol,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, ol,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  bk,  bk,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  ol,  ol,  ol, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  bk,  bk,  hd,  hd,  ol,  ol,  ol,  ol,  ol,  ol,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, ol,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  ey,  hd,  hd,  hd,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ey,  hd,  ey,  hd,  ey,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  ol,  ol, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  ey,  ey,  hd,  ey,  ey,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  ol,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  ol,  ol,  ol,  ol,  hd,  hd,  ol,  ol,  ol,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg] 
    ]

    pixel_cat5 = [


[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  ol,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  ol,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  bk,  ol,  bg,  bg,  bg,  bg,  ol,  hd,  bk,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  bk,  bk,  ol,  ol,  ol,  ol,  hd,  bk,  bk,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  bk,  bk,  hd,  hd,  hd,  hd,  hd,  bk,  bk,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  ol,  ol,  hd,  hd,  hd,  ol,  ol,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  bg,  ol,  hd,  hd,  hd,  bg,  ol,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  ol,  ol,  ol,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  rn,  rn,  hd,  hd,  hd,  ol,  ol,  ol,  ol,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  rn,  rn,  hd,  hd,  ol,  ol,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  ey,  hd,  hd,  hd,  ol,  ol,  ol,  ol,  ol,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  ey,  hd,  ey,  hd,  ey,  hd,  hd,  hd,  ol,  bg,  ol,  ol,  ol,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  ey,  ey,  hd,  ey,  ey,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg]]

    pixel_cat6 = [


[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ew, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ew, ew, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, ew, ew, ew, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],  
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, hd, hd, hd, ol, ol, ol, hd, hd, hd, ol, ol, ol, ol, ol, ol, hd, hd, ol, ol, ol, ol, ol, ol, hd, hd, hd, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, ol, ol, ol, hd, hd, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ol, ol, ol, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, es, es, es, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, ey, ey, ey, hd, hd, ey, hd, hd, hd, hd, hd, ol, ol, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, ey, hd, hd, hd, ey, ey, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bk, bk, bk, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bk, bk, bk, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]
    pixel_cat7 = [


[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ew, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ew, ew, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, ew, ew, ew, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, hd, hd, ol, ol, ol, ol, ol, ol, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, ol, ol, bg, bg, bg, ol, ol, ol, ol, ol, hd, ol, ol, ol, ol, ol, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, ol, ol, bg, bg, bg, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, es, es, es, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, ey, ey, ey, hd, hd, ey, hd, hd, hd, hd, hd, ol, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, ey, hd, hd, hd, ey, ey, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bk, bk, bk, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bk, bk, bk, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]]
    
    cats5 = [
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  ol,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  ol,  ol,  ol,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  th,  ol,  hd,  hd,  hd,  th,  ol,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  bg,  ol,  hd,  hd,  hd,  bg,  ol,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, ol,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  bk,  bk,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  ol,  ol,  ol, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  bk,  bk,  hd,  hd,  ol,  ol,  ol,  ol,  ol,  ol,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, ol,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  ol,  ol,  ol,  ol,  hd,  hd,  hd,  ey,  hd,  hd,  hd,  ol,  ol,  ol,  ol,  ol,  ol,  ol,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ey,  hd,  ey,  hd,  ey,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  ol,  ol, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  ey,  ey,  hd,  ey,  ey,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg,  bg,  bg,  bg,  ol,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  hd,  ol,  bg,  bg,  bg,  bg,  bg,  bg, bg, bg, bg, bg]
    ]

    cats6 = [

[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, ol, ol, rd, rd, rd, ol, ol, ol, ol, bg, ol, ol, ol, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, rd, rd, rd, rd, rd, rd, rd, rd, ol, ol, rd, rd, ol, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, ol, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, rd, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, rd, rd, rd, rd, rd, rd, rd, rd, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, rd, rd, rd, rd, rd, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, rd, rd, rd, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, hd, hd, ol, ol, ol, ol, ol, ol, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, ol, ol, bg, bg, bg, ol, ol, ol, ol, ol, hd, ol, ol, ol, ol, ol, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, ol, ol, bg, bg, bg, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, es, es, es, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, hd, hd, ey, ey, ey, hd, hd, ey, hd, hd, hd, hd, hd, ol, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ey, ey, hd, hd, hd, ey, ey, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bk, bk, bk, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], 
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, bk, bk, bk, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]]
    
    # choose which cat image to use
    seed(f)
    g = randint(0,1000)
    if g >= 1000:
        # if random number is 251 - 1000 >> pixel_cat1
        pixels = pixel_cat1
        p = "pixel_cat1"
    elif 1000 >= g > 950:
        # 101 - 250 >> pixel_cat2
        pixels = pixel_cat2
        p = "pixel_cat2"
    elif 950 >= g > 850:
        # 101 - 250 >> pixel_cat3
        pixels = pixel_cat3
        p = "pixel_cat3"
    elif 850 >= g > 750:
        # 101 - 250 >> pixel_cat4
        pixels = pixel_cat4
        p = "pixel_cat4"
    elif 750 >= g > 650:
        # 41 - 100 >> pixel_cat5
        pixels = pixel_cat5
        p = "pixel_cat5"
    elif 650 >= g > 550:
        # 6 - 40 >> pixel_cat6
        pixels = pixel_cat6
        p = "pixel_cat6"
    elif 550 >= g > 450:
        # 6 - 40 >> cats1
        pixels = cats1
        p = "cats1"
    elif 450 >= g > 350:
        # 6 - 40 >> cats2
        pixels = cats2
        p = "cats2"
    elif 350 >= g > 250:
         # 6 - 40 >> cats3
        pixels = cats3
        p = "cats3"
    elif 250 >= g > 150:
        # 6 - 40 >> cats4
        pixels = cats4
        p = "cats4"
    elif 150 >= g > 100:
        # 6 - 40 >> cats5
        pixels = cats5
        p = "cats5"
    elif 100 >= g > 50:
        # 6 - 40 >> cats6
        pixels = cats6
        p = "cats6"
    else:
        # if random number is 5 or less >> pixel_cat7!!
        pixels = pixel_cat7
        p = "pixel_cat7"
        
    # convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    # use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image = new_image.resize(dimensions, resample=0)
    imgname = dirname + '/cats_images/' + (str(x)) + '.png'
    new_image.save(imgname)
