"""
File: most_humorous_award.py
Author:王偉誠
ID:0711506
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2019 Most
Humorous Award for Introduction to Computer
Science class in NCTUMSE.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage


def smaller(img):
    """
    This method can change the size of the image.
    (make the image smaller.)
    """
    blank = SimpleImage.blank(img.width // 2, img.height // 2)
    for x in range(blank.width):
        for y in range(blank.height):
            blank_pixel = blank.get_pixel(x, y)
            img_pixel = img.get_pixel(x * 2, y * 2)
            blank_pixel.red = img_pixel.red
            blank_pixel.green = img_pixel.green
            blank_pixel.blue = img_pixel.blue
    return blank


def no_green(img):
    """
    This method will use the blank pixels to replace the green pixels in the image.
    """
    blank = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            blank_pixel = blank.get_pixel(x, y)
            avg = (pixel.red + pixel.green + pixel.blue) // 3
            # find out the green pixels and change them to blank pixels.
            if pixel.green > avg > 40:
                pixel.red = blank_pixel.red
                pixel.green = blank_pixel.green
                pixel.blue = blank_pixel.blue
    return img


def blur(background):
    """
    This method will smooth the background after making it bigger.
    """
    blank = SimpleImage.blank(background.width, background.height)
    for x in range(blank.width):
        for y in range(blank.height):
            pixel = blank.get_pixel(x, y)
            if blank.width - 1 > x > 0 and blank.height - 1 > y > 0:
                sum_red = 0
                sum_green = 0
                sum_blue = 0
                # get the nearest pixels of the center pixel.
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        old_9_pixel = background.get_pixel(i, j)
                        sum_red += old_9_pixel.red
                        sum_green += old_9_pixel.green
                        sum_blue += old_9_pixel.blue
                # calculate the average RGB value of the 9 pixels.
                avg_red = sum_red // 9
                avg_green = sum_green // 9
                avg_blue = sum_blue // 9
                # change the RGB value of the center pixel.
                pixel.red = avg_red
                pixel.green = avg_green
                pixel.blue = avg_blue
    return blank


def bigger(background):
    """
    This method can change the size of the background.
    (make the background bigger.)
    """
    blank = SimpleImage.blank(background.width * 3, background.height * 3)
    for x in range(blank.width):
        for y in range(blank.height):
            blank_pixel = blank.get_pixel(x, y)
            background_pixel = background.get_pixel(x // 3, y // 3)
            blank_pixel.red = background_pixel.red
            blank_pixel.green = background_pixel.green
            blank_pixel.blue = background_pixel.blue
    return blank


def ps(img, background):
    """
    This method will copy the img1 and paste it to the background,
    and the result will be funny.
    If it runs correctly, the face of img1 will be pasted to the board of the background.
    """
    for x in range(0, background.width):
        for y in range(0, background.height):
            background_pixel = background.get_pixel(x, y)
            background_avg = (background_pixel.red + background_pixel.green + background_pixel.blue) // 3
            if img.width + 100 > x >= 100 and y < img.height:
                img_pixel = img.get_pixel(x - 100, y)
                img_avg = (img_pixel.red + img_pixel.green + img_pixel.blue) // 3
                if 225 > background_avg > 210 and img_avg < 255:
                    background_pixel.red = img_pixel.red
                    background_pixel.green = img_pixel.green
                    background_pixel.blue = img_pixel.blue
    return background


def main():
    """
    This program will copy the img1 without green pixels, and then
    paste it to the background.
    After running this program, The face of img1 will on the board of the background.
    """
    background = SimpleImage("image_contest/background.jpg")
    background = bigger(background)
    background = blur(background)
    img = SimpleImage("image_contest/img1.jpg")
    img = no_green(img)
    img = smaller(img)
    final = ps(img, background)
    final.show()


if __name__ == '__main__':
    main()
