from PIL import Image 

image = Image.open("в.png")
box = (0, 0, 64, 64)
region = image.crop(box)
r, g, b, a = region.split()
region = Image.merge("RGBA", (b, g, r, a))
image.paste(region, box)
image.show()