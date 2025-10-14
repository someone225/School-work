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
from PIL import Image, ImageOps
import numpy as np

'''
copy over functions instead of importing them to make autograder safe version
'''
class image:
    in_path: str
    img_data: list
    ch_data: list

    zero_width: int
    zero_height: int

    TGT_WIDTH = 100
    TGT_HEIGHT = 100
    size = (TGT_WIDTH, TGT_HEIGHT)

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

    def set_tar_size(self, width, height):
        """
        sets the output target size to map the image to
        Args:
            width <int>: the desired output width
            height <int>: the desired output height
        Returns: 
            void
        Dependencies: 
            None
        """
        self.TGT_WIDTH = width
        self.TGT_HEIGHT = height
        self.size = (width, height)

    def new_image(self):
        """
        initializes a new image class. a path must be set but target size will default to 100 with no call
        Args:
            none
        Returns: 
            void
        Dependencies: 
            None
        """
        t = Image.open(self.in_path)
        (self.zero_width,self.zero_height) = (t.width // 2, t.height // 2)
        t2 = ImageOps.pad(t, self.size, color = '#000')
        self.img_data = np.asarray(t2, dtype= np.uint8)
        self.img_data = self.img_data.copy() 
    
    def get_rgb_data(self):
        for i in range(0, 3):
            self.ch_data = np.zeros( (3, len(self.img_data), len(self.img_data[0]) ) )
            self.ch_data[i] = self.img_data[:,:,i] / 255
            normalize(self.ch_data[i])
            self.img_data[:,:,i] = self.ch_data[i] * 255

    
    def get_grayscale_data(self):
        self.ch_data = self.img_data / 255
        normalize(self.ch_data)
        self.img_data = self.ch_data * 255
    
    def show_image(self):
        img_out = Image.fromarray(self.img_data)
        img_out.show()


def main():
    img = image()
    path = str(input("Enter the path of the image you want to clean: "))
    img.set_in_path(path)
    img.set_tar_size(100, 100)
    img.new_image()
    clean_image(img)

def clean_image(img):
    """
    cleans an image (resizes and adds borders if required)
    Args:
        img <class>: an imageUtils image class
    Returns: 
        void, modifies the input class

    """
    print("Image shape before cleaning: (%d, " %img.zero_width, "%d, "%img.zero_height, "%d)" %img.img_data.ndim, sep = '')

    state = 0
    size_diff_ratio = 0
    size_diff_ratio, state = get_ratio(img.zero_width, img.zero_height)
    
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

if __name__ == "__main__":
    main()



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
def get_ratio(num1, num2):
    """
    calculates the ratio between two numbers
    Args:
        num1: first number
        num2: second number
    Returns: 
        _: the ratio between the greater and lesser number (lesser/greater)
        state: a variable indicating which number is larger

    Dependencies: 
        None
    """

    if(num1 > num2):
        state = 1
        return ((num2/num1), state)

    elif(num2 > num1):
        state = 2
        return ( (num1/num2), state)

    else:
        return 0
