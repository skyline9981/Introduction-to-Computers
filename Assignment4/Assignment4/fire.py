"""
File: fire.py
Author:王偉誠
ID:0711506
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    This method will help you find the pixels which
    is redder than other pixels, and set their r = 255, g = 0, and b = 0.
    For other pixels, this method will male them gray.
    """
    photo = SimpleImage(filename)
    for x in range(photo.width):
        for y in range(photo.height):
            pixel = photo.get_pixel(x, y)
            avg = (pixel.red + pixel.green + pixel.blue) // 3
            if pixel.red > avg * HURDLE_FACTOR:  # find the redder pixels.
                pixel.red = 255  # change their RGB.
                pixel.green = 0
                pixel.blue = 0
            else:
                pixel.red = avg  # make other pixels gray.
                pixel.green = avg
                pixel.blue = avg
    return photo


def main():
    """
    This program will find the fire area, and make the pixels red.
    The other pixel will be change to gray.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
