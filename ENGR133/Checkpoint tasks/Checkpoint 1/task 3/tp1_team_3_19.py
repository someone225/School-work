"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Checkpoint 1 task 3: convert rgb image to hsv and apply pixel-pixel transformation
                         to the entire image.

Assignment Information:
    Assignment:     11.2.3 tp1 team 3
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
from PIL import Image, ImageOps

TGT_WIDTH = 100
TGT_HEIGHT = 100

def main():
    path = str(input("Enter the path of the RGB image you want to convert to hsv: ") )
    rgb_img = load_img(path)
    rgb_img = clean_image(rgb_img) #using the clean image function
    
    
    #user pixel coordinates
    x_str, y_str=input("Enter the x and y coordinates of the pixel you want inspect: ").split(',')
    #the above step gets the x, y coordinates to be inspected

    x = int(x_str)
    y = int(y_str)
    #above two converts the strings to integers. This is because we need integer data
    R= int(rgb_img[x, y][0])
    G=int(rgb_img[x, y][1])
    B=int(rgb_img[x, y][2])
    '''rgb_img[y,x] selects the pixel at row y, column x
    (numpy first index is vertical (y) and the seocnd is horizontal (x))
    [0], [1], [2] pick RGB channel values respectively
    using int() makes it so printing and later calculations will be in integers not NumPy types
        '''
    #RGB at x,yimg[y, x]
    print(f"RGB values of the ({x}, {y}) pixel: R={R}, G={G}, B={B}")
    print(f"Converting {path} to HSV...")
    hsv_img= convert_to_hsv(rgb_img)
    H, S, V=map(int, hsv_img[x, y])

    print(f"HSV values of the ({x}, {y}) pixel: H={H}, S={S}, V={V}")

    out = Image.fromarray(hsv_img)
    out.show()
    
def load_img(path:str): 
    '''
    args:
        path<str> - a string representing the path of input function
    returns:
        data.copy <np.array> - a numpy array containing the information of the image
                               this data is returned as a copy to eliminate read-only errors
    '''
    img = Image.open(path).convert("RGB")
    data = np.asarray(img, dtype= np.uint8)
    return data.copy()

def normalize(ch_input):
    """
    normalizes an input array according to the rgb linearlization algorithm
    Args:
        ch_input <array> - a 2d array containing pixel values of one rgb channel

    Returns: 
        void, modifies input data

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
    H=((hue%360)/360*255)
    S=(s*255)
    V=(v*255)

    return H, S, V

#def u8_issue(v: float):
    """helper function to fix uint8 issue in rounding
    returns int ready for np.uint8 conversion"""
    if v<0:
        return 0
    elif v>255:
        return np.uint8(255)
    else:
        return np.uint8(int(v))
    
def convert_to_hsv(rgb_image: np.ndarray):

#converting an entire rgb image to hsv image uint8 by iterating through rgb_to_hsv
    if rgb_image.dtype != np.uint8:
        raise ValueError ("expects 8 bit data")
        
    if rgb_image.ndim != 3: #Height, Width, Dimensions. RGB is 3 dimensions
        raise ValueError ("expects array dimension of 3")
    
    
    '''img_lin=rgb_image.astype(np.float32)/255
    for i in range(3):
        normalize(img_lin[:, :, i])'''
#img_lin is linearized image with values between [0,1]
    #lin.shape gives (height, width, 3). _ ignores 3rd value as it should always be 3
    #out is empty NumPy array in uint8 format where HSV will be stored.
    #converting back to ints
    H, W, _ = rgb_image.shape
    out=np.empty((H,W,3), dtype=np.uint8)
    

    for x in range (H):
        for y in range (W):
            R=int(rgb_image[x, y, 0])
            G=int(rgb_image[x, y, 1])
            B=int(rgb_image[x, y, 2])
            h, s, v = rgb_to_hsv(R, G, B)
            out[x, y] = int(h), int(s), int(v)
    return out

    
def clean_image(img):
    t=Image.fromarray(img)
    w, h =t.size
    scale=min(TGT_WIDTH/w, TGT_HEIGHT/h)
    new_w=int(m.floor(w*scale))
    new_h=int(m.floor(h*scale))
    print(f"Resized image to: ({new_h}, {new_w})")

    t=t.resize((new_w, new_h), resample=Image.BILINEAR)
    t_padded=ImageOps.pad(t, (TGT_WIDTH, TGT_HEIGHT), color="#000")
    return np.asarray(t_padded, dtype=np.uint8).copy()

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

if __name__ == "__main__":
    main()