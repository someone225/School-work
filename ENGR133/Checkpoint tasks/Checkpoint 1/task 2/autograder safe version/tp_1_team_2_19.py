"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Checkpoint 1 task 2: 

Assignment Information:
    Assignment:     11.2.2 Team Project Checkpoint 1 Task 2
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

import math as m
import numpy as np
from PIL import Image, ImageOps

'''
note to self: remove custom import and copy functions over instead to clean up autograder safe ver
'''
from Team19CustomUtils import imageUtils, generalUtils
#run "python3 -m pip install Team_19_Custom_Utils_Lib"
#if you are getting import errors, it might be because an update has been pushed,
#try running "pip install --upgrade Team-19-Custom-Utils-Lib" in that case --> current release version should be 0.08


def main():
    t = 0
    clean_image(t)


def clean_image(input):
    img = image()
    print("Image shape before cleaning: (%d, " %img.zero_width, "%d, "%img.zero_height, "%d)" %img.img_data.ndim, sep = '')

    state = 0
    size_diff_ratio = 0
    size_diff_ratio, state = generalUtils.get_ratio(img.zero_width, img.zero_height)
    
    match state:
        case 1: #width is greater
            print("Resized image to (%d," %img.TGT_WIDTH, "%d)" %m.floor(img.TGT_WIDTH * size_diff_ratio), sep = '')
        case 2: #height is greater
            print("Resized image to (%d, " %m.floor(img.TGT_HEIGHT * size_diff_ratio) , "%d)" %img.TGT_HEIGHT, sep = '')
    print("Image Shape after cleaning: (%d, " %img.TGT_WIDTH, "%d, " %img.TGT_HEIGHT, "%d)"%img.img_data.ndim, sep = '')

    match img.img_data.ndim:
        case 2: #grayscale
            img.get_grayscale_data()
        case 3: #rgb
            img.get_rgb_data()
        case 4: #rgba, same method to deal with as rgb
            img.get_rgb_data()
        case _:
            raise IndexError
    img.show_image()

class image:
    #anyways the only inputs that the below helper function requires is self,
    #as any variables required can be accessed as needed instead of explicitly defined inputs
    in_path: str
    img_data: list
    ch_data: list
    zero_width: int
    zero_height: int
    TGT_WIDTH = 100
    TGT_HEIGHT = 100
    size = (TGT_WIDTH, TGT_HEIGHT)
    def __init__(self):
        self.in_path = str(input("Enter the path of the image you want to clean: "))
        t = Image.open(self.in_path)
        (self.zero_width,self.zero_height) = (t.width // 2, t.height // 2)
        t2 = ImageOps.pad(t, self.size, color = '#000')
        #print("debug width: ", t2.width // 2)
        self.img_data = np.asarray(t2, dtype= np.uint8)
        self.img_data = self.img_data.copy() 
    
    def get_rgb_data(self):
        for i in range(0, 3):
            self.ch_data = np.zeros( (3, len(self.img_data), len(self.img_data[0]) ) )
            self.ch_data[i] = self.img_data[:,:,i] / 255
            imageUtils.normalize(self.ch_data[i])
            self.img_data[:,:,i] = self.ch_data[i] * 255

    
    def get_grayscale_data(self):
        self.ch_data = self.img_data / 255
        imageUtils.normalize(self.ch_data)
        self.img_data = self.ch_data * 255
    
    def show_image(self):
        img_out = Image.fromarray(self.img_data)
        img_out.show()

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


        case 3: #rgb
            img.get_rgb_data()

        case 4: #rgbA
            #code for rgbA data is functionally similar to getting rgb data as the 4th channel is simply ignored
            img.get_rgb_data()
        case _: #default case, expecting an error in data if none above cases match
            #raise IndexError as the program is unsure if there is sufficient dimensions to index output data
            raise IndexError


if __name__ == "__main__":
    main()