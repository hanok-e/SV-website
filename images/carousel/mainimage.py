from PIL import Image

mainimage = Image.open('subburaj2019multiphase.jpg')
mainimage = mainimage.crop((960, 500, mainimage.size[0]-960, mainimage.size[1]-300))
mainimage = mainimage.resize((1920, int((mainimage.size[1]/mainimage.size[0])*1920)))
mainimage_size = mainimage.size
mainimage.save('mainimage.jpg')
mainimage_size = mainimage.size

