"""
File: mirror_lake.py
Author:王偉誠
ID:0711506
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    First, this method creates a blank picture, and then
    it will copy the pixels from the top of the original image.
    Then, it will change the pixels from the top and the bottom of the blank picture.
    """
    photo = SimpleImage(filename)
    blank = SimpleImage.blank(photo.width, photo.height * 2)
    for x in range(photo.width):
        for y in range(photo.height):
            photo_pixel = photo.get_pixel(x, y)
            blank_up_pixel = blank.get_pixel(x, y)  # find the top pixels.
            blank_down_pixel = blank.get_pixel(x, blank.height - 1 - y)  # find the bottom pixels.
            blank_up_pixel.red = photo_pixel.red
            blank_up_pixel.green = photo_pixel.green
            blank_up_pixel.blue = photo_pixel.blue
            blank_down_pixel.red = photo_pixel.red
            blank_down_pixel.green = photo_pixel.green
            blank_down_pixel.blue = photo_pixel.blue
    return blank


def main():
    """
    This program will add a mirror lake under the original lake.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
