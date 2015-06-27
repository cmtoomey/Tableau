#!/usr/bin/env python
import xml.etree.ElementTree as ET
import subprocess
import os
import glob
wd = os.getcwd()
pattern = '*.twb'
subprocess.call(["git","reset"])
for name in glob.glob(wd+"/"+pattern):
    tree = ET.parse(name)
    root = tree.getroot()
    thumbnails = tree.findall('thumbnails')
    for thumbnails in thumbnails:
        thumbnail = thumbnails.findall('thumbnail')
        for thumbnail in thumbnail:
            thumbnails.remove(thumbnail)
    tree.write(name)
subprocess.call(["git","add","."])
