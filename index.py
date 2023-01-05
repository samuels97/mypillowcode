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
#im1 = Image.open('christmas.bmp')
#im1.show()

def tnails():
	try:
		print("Started action")
		image = Image.open('christmas.bmp')
		image.thumbnail((90,90))
		image.save('thumbnail.jpg')
		image1 = Image.open('thumbnail.jpg')
		image1.show()
		print("End of action")
	except IOError:
		pass

#tnails()

def MergeImage():
	image = Image.open('christmas.bmp')
	r, g, b = image.split()
	image.show()
	image = Image.merge("RGB", (b, r, g))
	image.show()


MergeImage()