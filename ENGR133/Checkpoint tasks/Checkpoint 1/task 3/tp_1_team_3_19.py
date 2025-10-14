"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Checkpoint 1 task 3: open desired images for user and additionally ask if
                         grayscale conversion is requested if rgb image is provided

Assignment Information:
    Assignment:     11.2.3 Team Project Checkpoint 1 Task 3
    Team ID:        007 - 19
    Author:         Akshada Dake, dakea@purdue.edu
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

import numpy as np
import math as m

def main():
    return 0
#helper i am reusing from task 1, someone pls fix idk how to import it
#just put something down in main while you work on functions so they dont throw indent errors
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


def rgb_to_hsv(R: int, G: int, B: int):
    """task 3 udf 1 – int R, G, B
    return hsv np.uint8-ready"""

    #normalizing [0,1]
    r=R/255
    g=G/255
    b=B/255

    #Cmax, Cmin, delta
    Cmax=max(r,g,b)
    Cmin=min(r,g,b)
    d = Cmax-Cmin #delta

    #Hue in degrees
    if d==0:
        hue=0.0
    elif Cmax==r:
        hue=60*(((g-b)/d)%6)
    elif Cmax==g:
        hue=60*(((b-r)/d)+2)
    else: #Cmax==b
        hue=60*(((r-g)/d)+4)

    #Saturation
    if Cmax==0:
        s=0 #saturation
    else:
        s=d/Cmax # [1,0]

    #Value
    v=Cmax

    #Scale [0,255]
    H=int(round((hue%360)/(360*255)))
    S=int(round(s*255))
    V=int(round(v*255))

    return H, S, V

def convert_to_hsv(rgb_image: np.ndarray) -> np.ndarray:

#converting an entire rgb image to hsv image uint8 by iterating through rgb_to_hsv
    if rgb_image.dtype != np.uint8 or rgb_image.ndim != 3 or rgb_image.shape [2] != 3:
        raise ValueError ("expects Height x Width x 3(RGB) uint8 array")

    img_lin=rgb_image.astype(np.float32)/255
    for i in range(3):
        normalize(img_lin[:, :, i])

    #converting back to ints
    H, W, _ = img_lin.shape
    out=np.empty((H,W,3), dtype=np.uint8)

    for y in range (H):
        for x in range (W):
            R=int(round(img_lin[y, x, 0]*255))
            G=int(round(img_lin[y, x, 1]*255))
            B=int(round(img_lin[y, x, 2]*255))
            out[y, x] = rgb_to_hsv(R, G, B)
    return out
    


if __name__ == "__main__":
    main()