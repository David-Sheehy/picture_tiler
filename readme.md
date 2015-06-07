A simple command line program that creates a collage out of seperate image
files. It was initially created because I wanted to create a wallpaper out of
xkcd comic strips. The resulting hacking session is this quick and dirty
script.

It definitely needs improvement, the algorithm is stupid and has a horrendous
order of growth. It just checks if there's a spot for the particular image
before moving on to the next image. Every spot needs to be checked (n^2
possible spots) at most (m^2) times. No effort is made to try any strategies to
fill the area.

Additionally no argument parsing is done. It's assumed that the only
information passed to it is a list of file paths.
 
#Requirements:  
python3
pillow (python imaging library) >= 2.8.1

(Though earlier versions will probably
work, I did not use any advanced features beyond  Image.new, Image.paste, and
Image.save)

#Options

1. -s=w h --size=w h 
    Adjusts the size of the output file. Default is 1920x1800

2.  -o=filename --ouput=filename
    Changes the output file path.

3. -v --verbose
    Makes the program output verbose. 

#Usage

tile_pics.py path/to/image1 path/to/image2...

#todo
Argument parsing
Create a largest first strategy.
Create the smallest first strategy
