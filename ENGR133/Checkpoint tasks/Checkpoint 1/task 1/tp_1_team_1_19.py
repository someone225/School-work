"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Checkpoint 1 task 1: open desired images for user and additionally ask if
                         grayscale conversion is requested if rgb image is provided

Assignment Information:
    Assignment:     11.2.1 Team Project Checkpoint 1 Task 1
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


from PIL import Image
import numpy as np
import math as m
import pathlib as pt

CHANNEL_WEIGHTS = [0.2126, 0.7152, 0.0722]

def main():
    #funny workaround so the function gets accepted by assignment requirements
    #the path does nothing here, all input and data is being managed by the structure
    in_path = ''
    load_img(in_path)

#structure to store all information regarding image data
#pointers don't exist in python so all helper functions must be nested within the structure itself
#also its technically called a class but whatever
class image:
    #anyways the only inputs that the below helper function requires is self,
    #as any variables required can be accessed as needed instead of explicitly defined inputs

    in_path: str
    img_data: list
    ch_data: list
    #all variables in this structure are only initialized as their type to begin memory allocation
    #explicit definitions are done when they are required
    #this allows the same list(s) to take on various lengths and contain different data as required
    #pretty sure we also don't run into goofy memory leak issues that definitely would happen in more rigid languages like C

    #__init__ is an automatic call when a structure is called, so it also works to receive inputs
    def __init__(self):
        self.in_path = str(input("Enter the path of the image you want to load: "))
        t = Image.open(self.in_path)
        self.img_data = np.asarray(t, dtype= np.uint8)
        #creating a copy of image data bypasses read-only errors as now we are not modifying the original data
        self.img_data = self.img_data.copy() 
    
    def get_rgb_data(self):
        user_input = str(input("Would you like to convert to grayscale?\n"))

        #use of match cases vs if statements here is really just up to individual style,
        #basically does the same thing in this situation
        match user_input:
            case 'yes':
                self.img_data = rgb_to_grayscale(self.img_data)
            case 'no':
                for i in range(0, 3):
                    self.ch_data = np.zeros( (3, len(self.img_data), len(self.img_data[0]) ) )
                    self.ch_data[i] = self.img_data[:,:,i] / 255
                    normalize(self.ch_data[i])
                    self.img_data[:,:,i] = self.ch_data[i] * 255
            case _:
                #this is here in case the user inputs anything unexpected
                #raise ValueError as the user has inputted an unexpected value
                raise ValueError
    
    def get_grayscale_data(self):
        self.ch_data = self.img_data / 255
        normalize(self.ch_data)
        self.ch_data = self.ch_data * 255
    
    def show_image(self):
        img_out = Image.fromarray(self.img_data)
        img_out.show()

#load_img has to have only one input (due to assignment requirements), so it cannot be a helper function
#this input must be in a path, but no one said we have to do anything with it so it's just here for the sake of it
def load_img(path):
    """
    loads an image
    Args:
        path <unused>: does nothing, really. It is a depreciated value that does not hold any type and is not modified
                       previously used to represent the path of desired image to open, but that information is now 
                       stored in the image structure
    Returns: 
        if image is grayscale -> void, displays linearlized grayscale image
        if image is rgb/rgbA -> void, asks user for conversion confirmation, then displays image as requested
        if none of the above -> void, raises IndexError

    Dependencies: 
        requires library 'numpy' for array dimensions switch case
        requires an initialized 'image' structure
    """
    img = image()
    match img.img_data.ndim:
        case 2: #grayscale
            img.get_grayscale_data()
            img.show_image()

        case 3: #rgb
            img.get_rgb_data()
            img.show_image()

        case 4: #rgbA
            #code for rgbA data is functionally similar to getting rgb data as the 4th channel is simply ignored
            img.get_rgb_data()
            img.show_image()
        case _: #default case, expecting an error in data if none above cases match
            #raise IndexError as the program is unsure if there is sufficient dimensions to index output data
            raise IndexError
    
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
        ch_data[i] = img_array[:,:,i] / 255
        normalize(ch_data[i])
        ch_data[i] = ch_data[i] * CHANNEL_WEIGHTS[i]

    gray_values = np.zeros((len(ch_data[0]), len(ch_data[0][0])))

    for i in range(0, len(gray_values)):
        for j in range(0, len(gray_values[0])):
            for k in range(0, len(ch_data)):
                gray_values[i][j] += ch_data[k][i][j] * 255 

    return gray_values
    
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
