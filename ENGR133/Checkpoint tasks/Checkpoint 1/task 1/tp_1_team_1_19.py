"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     11.2.1 Team Project Checkpoint 1 Task 1
    Team ID:        007 - 19
    Author:         Mark Sheng, sheng65@purdue.edu
    Date:           09/10/2025

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
    in_path = str(input("Enter the path of the image you want to load: "))
    im = Image.open(in_path)
    img_in_data = np.asarray(im)
    #test grayscale conversion function
    load_img(in_path)


def load_img(path) -> str:
    img = Image.open(path)
    img_data = np.asarray(img, dtype= np.uint8)

    match img_data.ndim:
        case 2: # grayscale, normalize data and open
            ch_gray = img_data / 255
            normalize(ch_gray)
            img_out_data = ch_gray * 255
            img_out = Image.fromarray(img_out_data)
            img_out.show()

        case 3: #rgb
            #code
            print('test rgb case') #remove when finished
            ch_r = img_data[:,:,0]
            ch_g = img_data[:,:,1]
            ch_b = img_data[:,:,2]

            

        case 4: #rgbA
            #code
            print('test rgbA case') #remove when finished
        case _: #default case, expecting an error in data if none above cases match
            raise ValueError
    
def rgb_to_grayscale (img_array):


    ch_r = img_array[:,:,0] / 255
    ch_g = img_array[:,:,1] / 255
    ch_b = img_array[:,:,2] / 255

    gray_values = np.zeros((len(ch_r), len(ch_r[0])))
    
    normalize(ch_r)
    normalize(ch_g)
    normalize(ch_b)

    ch_r = ch_r * CHANNEL_WEIGHTS[0]
    ch_g = ch_g * CHANNEL_WEIGHTS[1]
    ch_b = ch_b * CHANNEL_WEIGHTS[2]

    for i in range(0, len(gray_values)):
        for j in range(0, len(gray_values[0])):
            gray_values[i][j] = ch_r[i][j] * 255 + ch_g[i][j] * 255 + ch_b[i][j] * 255

    return gray_values
    

def a_reduce_dim(input):
    output = [0] *( len(input) * len(input[0]) )
    k = 0
    for i in range(0, len(input)):
        for j in range(0, len(input[0])):
            output[k] = input[i][j]
            k += 1
    return output

def normalize(ch_input):
    for i in range(0, len(ch_input)):
        for j in range(0, len(ch_input[0])):
            if(ch_input[i][j] <= 0.0405):
                ch_input[i][j] = ch_input[i][j] / 12.92
            else:
                ch_input[i][j] = m.pow( ((ch_input[i][j] + 0.055)/1.055), 2.4 )  

def a_sum(input):
    sum = 0
    for i in range (0, len(input)):
        sum += input[i]

    return sum

def a_mean(input):
    return ( a_sum(input) / len(input) )

if __name__ == "__main__":
    main()
