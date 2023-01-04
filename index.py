from PIL import Image
#open image using Image module
im = Image.open("christmas.png")
#show actual image
im.show()
#show rotated image
im = im.rotate(45)
im.show()