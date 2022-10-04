"""
File: green_screen.py
Author:王偉誠
ID:0711506
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    This method will help you find out the green pixels in figure and
    use the pixels in background to replace them.
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            pixel = figure_img.get_pixel(x, y)  # get the pixels in figure.
            background_pixel = background_img.get_pixel(x, y)  # get the pixels in background.
            bigger = max(pixel.red, pixel.blue)
            if pixel.green > 2 * bigger:  # find out the green pixels.
                pixel.red = background_pixel.red
                pixel.green = background_pixel.green
                pixel.blue = background_pixel.blue
            else:
                continue
    return figure_img


def main():
    """
    This program will combine the figure and the background.
    The green pixels in figure will be replaced by the pixels in background.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
