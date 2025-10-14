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

from Team19CustomUtils import imageUtils, generalUtils
#run "python3 -m pip install Team_19_Custom_Utils_Lib"
#if you are getting import errors, it might be because an update has been pushed,
#try running "pip install --upgrade Team-19-Custom-Utils-Lib" --> current release version should be 0.0.11


def main():
    img = imageUtils.image()
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

    Dependencies: 
        requires module imageUtils from Team19CustomUtils
        requires module generalUtils from Team19CustomUtils
    """
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

if __name__ == "__main__":
    main()