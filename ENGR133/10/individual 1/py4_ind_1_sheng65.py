"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     10.3.1 py4 Individual 1
    Team ID:        007 - 19
    Author:         Mark, sheng65@purdue.edu
    Date:           10/06/2025

Contributors:
    Mark, Sheng65@purdue.edu

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




from PIL import Image
import numpy as np
import math as m

OUTPUT_FILE_NAME = 'color_analysis.txt'


def main():
    in_file_name = str(input("Enter the filename of the image: "))
    img = Image.open(in_file_name)
    img_data = np.asarray(img)

    if(img_data.ndim == 3):
        ch_red = img_data[:, :, 0] / 255
        ch_green = img_data[:, :, 1] / 255
        ch_blue = img_data[:, :, 2] / 255

        normalize(ch_red)
        normalize(ch_green)
        normalize(ch_blue)

        red_val = a_mean(ch_red)
        green_val = a_mean(ch_green)
        blue_val = a_mean(ch_blue)

    else:
        red_val = 0.00
        green_val = 0.00
        blue_val = 0.00

    out_file = open(OUTPUT_FILE_NAME, 'w')
    out_file.write("Image: %s\n" %in_file_name)

    out_file.write("Red Channel Mean: %.2f\n" %red_val)
    out_file.write("Green Channel Mean: %.2f\n" %green_val)
    out_file.write("Blue Channel Mean: %.2f" %blue_val)


def a_mean(input):
    sum = 0
    for i in range (0, len(input)):
        for j in range(0, len(input[0])):
            sum += input[i][j]

    return (sum / (len(input) * len(input[0])))

def normalize(ch_input):
    for i in range(0, len(ch_input)):
        for j in range(0, len(ch_input[0])):
            if(ch_input[i][j] <= 0.0405):
                ch_input[i][j] = ch_input[i][j] / 12.92
            else:
                ch_input[i][j] = m.pow( ((ch_input[i][j] + 0.055)/1.055), 2.4 )

if __name__ == "__main__":
    main()
