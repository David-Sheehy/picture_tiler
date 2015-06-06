from PIL import Image
import math
import sys


# handle arguments
pics = sys.argv[1:]

# create output image
sec_size = 32                   # The created image will be divided into
                                # 32 x 32s
oi = Image.new("RGB",(320,320))


# draw each picture to the output image

# determine where to place the image



oi.save("output.png")
# save the image
