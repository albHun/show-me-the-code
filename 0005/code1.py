from PIL import Image
import glob, os

#search for jpg files
for infile in glob.glob("./*.jpg"):
#    file, ext = os.path.splitext(infile)

    #open file and get size
    img = Image.open(infile)
    width, height = img.size

    #get shrinking parameter
    if width > 1136 or height > 640:
        wratio = width / 1136.0
        hratio = height / 640.0
        if wratio > hratio:
            shrinkFold = wratio
        else:
            shrinkFold = hratio
    
        #manipulate image
        new_wh = int(width / shrinkFold), int(height / shrinkFold)
        img = img.resize(new_wh)
        img.save(infile + '_thumbnail.jpg')
