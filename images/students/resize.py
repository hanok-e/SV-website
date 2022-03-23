from PIL import Image
import os


for f in os.listdir('.'):
    if f.endswith('.png') or f.endswith('.jpeg') or f.endswith('.jpg'):
        image = Image.open(f)
        width, height = image.size
        new_width = 100
        new_height = int((height*new_width) / width)
        image = image.resize((new_width, new_height))
        fn, fext = os.path.splitext(f)
        image.save('resized/' + fn + '_resized' + fext, quality=90)

