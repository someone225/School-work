"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Checkpoint 1 task 1: open desired images for user and additionally ask if
                         grayscale conversion is requested if rgb image is provided

Assignment Information:
    Assignment:     tp1 team 1 - Team Project Checkpoint 1 Task 1
    Team ID:        007 - 19
    Author:         Mark Sheng, sheng65@purdue.edu
    Date:           09/10/2025

Contributors:
    Mark, sheng65@purdue [repeat for each]
    Akshada, dakea@purdue
    Erdem, eamarsa@purdue
    Milagros, mmelhemb@purdue 


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


'''
workflow cases:
    - ask user for image to open
    - scan for channel count -> if 4, discard 4th channel
    - if channel count -> 3, image is rgb, ask user if desire output in grayscale
    - if channel count -> 2, image is grayscale, output as is
'''

import math as m
from PIL import Image, ImageOps
import numpy as np


def main():
    path = str(input("Enter the path of the image you want to load: "))
    img = image()
    img.img_data = load_img(path)
    img.set_in_path(path)

    #print(img.img_data.ndim)
    match img.img_data.ndim:
        case 2: #grayscale
            img.show_image()
        case 3: #rgb
            handle_rgb_case(img)
        case 4: #rgbA
            #code for rgbA data is functionally similar to getting rgb data as the 4th channel is simply ignored
            handle_rgb_case(img)
        case _: #default case, expecting an error in data if none above cases match
            #raise IndexError as the program is unsure if there is sufficient dimensions to index output data
            raise IndexError
        
        
class image:
    in_path: str
    img_data: list
    ch_data: list

    zero_width: int
    zero_height: int


    def set_in_path(self, path:str):
        """
        sets the path for a new image
        Args:
            path <string>:  the path to the image
        Returns: 
            void
        Dependencies: 
            None
        """
        self.in_path = path
    
    def show_image(self):
        img_out = Image.fromarray(self.img_data)
        img_out.show()
          
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

def handle_rgb_case(img):
    """
        asks the user if they want to convert an rgb image to grayscale
        Args:
            img <class>: an imageUtils image class
        Returns: 
            void, modifies class values
        Dependencies: 
            None
    """
    selector = str(input("Would you like to convert to grayscale?\n"))
    match selector:
        case 'yes':
            img.img_data = rgb_to_grayscale(img.img_data)
            img.show_image()
        case 'no':
            img.show_image()
        case _:
            #this is here in case the user inputs anything unexpected
            #raise ValueError as the user has inputted an unexpected value
            raise ValueError

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

CHANNEL_WEIGHTS = [0.2126, 0.7152, 0.0722]
def rgb_to_grayscale (img_array):  
    """
    converts an array of rgb pixel values into grayscale using the grayscale conversion algorithm
    Args:
        img_array: a 3 dimensional array containing data on the image
                   more specifically, it is a numpy array obtained from calling
                   numpy.asarray on PIL.Image.open, and NOT an appended list of
                   rgb pixel values
    Returns: 
        gray_values: a 2 dimensional array containing grayscale converted pixel values for the image

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


if __name__ == "__main__":
    main()
