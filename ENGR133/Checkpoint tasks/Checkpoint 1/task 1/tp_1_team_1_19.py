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

from Team19CustomUtils import imageUtils
#run "python3 -m pip install Team_19_Custom_Utils_Lib"
#if you are getting import errors, it might be because an update has been pushed,
#try running "pip install --upgrade Team-19-Custom-Utils-Lib" --> current release version should be 0.0.14

def main():
    path = str(input("Enter the path of the image you want to load: "))
    img = imageUtils.image()
    img.img_data = load_img(path)
    img.set_in_path(path)
    img.new_image()

    match img.img_data.ndim:
        case 2: #grayscale
            img.get_grayscale_data()
            img.show_image()
        case 3: #rgb
            handle_rgb_case(img)
        case 4: #rgbA
            #code for rgbA data is functionally similar to getting rgb data as the 4th channel is simply ignored
            handle_rgb_case(img)
        case _: #default case, expecting an error in data if none above cases match
            #raise IndexError as the program is unsure if there is sufficient dimensions to index output data
            raise IndexError
        
    
        
#load_img has to have only one input (due to assignment requirements), so it cannot be a helper function
def load_img(path:str): 
    '''
    args:
        path<str> - a string representing the path of input function
    returns:
        a numpy array containing the information of the image
    '''

    img = Image.open(path)
    data = np.asarray(img, dtype= np.uint8)
    return data.copy()

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
            img.img_data = imageUtils.rgb_to_grayscale(img.img_data)
            img.show_image()
        case 'no':
            img.get_rgb_data()
            img.show_image()
        case _:
            #this is here in case the user inputs anything unexpected
            #raise ValueError as the user has inputted an unexpected value
            raise ValueError

if __name__ == "__main__":
    main()
