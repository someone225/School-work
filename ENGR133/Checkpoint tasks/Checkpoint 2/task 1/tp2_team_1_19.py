"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     tp2 team 1 - checkpoint 2 team task 1
    Team ID:        007 - 19 (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Mark, sheng65@purdue.edu
    Date:           e.g. 01/23/2025

Contributors:
    Mark, sheng65@purdue [repeat for each]
    Akshada, dakea@purdue
    Erdem, eamarsa@purdue
    Milagros, mmelhemb@purdue 

    documentation used: 
    python numpy API referance https://numpy.org/doc/stable/reference/index.html
    python PIL documentation https://pillow.readthedocs.io/en/stable/ 

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
    
    image_path = input("Enter the path to the image file: ")
    data = load_img(image_path)
    data_gry = rgb_to_grayscale(data)
    img_out = gaussian_filter(data_gry, 1)
    output = Image.fromarray(img_out)
    output.show()

    








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

    gray_values = gray_values / 255
    denormalize(gray_values)
    gray_values = gray_values * 255
    

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

    kernel_size = 2 * m.ceil(3 * stdev) + 1

    kernel_data = get_gaussian_kernel_weights(kernel_size, stdev)
    img_out = f_convolve(img_gry,kernel_data, kernel_size)

    return img_out



def get_gaussian_kernel_weights(k_size, stdev):
    """
    calculates the weights of a kernel region for a gaussian blur application
    Args:
        << k_size <int>: size of the kernel
        << stdev <int>: the standard deviation to model weights

    Returns: 
        >> weights <list | 2d>: data representing the weights of a target kernel centered around (centerX, centerY) 

    Dependencies: 
        ! requires module 'math' to perform exponentiation
        ! requires module 'numpy' to perform weight normalization
    """
    kernel = np.zeros((k_size, k_size))
    center = k_size // 2 #normally the center would be found by rounding up, but it is rounded down here because of indexing
    for x in range(0, k_size):
        for y in range(0, k_size):
            dx = x - center
            dy = y - center
            kernel[x, y] = (1/(2 * m.pi * stdev**2) ) * m.exp( (-1 * (  (dx ** 2) + (dy ** 2) ) / (2 * stdev**2 )) )
    weights = kernel / np.sum(kernel)
    return weights 
    

def f_convolve(f_img, f_kernel, k_size):
    """
    performs a convolution of two matrix functions
    Args:
        << f_img  <list | 2d>: image data
        << f_kernel <list | 2d>: data of currently interested kernel
        << k_size <int>: size of the kernel

    Returns: 
        >> img_out <list | 2d>: result of the convolution

    Dependencies: 
        ! k_size must be odd
    """
    radius = k_size // 2
    
    f_rows, f_cols = f_img.shape
    k_rows, k_cols = f_kernel.shape


    f_img = f_img.astype(np.float64)

    f_padded = np.pad(f_img, pad_width = radius, mode='symmetric' )
    #add pad to push convolution as otherwise matrix sizes will not match at edges

    f_out = np.zeros_like(f_img, dtype=np.float64)
    for r in range(f_rows):
        for c in range(f_cols):
            tar_reg = f_padded[r : r + k_rows, c : c + k_cols ]
            f_out[r][c ] = round(np.sum(tar_reg * f_kernel))
    #f_out=np.clip(f_out, 0, 255)

    f_out = f_out.astype(np.uint8)

    return f_out #added to see if fixes issue
    #return f_out


def get_combination(array):
    """
    calculates the amount and values of all possible combinations within the values of an array
    Args:
        << array <list | 1d>: array containing any amount of values

    Returns: 
        >> combinations <int>: the amount of possible combinations present within the indexes of the list
        >> pairs <list | 2d>: array containing all possible pairs

    Dependencies: 
        <! Dimensionality: input array must be one-dimensional
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

def load_img(path:str): 
    '''
    args:
        path<str> - a string representing the path of input function
    returns:
        a numpy array containing the information of the image
    '''

    img = Image.open(path)
    data = np.asarray(img, dtype= np.uint8)
    data = data.copy()
    #print(data.shape)
    match data.ndim:
        case 2:
            ch_data = data / 255
            normalize(ch_data)
            data = ch_data * 255
            data = data.astype(np.uint8)

        case 3:
            data = data[:,:,:3]
            for i in range(0, 3):
                ch_data = np.zeros( (3, len(data), len(data[0]) ) )
                ch_data[i] = data[:,:,i] / 255
                normalize(ch_data[i])
                data[:,:,i] = ch_data[i] * 255
            data = data.astype(np.uint8)
        case 4:
            data = data[:,:,:3]
            for i in range(0, 3):
                ch_data = np.zeros( (3, len(data), len(data[0]) ) )
                ch_data[i] = data[:,:,i] / 255
                normalize(ch_data[i])
                data[:,:,i] = ch_data[i] * 255
            data = data.astype(np.uint8)
        case _:
            raise IndexError("Unepected dimensions in image data")
    return data

def normalize(ch_input):
    """
    normalizes an input array according to the rgb linearlization algorithm
    Args:
        ch_input: a 2d array containing pixel values of one rgb channel

    Returns: 
        void

    Dependencies: 
        requires 'pow' module from library 'math' to linearlize bright pixels
    """
    for i in range(0, len(ch_input)):
        for j in range(0, len(ch_input[0])):
            if(ch_input[i][j] <= 0.0405):
                ch_input[i][j] = ch_input[i][j] / 12.92
            else:
                ch_input[i][j] = m.pow( ((ch_input[i][j] + 0.055)/1.055), 2.4 )  

def denormalize(ch_input):
    """
    Transforms linear float data back to sRGB (gamma-corrected) float data.
    This is the inverse of the normalize() function.
    Operates IN-PLACE on the input array.
    """
    # Use np.where for a fast, vectorized operation
    srgb_low = ch_input <= 0.0031308
    srgb_high = ~srgb_low
    
    ch_input[srgb_low] = ch_input[srgb_low] * 12.92
    ch_input[srgb_high] = (1.055 * np.power(ch_input[srgb_high], (1 / 2.4))) - 0.055

if __name__ == "__main__":
    main()


