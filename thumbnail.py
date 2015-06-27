#!/usr/bin/env python
# These are the tools you need to do all the things
import xml.etree.ElementTree as ET
import subprocess
import os
import glob
# This gets the current working directory
wd = os.getcwd()
# We are going to search for TWB, so we put store that for later
pattern = '*.twb'
# Since we run this after git add, we need to undo those changes
subprocess.call(["git","reset"])
# Now we find all the files in our folder that end in TWB
for name in glob.glob(wd+"/"+pattern):
    # Then we parse them into the XML tree
    tree = ET.parse(name)
    # Then we get the root directory
    root = tree.getroot()
    # Then we find all the thumbnails tags
    thumbnails = tree.findall('thumbnails')
    for thumbnails in thumbnails:
        # Then we find all the thumbnail tags
        thumbnail = thumbnails.findall('thumbnail')
        for thumbnail in thumbnail:
            # then we delete the thumbnail tags
            thumbnails.remove(thumbnail)
    # Then we overwrite on top of the other file
    tree.write(name)
    break
# then we re-do our git add so the commit works correctly
subprocess.call(["git","add","."])
# because this all happens before the commit message, everything gets captured correctly
