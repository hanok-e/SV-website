from PIL import Image

aero = Image.open('srinidhi2017aerodynamics.jpg')
aero = aero.crop((0, 0, aero.size[0], aero.size[1] - 122))
aero = aero.resize((1920, int((aero.size[1]/aero.size[0])*1920)))
aero_size = aero.size
aero.save('aero.jpg')

heat = Image.open('saurav2019heat.jpg')
heat = heat.crop((0, 126, heat.size[0], heat.size[1]))
heat = heat.resize((1920, int((heat.size[1]/heat.size[0])*1920)))
heat_size = heat.size
heat.save('heat.jpg')
heat_size = heat.size

multiphase = Image.open('subburaj2019multiphase.jpg')
multiphase = multiphase.crop((0, 0, multiphase.size[0], multiphase.size[1]-82))
multiphase = multiphase.resize((1920, int((multiphase.size[1]/multiphase.size[0])*1920)))
multiphase_size = multiphase.size
multiphase.save('multiphase.jpg')
multiphase_size = multiphase.size

turbulence = Image.open('jakkala2022turbulence.png')
turbulence = turbulence.crop((0, 161.5, turbulence.size[0], turbulence.size[1]-150))
turbulence = turbulence.resize((1920, int((turbulence.size[1]/turbulence.size[0])*1920)))
turbulence_size = turbulence.size
turbulence.save('turbulence.png')
turbulence_size = turbulence.size

complx = Image.open('karthik2018complex.png')
complex_size = complx.size

sizes = [aero_size, heat_size, multiphase_size, turbulence_size, complex_size]
print(sizes)
