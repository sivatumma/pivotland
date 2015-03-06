import os
import sys
from PIL import Image

def resize(folder, fileName, widthHeight):
    filePath = os.path.join(folder, fileName)
    im = Image.open(filePath)
    newIm = im.resize(widthHeight, Image.ANTIALIAS)
    # i am saving a copy, you can overrider orginal, or save to other folder
    newIm.save("resized\\" + fileName)

def bulkResize(imageFolder, widthHeight):
    imgExts = ["png", "bmp", "jpg"]
    for path, dirs, files in os.walk(imageFolder):
        for fileName in files:
            ext = fileName[-3:].lower()
            if ext not in imgExts:
                continue

            resize(path, fileName, widthHeight)

if __name__ == "__main__":
    imageFolder=sys.argv[1] # first arg is path to image folder
    widthHeight=(sys.argv[2],sys.argv[3]) # 2nd is resize in %
    bulkResize(imageFolder, widthHeight)