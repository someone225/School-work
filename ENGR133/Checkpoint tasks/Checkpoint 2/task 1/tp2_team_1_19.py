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
from PIL import Image, ImageOps, ImageFilter


def main():
    
    image_path = input("Enter the path to the image file: ")
    data = load_img(image_path)
    data_gry = rgb_to_grayscale(data)
    img_out = gaussian_filter_manual(data_gry, 3)
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
    
    gray_values = gray_values.astype(np.uint8)

    return gray_values


def gaussian_filter_manual(img_gry, stdev):
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
    radius = m.floor(kernel_size/2) #round down insted of up as radius counts away from the center pixel (ie kernel size 5 should have radius 2, size 7 should have radius 3, etc)

    t = Image.fromarray(img_gry)
    h0 = t.height
    w0 = t.width

    

    
    img_unpadded = np.asarray(t)
    img_out = np.zeros_like(img_unpadded)
    ref_img = np.pad(img_unpadded, pad_width= radius, mode='constant', constant_values = 0)
    #i_ref = ImageOps.pad(t, (w0 + kernel_size, h0 + kernel_size), color = '#000')
    #ref_img = np.asarray(i_ref)
    #ref_img = ref_img.copy()

    kernel_data = get_gaussian_kernel_weights(radius)
    img_out = f_convolve(ref_img,kernel_data, h0, w0)

    return img_out

def gaussian_filter(img_gry, stdev):
    """
    applies a gaussian blur to input grayscale data using the PIL gaussianblur function
    Args:
        << img_gry <list | 2d | numpy.uint8>: array representing grayscale image data
        << stdev <int>: number influencing kernel (target area) size
    Returns: 
        >> img_out <list | 2d | numpy.uint8>: array representing blurred grayscale image data

    Dependencies: 
        !! Requires modules 'Image' 'ImageOps', and 'ImageFilter' from library 'PIL'
        <! Requires rgb inputs to be converted to grayscale
    """

    t = Image.fromarray(img_gry)
    kernel_size = 2 * 3 * m.ceil(stdev) + 1
    new_t = ImageOps.pad(t, (t.width + kernel_size, t.height + kernel_size), color = '#000')

    new_t = new_t.filter(ImageFilter.GaussianBlur(radius = stdev))

    img_out = np.asarray(new_t, dtype= np.uint8)
    return img_out



def get_gaussian_kernel_weights(radius):
    """
    calculates the weights of a kernel region for a gaussian blur application
    Args:
        << centerX <int>: x-index of the center of the kernel
        << centerY <int>: y-index of the center of the kernel
        << radius <int>: half the size of the kernel - eg. how far up/down/left/right the function should scan and apply localized blurring to
        << img_data <list | 2d>: data representing image being blurred. this must be padded beforehand

    Returns: 
        >> weights <list | 2d>: data representing the weights of a target kernel centered around (centerX, centerY) 

    Dependencies: 
        <! Dimensionality: img_data must be 2-dimensional
        <! Preprocessing: img_data must be padded
    """

 
    sum_weight = 0
   

    #size of the kernel is w = 2 * radius + 1, L = 2 * radius + 1
    w = 2 * radius + 1
    l = 2 * radius + 1
    centerX = w // 2
    centerY = w // 2
    weights = np.zeros((w , l))

    #initialize scan boundaries
    scan_start_index_x = centerX - radius
    scan_start_index_y = centerY - radius

    scan_end_index_x = centerX + radius
    scan_end_index_y = centerY + radius


    


    i = 0
    j = 0


    for x in range(scan_start_index_x, scan_end_index_x + 1):
        j = 0
        for y in range(scan_start_index_y, scan_end_index_y + 1):
            weights[i][j] =  get_gaussian_weight(x, y, centerX, centerY)
            sum_weight += weights[i][j]
            j += 1

        i += 1
    #normalize weights
    for x in range(0, len(weights)):
        for y in range(0, len(weights[0])):
            weights[x][y] = weights[x][y] / sum_weight
            #print(" weight: %.2f" %weights[x][y], sep = '')

    return weights
    

def f_convolve(f_img, f_kernel, zero_height, zero_width):
    """
    performs a convolution of two matrix functions
    Args:
        << f_img  <list | 2d>: image data. must be padded beforehand
        << f_kernel <list | 2d>: data of currently interested kernel
        << zero_height <int>: unpadded height of image
        << zero_width <int>: unpadded width of image

    Returns: 
        >> f_out <list | 2d>: result of the convolution

    Dependencies: 
        ! func_img must be padded before call
    """

    f_out = np.zeros_like(f_img)
    k_height, k_width = f_kernel.shape
    for y in range(0, zero_height):
        for x in range(0, zero_width):
            tar_reg = f_img[y : y + k_height, x : x+k_width]
            f_out[y][x] = np.sum(tar_reg * f_kernel)

    return f_out

    

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
    dx = xPos - xRef
    dy = yPos - yRef

    #print(dy)
    v = (-1 * (  (dx ** 2) + (dy ** 2) ) / 2 )
    weight = (1/(2 * m.pi) ) * m.exp( v )
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


if __name__ == "__main__":
    main()


