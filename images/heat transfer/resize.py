from PIL import Image
import os


sr21 = Image.open('sreekesh2021.png')
vi20 = Image.open('vivek2020.jpeg')
ku19 = Image.open('kumar2019.png')
sh14 = Image.open('shaafi2014.jpeg')

for f in os.listdir('.'):
    if f.endswith('.png') or f.endswith('.jpeg'):
        image = Image.open(f)
        width, height = image.size
        new_height = 300
        new_width = int((width*new_height) / height)
        image = image.resize((new_width, new_height))
        fn, fext = os.path.splitext(f)
        image.save('resized/' + fn + '_resized' + fext)

