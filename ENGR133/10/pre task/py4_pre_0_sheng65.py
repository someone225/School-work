"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    takes in a csv file, scans colums for data, creates a plot, and outputs a modified version to a separate csv file

Assignment Information:
    Assignment:     10.1.2 pre task team 19
    Team ID:        007 - 19 
    Author:         Mark Sheng, sheng65@purdue.edu
    Date:           09/30/2025

Contributors:
    Mark Sheng, sheng65@purdue [repeat for each]

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

""" Write any import statements here (and delete this line)."""
import math as m
import csv
import os
import cv2 #type: ignore
import matplotlib.pyplot as plt #type: ignore
import numpy as np

from PIL import Image  #type: ignore
from PIL import ImageOps #type: ignore

INPUT_FILE_PATH = 'C:/Users/marks/Documents/GitHub/School-work/ENGR133/10/pre task/py4_pre_0_data.csv'
OUTPUT_FILE_PATH = "C:/Users/marks/Documents/GitHub/School-work/ENGR133/10/pre task/py4_pre_0_sheng65.csv"





def main():

    '''
        cwd = os.getcwd()  # Get the current working directory (cwd)
        files = os.listdir(cwd)  # Get all the files in that directory
        print("Files in %r: %s" % (cwd, files))
    '''

    data_col_1_str = [''] * 10
    data_col_2_str = [''] * 10


    with open(INPUT_FILE_PATH, 'r') as csvfile:
        f = csvfile.readlines(0)
        for i in range(0, len(f)):
            z = 0
            #keep appending numbers to data column 1 until a comma is hit
            while(f[i][z] != ","):
                data_col_1_str[i] += f[i][z]
                z += 1
            z += 1 #skip the comma
            #then, keep appending numbers to data colum 2 until a line break is hit
            while(f[i][z] != "\n"):
                data_col_2_str[i] += f[i][z]
                z += 1

        data_col_1_int = [''] * len(data_col_1_str)
        data_col_2_int = [''] * len(data_col_2_str)
        

        

        for i in range(0, len(data_col_1_str)):
           data_col_1_int[i] = int(data_col_1_str[i])
           data_col_2_int[i] = int(data_col_2_str[i]) * 4


        fig, ax = plt.subplots()
        ax.scatter(data_col_1_int, data_col_2_int)
        plt.show()

    with open(OUTPUT_FILE_PATH, 'w') as csv_output:
        for i in range(0, len(data_col_1_int)):
            csv_output.write(f"{data_col_1_int[i]},{data_col_2_int[i]}\n")
        
                    

    #f = open('C:/Users/marks/Desktop/ENGR133/10/pre task/py4_pre_0_data.csv', "r")

    
    #inputs = [0] * 10
    #inputs = f.read()
    #for i in range(0, 9):
        
    #    print(inputs[i])
    


if __name__ == "__main__":
    main()
