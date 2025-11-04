"""
Course Number: ENGR 13300
Semester: e.g. Spring 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     e.g. checkpoint 3 task 3
    Team ID:        007 - 19
    Author:         MarkN, Sheng65@purdue.edu
    Date:           e.g. 01/23/2025

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

import math as m
import numpy as np


def main():
    """Write your code here (and delete this line)."""



def calculate_sigmoid(z):
    #class 3 function (substack helper)
    """
    calculates the position of an input z according to a rational normalization function
    args:
        z (float): any input number
    returns:
        output (float): the value of the function 1/ (1 + e^-x). A small deviation is added to this value to prevent e^-x from inflating to infinity or diminishing to 0

    """
    e0 = 0.00000000465661287 #2^-31, a value small enough that it should not affect calculation results while staying within most common bounds of negative power floats
                             #it additionally has the benefit of being albe to be precisely represented as a power of 2, greatly reducing floating point error
                             #this value has been entered manually to avoid fallbacking on outside modules, which may introduce their own inconsistencies when constructing stabilizer values
    
    output = 1/(1+ m.exp((-1 * z) + e0))
    #e0 stabilizes the denominator and prevents division by 0
    
    return output

def predict_proba(X, w, b):
    #class 2 function (stack helper)
    """
    calculates the probability for all examples in a dataset
    args:
        X (2d arr): feature matrix in which len(X) returns the number of examples and len(X[0]) returns the number of features
        w (1d arr): weight vector where len(w) matches with len(X[0])
        b (float): bias factor
    returns:
        z (1d arr): probability array where len(z) matches with len(x)

                        matrix multiplication between two matrices x * y and y * z will return an output matrix of x * z
                        in this case, matrix multiplication is performed between one of shape m * n and one of shape n * 1,
                        resulting in an output shape of m * 1

                        this value is then normalized to the sigmoid function to complete the probability array
    """
    z = X @ w + b
    for i in range(0, len(z)):
        z[i] = calculate_sigmoid(z[i])


    print(np.shape(z))
    return z

def predict_labels(X, w, b, threshold = 0.5):
    #class 1 function (main call function)
    """
    converts probabilities to binary class labels (0 or 1)
    args:
        X (2d arr): feature matrix in which len(X) returns the number of examples and len(X[0]) returns the number of features
        w (1d arr): weight vector where len(w) matches with len(X[0])
        b (float): bias factor
        threshold (float): pre-defined comparison threshold. values over this will be designated 1 and values under this will be designated 0
                           the break-even point is equivalent to threshold, so values exactly equivalent to this value will additionally be designated 1

    returns:
        z(1d array): binary classified probability array where len(z) matches with len(X)

                        matrix multiplication between two matrices x * y and y * z will return an output matrix of x * z
                        in this case, matrix multiplication is performed between one of shape m * n and one of shape n * 1,
                        resulting in an output shape of m * 1
    """
    z = predict_proba(X, w, b)
    for i in range(0, len(z)):
        if(z[i] < threshold): 
            z[i] = 0
        else:
            z[i] = 1
    
    return z


if __name__ == "__main__":
    main()

