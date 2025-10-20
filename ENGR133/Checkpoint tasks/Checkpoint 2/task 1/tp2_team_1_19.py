"""
Course Number: ENGR 13300
Semester: e.g. Spring 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     e.g. 7.2.1 Py1 Team 1 (for Python 1 Team task 1)
    Team ID:        ### - ## (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Name, login@purdue.edu
    Date:           e.g. 01/23/2025

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

import numpy as np
import math as m
from PIL import Image, ImageOps


def main():
    test = [-2, -1, 0, 1, 2]
    print(get_combination(test))
    return 0



CHANNEL_WEIGHTS = [0.2126, 0.7152, 0.0722]
def rgb_to_grayscale (img_array):  
    """
    converts an array of rgb pixel values into grayscale using the grayscale conversion algorithm
    Args:
        img_array <numpy.array>: a 3 dimensional array containing data on the image
                   more specifically, it is a numpy array obtained from calling
                   numpy.asarray on PIL.Image.open, and NOT an appended list of
                   rgb pixel values
    Returns: 
        gray_values <list | numpy.uint8>: a 2 dimensional array containing grayscale converted pixel values for the image

    Dependencies: 
        reqires module 'Image' from library 'PIL' for valid input data
        requires library 'numpy' for valid input type
    """
    ch_data = [0] * 3 
    for i in range(0, len(ch_data)):
        ch_data[i] = img_array[:,:,i] * CHANNEL_WEIGHTS[i]

    gray_values = np.zeros((len(ch_data[0]), len(ch_data[0][0])))

    for i in range(0, len(gray_values)):
        for j in range(0, len(gray_values[0])):
            for k in range(0, len(ch_data)):
                gray_values[i][j] += ch_data[k][i][j] 
    
    gray_values = gray_values.astype(np.uint8)

    return gray_values


def gaussian_filter(img_gry, stdev):
    """
    applies a gaussian blur to input grayscale data
    Args:
        << img_gry <list | 2d | numpy.uint8>: array representing grayscale image data
        << stdev <int>: number influencing kernel (target area) size
    Returns: 
        >> img_out <list | 2d | numpy.uint8>: array representing blurred grayscale image data

    Dependencies: 
        !! Requires modules 'Image' and 'ImageOps' from library 'PIL'
        <! Requires rgb inputs to be converted to grayscale
    """
    kernel_size = 2 * 3 * m.ceil(stdev) + 1

    t = Image.fromarray(img_gry)
    new_t = ImageOps.pad(t, (t.width + kernel_size, t.height + kernel_size), color = '#000')
    scan_start_xPos = 3 * m.ceil(stdev) - 1
    scan_start_yPos = 3 * m.ceil(stdev) - 1
 



    return 0


def get_gaussian_kernel_value(centerX, centerY, radius):
    """
    calculates the values of a kernel region after a gaussian blur application
    Args:
        << centerX <int>: x-index of the center of the kernel
        << centerY <int>: y-index of the center of the kernel
        << radius <int>: half the size of the kernel - eg. how far up/down/left/right the function should scan and apply localized blurring to

    Returns: 
        >> k_out <list | 2d>: values representing the values of each pixel in the kernel after blur

    Dependencies: 
        ! None
    """
    return 0

def get_gaussian_weight(xPos, yPos, xRef, yRef):
    """
    calculates the weight of a select pixel according to gaussian blurring algorithm
    Args:
        << xPos <int>: x-index of the current relative position
        << yPos <int>: y-index of the current relative position
        << xRef <int>: x-index of the referance position
        << yRef <int>: y-index of the referance position

    Returns: 
        >> weight <float>: the weight of the current relative position to apply blur to

    Dependencies: 
        ! requires library 'math' for valid calculations
    """
    dx = xRef - xPos
    dy = yRef - yPos

    weight = 1/(2 * m.pi()) * m.pow( m.e(), (-1 * (dx * dx + dy * dy) / 2 ) )
    return weight

def get_combination(array):
    """
    calculates the amount and values of all possible combinations within the values of an array
    Args:
        << array <list | 1d>: array containing any amount of values

    Returns: 
        >> combinations <int>: the amount of possible combinations present within the indexes of the list
        >> pairs <list | 2d>: array containing all possible pairs

    Dependencies: 
        ! None
    """
    combinations = len(array) * len(array)
    pairs = [0] * combinations
    t = 0
    for x in range(0, len(array)):
        pairs[t] = (array[x], array[0])
        for y in range(0, len(array)):
            pairs[t] = (array[x], array[y])
            t += 1
            


    return combinations, pairs

if __name__ == "__main__":
    main()


