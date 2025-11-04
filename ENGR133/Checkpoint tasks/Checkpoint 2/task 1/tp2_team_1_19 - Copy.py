"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     tp2 team 1 - checkpoint 2 team task 1
    Team ID:        007 - 19 (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Mark, sheng65@purdue.edu
    Date:           e.g. 01/23/2025

Contributors:
    Mark, sheng65@purdue [repeat for each]
    Akshada, dakea@purdue
    Erdem, eamarsa@purdue
    Milagros, mmelhemb@purdue 

    documentation used: 
    python numpy API referance https://numpy.org/doc/stable/reference/index.html
    python PIL documentation https://pillow.readthedocs.io/en/stable/ 

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
from PIL import Image

def main():
    """
    Main function to load, process, and display an image.
    Follows the logic described in the assignment instructions.
    """
    try:
        image_path = input("Enter the path to the image file: ")
        
        # 1. Load the image into a uint8 NumPy array
        data_uint8 = load_img(image_path)

        data_gry = None
        # 2. Convert to grayscale if it's an RGB image
        if data_uint8.ndim == 3:
            
            # (linearize, apply weights, de-linearize) and returns uint8
            data_gry = rgb_to_grayscale(data_uint8)
        else:
            # It's already grayscale
            data_gry = data_uint8
        
        # 3. Apply the Gaussian filter
        # This function takes uint8 and returns uint8
        img_out = gaussian_filter(data_gry, 1)
        
        # 4. Display the image
        output = Image.fromarray(img_out)
        output.show()

    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


CHANNEL_WEIGHTS = [0.2126, 0.7152, 0.0722]

def rgb_to_grayscale(img_array_uint8):  
    """
    Converts a uint8 sRGB array to a uint8 Grayscale array.
    """
    
    # 1. Convert to float (0.0 - 1.0 range)
    img_float = img_array_uint8.astype(np.float64) / 255.0

    # 2. Linearize each channel. We must copy them to operate.
    r_linear = img_float[:, :, 0].copy()
    g_linear = img_float[:, :, 1].copy()
    b_linear = img_float[:, :, 2].copy()
    
    normalize(r_linear)
    normalize(g_linear)
    normalize(b_linear)

    # 3. Apply weights to get linear grayscale float
    linear_rgb = np.stack([r_linear, g_linear, b_linear], axis=-1)
    gray_linear_float = np.dot(linear_rgb, CHANNEL_WEIGHTS)
    
    # 4. De-linearize (apply sRGB gamma)
    gray_srgb_float = gray_linear_float.copy()
    delinearize(gray_srgb_float)

    #convert back to uint8 (0-255 range)
    # Clip 
    gray_srgb_float = np.clip(gray_srgb_float, 0.0, 1.0)
    
    # *FIXED 
    gray_uint8 = (gray_srgb_float * 255).astype(np.uint8)

    return gray_uint8


def normalize(ch_input):
    """
    Transforms sRGB (gamma-corrected) float data to linear float data.
    Operates IN-PLACE on the input array.
    """
    # Use np.where for a fast, vectorized operation
    linear_low = ch_input <= 0.0405
    linear_high = ~linear_low
    
    ch_input[linear_low] = ch_input[linear_low] / 12.92
    ch_input[linear_high] = np.power(((ch_input[linear_high] + 0.055) / 1.055), 2.4)


def delinearize(ch_input):
    """
    Transforms linear float data back to sRGB (gamma-corrected) float data.
    This is the inverse of the normalize() function.
    Operates IN-PLACE on the input array.
    """
    # Use np.where for a fast, vectorized operation
    srgb_low = ch_input <= 0.0031308
    srgb_high = ~srgb_low
    
    ch_input[srgb_low] = ch_input[srgb_low] * 12.92
    ch_input[srgb_high] = (1.055 * np.power(ch_input[srgb_high], (1 / 2.4))) - 0.055


def gaussian_filter(img_gry, stdev):
    """
    Applies a gaussian blur to input grayscale data.
    """
    # 1. Determine kernel size (must be odd)
    kernel_size = 2 * m.ceil(3 * stdev) + 1

    # 2. Get the normalized float kernel
    kernel_data = get_gaussian_kernel_weights(kernel_size, stdev)
    
    # 3. Apply convolution
    img_out = f_convolve(img_gry, kernel_data, kernel_size)

    return img_out


def get_gaussian_kernel_weights(k_size, stdev):
    """
    Calculates the weights of a normalized 2D Gaussian kernel.
    """
    kernel = np.zeros((k_size, k_size), dtype=np.float64)
    center = k_size // 2 
    
    sum_val = 0.0 # For normalization
    
    for x in range(0, k_size):
        for y in range(0, k_size):
            dx = x - center
            dy = y - center
            
            exponent = (-1 * ((dx ** 2) + (dy ** 2))) / (2 * (stdev ** 2))
            prefactor = 1 / (2 * m.pi * (stdev ** 2))
            
            val = prefactor * m.exp(exponent)
            kernel[x, y] = val
            sum_val += val
            
    # Normalize the kernel so all weights sum to 1
    weights = kernel / sum_val
    return weights 
    

def f_convolve(f_img_uint8, f_kernel, k_size):
    """
    Performs a 2D convolution of a uint8 image with a float kernel.
    """
    radius = k_size // 2
    
    # Convert image to float for calculations
    f_img = f_img_uint8.astype(np.float64)
    
    f_rows, f_cols = f_img.shape
    k_rows, k_cols = f_kernel.shape

    # Pad with zeros (mode='constant')
    f_padded = np.pad(f_img, pad_width=radius, mode='constant', constant_values=0)

    # Output array should be float during calculation
    f_out = np.zeros_like(f_img, dtype=np.float64)
    
    # Perform convolution
    for r in range(f_rows):
        for c in range(f_cols):
            # Select the target region from the *padded* image
            tar_reg = f_padded[r : r + k_rows, c : c + k_cols]
            # Apply element-wise multiplication and sum
            #add upcast and see if that fixes?
            f_out[r, c] =  np.sum(tar_reg * f_kernel) 

    #upcasted value can be directy converted afterwards
    f_out = f_out.astype(np.uint8)
    
    return f_out



def load_img(path: str): 
    '''
    Loads an image from a path and returns a uint8 numpy array.
    '''
    img = Image.open(path)
    data = np.asarray(img, dtype=np.uint8)
    data = data.copy() # Make a mutable copy
    
    match data.ndim:
        case 2:
            return data
        case 3:
            return data[:, :, :3]
        case 4:
            return data[:, :, :3]
        case _:
            raise IndexError(f"Unexpected image dimensions: {data.ndim}")

if __name__ == "__main__":
    main()
