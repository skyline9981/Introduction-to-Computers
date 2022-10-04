"""
ID:0711506
Author:王偉誠
Assignment6 - I
Adapted from Nick Parlante's Ghost assignment by
Jerry Liao.

-----------------------------------------------

YOUR DESCRIPTION HERE
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    """
    red_num = int(red)
    green_num = int(green)
    blue_num = int(blue)
    dist = ((red_num - int(pixel.red)) ** 2 + (green_num - int(pixel.green)) ** 2
            + (blue_num - int(pixel.blue)) ** 2) ** (1/2)
    return dist
    pass


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    # calculate the total RGB
    red_sum = 0
    green_sum = 0
    blue_sum = 0
    for i in range(len(pixels)):
        pixel = pixels[i]
        red_sum += pixel.red
        green_sum += pixel.green
        blue_sum += pixel.blue
    # calculate the average RGB
    red_avg = red_sum // len(pixels)
    green_avg = green_sum // len(pixels)
    blue_avg = blue_sum // len(pixels)
    avg = [red_avg, green_avg, blue_avg]
    return avg
    pass


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    some_pixel = []
    avg = get_average(pixels)
    for i in range(len(pixels)):
        pixel = get_pixel_dist(pixels[i], avg[0], avg[1], avg[2])
        some_pixel.append(pixel)
    best = sorted(some_pixel)[0]
    for j in range(len(pixels)):
        pixel = get_pixel_dist(pixels[j], avg[0], avg[1], avg[2])
        if pixel == best:
            return pixels[j]
    pass


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            result_pixel = result.get_pixel(x, y)
            img_pixel = []
            for i in range(len(images)):
                pixel = images[i].get_pixel(x, y)
                img_pixel.append(pixel)
            result_pixel.red = get_best_pixel(img_pixel).red
            result_pixel.green = get_best_pixel(img_pixel).green
            result_pixel.blue = get_best_pixel(img_pixel).blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
