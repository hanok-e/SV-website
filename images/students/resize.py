from PIL import Image
import os


for f in os.listdir('.'):
    if f.endswith('.png') or f.endswith('.jpeg') or f.endswith('.jpg'):
        image = Image.open(f)
        width, height = image.size
        new_width = 120
        new_height = int((height*new_width) / width)
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
        if new_height > 120:
            image = image.crop((0, 0, new_width, 120))
        fn, fext = os.path.splitext(f)
        image.save('resized/' + fn + '_resized' + fext, quality=95)

