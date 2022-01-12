#!/usr/bin/env python3
import glob, os
from PIL import Image
# rotate, resize and Convert files to JPEG
for infile in glob.glob("./images/*"):
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
       # print(infile, outfile)
        try:
            with Image.open(infile) as im:
                im.convert("RGB").rotate(90).resize((128,128)).save('/opt/icons/'+outfile.split('/')[2])
        except OSError:
            print("cannot convert", infile)
            raise
