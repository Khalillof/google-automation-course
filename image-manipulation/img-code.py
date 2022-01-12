#!/usr/bin/env python3
from PIL import Image
import glob, os, sys
"""
 check this site for reference
 https://pillow.readthedocs.io/en/stable/
 https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
 https://pillow.readthedocs.io/en/stable/reference/Image.html

"""
# Open, rotate, and display an image (using the default viewer)
with Image.open("hopper.jpg") as im:
    im.rotate(45).show()


#Convert files to JPEG

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)
"""
 Create thumbnails
The following script creates nice thumbnails of all JPEG images in the current directory 
preserving aspect ratios with 128x128 max resolution.

"""
##########################################################################
size = 128, 128

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        im.thumbnail(size)
        im.save(file + ".thumbnail", "JPEG")
###############################################################################

# resize an image and save the new image with a new name
im = Image("example.jpg")
new_im = im.resize((640,480))
print(im.format, im.size, im.mode)
new_im.save("example_resized.jpg")

###################################################################################
# combine these operations into just one line that rotates, resizes, and saves:

im = Image("example.jpg")
im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")

#################################################################################