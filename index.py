from PIL import Image
#open image using Image module
im = Image.open("christmas.png")
#show actual image
#im.show()
#show rotated image
#im = im.rotate(45)
#im.show()
print(im.filename)
print(im.format)
print(im.mode)
print(im.size)
print(im.width)
print(im.height)
#im.save('christmas.bmp')
im1 = Image.open('christmas.bmp')
im1.show()
