"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     10.3.2 py4 Individual 2
    Team ID:        007 - 19
    Author:         Mark, Sheng65@purdue.edu
    Date:           10/06/2025

Contributors:
    Mark, sheng65@purdue.edu

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
import pathlib as pt
import matplotlib.pyplot as plt

R_WEIGHT = 0.2126
G_WEIGHT = 0.7152
B_WEIGHT = 0.0722

COLOR_NAMES = ['red', 'green', 'blue']

def main():
    valid_files = 0
    path = pt.Path('images')
    files = list(path.iterdir())
    for i in range(0, len(files)):
        if pt.PurePosixPath(files[i]) == '.png' or '.jpg' or '.jpeg':
            valid_files += 1
            #print(files[i])

    user_input = ''
    while(user_input != 'q'):
        y_val = 0
        t = [''] * valid_files
        print("Available images:")
        for i in range(0, valid_files): 
            t[i] = str(files[i])
            print("%d." %(i+1), "%s" %t[i][7:])
        #format to exclude first 7 characters ('images/' from output)
        user_input = str(input("Select an image (q to quit): "))

        #check for ValueError on user input
        #if not, this means it can be converted to an integer, and therefore is an integer input
        try: 
            user_input = int(user_input)
            img = Image.open(files[user_input - 1])
            img_data = np.asarray(img)

            #check for ValueError on 8-bit formatting
            #if not, this means the image is not 8-bit
            try:
                uint8_data = np.array(img_data, dtype = np.uint8)

                if(img_data.ndim == 3): #color images
                    ch_red = uint8_data[:, :, 0] / 255 
                    ch_green = uint8_data[:, :, 1] / 255
                    ch_blue = uint8_data[:, :, 2] / 255

                    #normalize channel values
                    normalize(ch_red)
                    normalize(ch_blue)
                    normalize(ch_green)

                    #update 8-bit image data
                    uint8_data[:,:,0] = ch_red * 255
                    uint8_data[:,:,1] = ch_green * 255
                    uint8_data[:,:,2] = ch_blue * 255

                    #plot channel values to 1-d arrays
                    plot_red = a_reduce_dim(ch_red) 
                    plot_green = a_reduce_dim(ch_green) 
                    plot_blue = a_reduce_dim(ch_blue) 

                    #calculate means for luminance formula
                    r_sum = a_mean(plot_red)
                    g_sum = a_mean(plot_green)
                    b_sum = a_mean(plot_blue)

                    #multiply normalized values by 255 to balance finalized values
                    for i in range(0, len(plot_red)):
                        plot_red[i] = plot_red[i] * 255
                        plot_green[i] = plot_green[i] * 255
                        plot_blue[i] = plot_blue[i] * 255

                    #calculate luminance and conglomerate channel plots
                    plot_data = [plot_red, plot_green, plot_blue]
                    y_val = luminance(r_sum, g_sum, b_sum)

                    #plot histogram
                    plt.title('RGB Intensity Histogram')
                    plt.xlabel("Pixel value (0-255)")
                    plt.ylabel("Quantity")
                    for i in range (0, 3):
                        plt.hist(plot_data[i], label = 'x', bins = 256, color = COLOR_NAMES[i], alpha = 0.5)
                    

                    

                else: #grayscale images
                    ch_gray = uint8_data / 255
                    normalize(ch_gray)
                    uint8_data = ch_gray * 255
                    gray_values = a_reduce_dim(ch_gray)
                    gray_sum = a_mean(gray_values)
                    plot_gray = [0] * len(gray_values)
                    for i in range(0, len(plot_gray)):
                        plot_gray[i] = gray_values[i] * 255
                    
                    
                    
                    y_val = luminance(gray_sum, gray_sum, gray_sum)
                    plt.title("Grayscale Intensity Histogram")
                    plt.xlabel("Pixel value (0-255)")
                    plt.ylabel("Quantity")
                    plt.hist(plot_gray, label = 'x', bins = 256, color = 'gray', alpha = 0.5)




                print("The average luminance of the image: %.3f" %y_val)
                img_out = Image.fromarray(uint8_data)
                img_out.show()
                plt.show()
                

            except ValueError:
                print("Image is not 8-bit.")
                raise ValueError
        

        except ValueError:
            print("Invalid choice, please try again.")



def a_reduce_dim(input):
    output = [0] *( len(input) * len(input[0]) )
    k = 0
    for i in range(0, len(input)):
        for j in range(0, len(input[0])):
            output[k] = input[i][j]
            k += 1
    return output

    
def a_sum(input):
    sum = 0
    for i in range (0, len(input)):
            sum += input[i]

    return sum

def a_mean(input):
    return ( a_sum(input) / len(input) )


def normalize(ch_input):
    for i in range(0, len(ch_input)):
        for j in range(0, len(ch_input[0])):
            if(ch_input[i][j] <= 0.0405):
                ch_input[i][j] = ch_input[i][j] / 12.92
            else:
                ch_input[i][j] = m.pow( ((ch_input[i][j] + 0.055)/1.055), 2.4 )    

def luminance(r, g, b):
    return (r * R_WEIGHT + g * G_WEIGHT + b * B_WEIGHT)


if __name__ == "__main__":
    main()
