from PIL import Image, ImageEnhance

im = Image.open("bh.jpeg")

enhancer = ImageEnhance.Brightness(im)

factor = 1.5
im_output = enhancer.enhance(factor)
im_output.save("original.jpg")