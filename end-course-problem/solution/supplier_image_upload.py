#!/usr/bin/env python3
import requests, glob

url="http://localhost/upload/"

for img_url in glob.glob("./supplier-data/images/*.jpeg"): 
    with open(img_url, "rb") as opened:
        r=requests.post(url,files={'file':opened})

