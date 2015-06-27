import xml.etree.ElementTree as ET
import os
import glob
wd = os.getcwd()
pattern = '*.twb'
for name in glob.glob(wd+"/"+pattern):
    tree = ET.parse(name)
    root = tree.getroot()
    thumbnails = tree.findall('thumbnails')
    for thumbnails in thumbnails:
        thumbnail = thumbnails.findall('thumbnail')
        for thumbnail in thumbnail:
            thumbnails.remove(thumbnail)
    tree.write(name)
