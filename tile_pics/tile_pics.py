#! /usr/bin/env python3
from PIL import Image
import math
import argparse
import random

# various flags
VERBOSE = False

SHUFFLE = False
OUTPUT_PATH = "output.png"
OUTPUT_SIZE = (1920,1080)             
sec_size = 32                   # The created image will be divided into 32x32

def main(pics) :
    
    # calculate the sectors in the output image and create it.
    sec_count = (int(OUTPUT_SIZE[0]/sec_size), int(OUTPUT_SIZE[1]/sec_size)) 
    oi = Image.new("RGB",OUTPUT_SIZE)

    # spots is a matrix holding the status of each sector of the output image
    spots =  [[True for c in range(sec_count[0])] for r in range(sec_count[1])]

    if(SHUFFLE):
        random.shuffle(pics)

    # draw each picture to the output image
    for p in pics:
        img = Image.open(p)
        i_size = img.size
        is_w = int(math.ceil(i_size[0]/sec_size))    # spots needed for width
        is_h = int(math.ceil(i_size[1]/sec_size))    # spots needed for height

        location = (-1,-1)  # (row, column) of the image being placed
        # At each individual spot, check if there is not  enough space open to
        # display the current image
        for r, row in enumerate(spots):
            display = False # are we displaying at the current spot?
            for c, val in enumerate(row):
                if ((r + is_h) > sec_count[1]):
                    display = False
                    break
                if ((c + is_w) > sec_count[0]):
                    display = False
                    break

                clear = True
                # is every square starting at spot[r][c] to spot[r+is_h][r+is_w]
                # open?
                for h in range(is_h):
                    if not clear:
                        display = False
                        break;
                    for w in range(is_w):
                        if not spots[r+h][c+w]:
                            clear = False
                            break
                    #endfor
                #endfor

                # we can fill up the current box
                if clear:
                    location = (r, c)
                    display = True
                    break
            #endfor
            if display:
                break
        #endfor
        if VERBOSE:
            print("Pasting image at location {}".format(location))

        # update the spots grid. 
        if location[0] != -1 and location[1] != -1:
            # we can!
            for h in range(is_h):
                for w in range(is_w):
                    spots[location[0] + h][location[1]+w] = False

            # draw the image
            oi.paste(img, (location[1] * sec_size, location[0] * sec_size))

    # save the image
    oi.save(OUTPUT_PATH)

if __name__ == '__main__':
    # parse the arguments
    parser = argparse.ArgumentParser(
                            description="Create a collage from pictures. "
                        )
    # Shuffle the picture files
    parser.add_argument("--shuffle",
                        help="Randomize the order of the pictures before\
                        creating the collage."
                       )
    # output file
    parser.add_argument("-o","--output",
                        nargs=1,
                        help="Change the path of the output file."
                       )
    # output size
    parser.add_argument("-s", "--size",
                        nargs=2,
                        help="Change the dimensions of the output file."
                       )
    # picture arguments
    parser.add_argument("pic_path", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    if(args.shuffle):
        SHUFFLE = True
    if(args.output):
        OUTPUT_PATH = args.output[0]
    if(args.size):
        OUTPUT_SIZE = (args.size[0],args.size[1])
    if(args.pic_path):
        main(args.pic_path)
