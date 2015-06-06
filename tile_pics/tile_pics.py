from PIL import Image
import math
import sys

VERBOSE = False

# handle arguments
pics = sys.argv[1:]

# create output image
oi_size = (1920,1080)             
sec_size = 32                   # The created image will be divided into 32x32
sec_count = (int(oi_size[0]/sec_size), int(oi_size[1]/sec_size)) 
oi = Image.new("RGB",oi_size)

# spots is a matrix holding the availability of each sector of the output image
spots =  [[True for c in range(sec_count[0])] for r in range(sec_count[1])]

# draw each picture to the output image
for p in pics:
    img = Image.open(p)
    i_size = img.size
    is_w = int(math.ceil(i_size[0]/sec_size))       # spots needed for width
    is_h = int(math.ceil(i_size[1]/sec_size))       # spots needed for height

    location = (-1,-1)  # (row, column) of the image being placed
    # At each individual spot, check if there is not  enough space open to display
    # the current image
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
            # is every square starting at spot[r][c] to sport[r+is_h][r+is_w]
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

    # display status of the grid

# determine where to place the picture on the image


oi.save("output.png")
# save the image
