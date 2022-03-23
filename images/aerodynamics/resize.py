from PIL import Image
import os


for f in os.listdir('.'):
    if f.endswith('.png') or f.endswith('.jpeg') or f.endswith('.jpg'):
        image = Image.open(f)
        width, height = image.size
        new_height = 300
        new_width = int((width*new_height) / height)
        image = image.resize((new_width, new_height))
        fn, fext = os.path.splitext(f)
        image.save('resized/' + fn + '_resized' + fext, quality=90)

