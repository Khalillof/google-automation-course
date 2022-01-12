#!/usr/bin/env python3
import glob, os
from PIL import Image
# resize and Convert files to JPEG
for infile in glob.glob("./supplier-data/images/*.tiff"):
    f, e = os.path.splitext(infile)
    outfile = f + ".jpeg"
    if infile != outfile:
       # print(infile, outfile)
        try:
            with Image.open(infile) as im:
                
                im.convert("RGB").resize((600,400)).save('./supplier-data/images/'+outfile.split('/')[3])
        except OSError:
            print("cannot convert", infile)
            raise