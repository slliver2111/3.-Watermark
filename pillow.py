import pillow
from PIL import Image


class PillowConverter:
    def __init__(self):
        pass

    #im = Image.open("hopper.ppm")

    def merge(im1, im2):
        w = im1.size[0] + im2.size[0]
        h = max(im1.size[1], im2.size[1])
        im = Image.new("RGBA", (w, h))

        im.paste(im1)
        im.paste(im2, (im1.size[0], 0))

        return im
