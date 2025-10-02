<<<<<<< HEAD
"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py2 Ind 2 Main
    Team ID:        idk - 19 (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Mark Sheng, Sheng65@purdue.edu
    Date:           09/24/2025

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

import math as m
import py2_ind_2_functions_sheng65 as f # type: ignore
FEET_TO_INCHES = 12
CUBIC_INCHES_TO_GALLONS = 231



def main():
    error = 0
    shape = str(input("Enter the name of the pool to calculate (Standard, Ramp, or Round): "))
    match shape:
        case "Standard":
            error = 0
        case "Ramp":
            error = 0
        case "Round":
            error = 0
        case _:
            print("Please run the program again and enter a valid pool name.")
            error = 1
            return 0

    prompts = ["Enter the surface length or radius. ", "Enter the surface width or bottom radius. ", "Enter the shallow end depth. ", "Enter the deep end depth. "]
    dimensions = [0] * 4
    for i in range(0, 4):
        dimensions[i] = int(input(prompts[i])) * FEET_TO_INCHES
        if(dimensions[i] <= 0):
            error = 1
    '''
    dimensions[0] = L1, surface length
    dimensions[1] = L2, surface width
    dimensions[2] = Ds, shallow depth
    dimensions[3] = Dd, deep depth
    '''
    if(dimensions[3] < dimensions[2]):
        error = 1
    
    if(error):
        print("Please enter valid dimensions.")


    else:
        '''
        for i in range(0, 4):
            print("Debug: %d" %dimensions[i])
        '''

        volume = 0
        match shape:
            case "Standard":
                #print("Debug: case matched to Standard")
                #v = { (L1/3) * Ds + 2 * [(L1/3) * Ds + 0.5 * (L1/3) * (Dd - Ds)] } * L2 / 231
                volume = f.standard(dimensions[0], dimensions[1], dimensions[2], dimensions[3])
                formatted_volume = f.append_numerical_separator(volume)
                print("The volume of the Standard pool with your dimensions is %s gallons." %formatted_volume, sep = '')
                
            
            case "Ramp": 
                #print("Debug: case matched to Ramp")
                #v = (0.5 * (L1/3) * Ds + 2 * (L1/3) * Ds +   0.5 * (L1/3) * (Dd - Ds) ) * L2 / 231
                volume = f.standard(dimensions[0], dimensions[1], dimensions[2], dimensions[3])
                formatted_volume = f.append_numerical_separator(volume)
                print("The volume of the Ramp pool with your dimensions is %s gallons." %formatted_volume, sep = '')
            
            case "Round":
                #print("Debug: case matched to Round")
                #v = (L1^2 * pi * Ds + (1/3) * pi * (Dd - Ds) * (L2^2 + L2 * L1 + L1^2)) * L2 / 231
                volume = f.round(dimensions[0], dimensions[1], dimensions[2], dimensions[3])
                formatted_volume = f.append_numerical_separator(volume)
                print("The volume of the Round pool with your dimensions is %s gallons." %formatted_volume, sep = '')

                
    




if __name__ == "__main__":
    main()
=======
"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py2 Ind 2 Main
    Team ID:        idk - 19 (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Mark Sheng, Sheng65@purdue.edu
    Date:           09/24/2025

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

import math as m
import py2_ind_2_functions_sheng65 as f # type: ignore
FEET_TO_INCHES = 12
CUBIC_INCHES_TO_GALLONS = 231



def main():
    error = 0
    shape = str(input("Enter the name of the pool to calculate (Standard, Ramp, or Round): "))
    match shape:
        case "Standard":
            error = 0
        case "Ramp":
            error = 0
        case "Round":
            error = 0
        case _:
            print("Please run the program again and enter a valid pool name.")
            error = 1
            return 0

    prompts = ["Enter the surface length or radius. ", "Enter the surface width or bottom radius. ", "Enter the shallow end depth. ", "Enter the deep end depth. "]
    dimensions = [0] * 4
    for i in range(0, 4):
        dimensions[i] = int(input(prompts[i])) * FEET_TO_INCHES
        if(dimensions[i] <= 0):
            error = 1
    '''
    dimensions[0] = L1, surface length
    dimensions[1] = L2, surface width
    dimensions[2] = Ds, shallow depth
    dimensions[3] = Dd, deep depth
    '''
    if(dimensions[3] < dimensions[2]):
        error = 1
    
    if(error):
        print("Please enter valid dimensions.")


    else:
        '''
        for i in range(0, 4):
            print("Debug: %d" %dimensions[i])
        '''

        volume = 0
        match shape:
            case "Standard":
                #print("Debug: case matched to Standard")
                #v = { (L1/3) * Ds + 2 * [(L1/3) * Ds + 0.5 * (L1/3) * (Dd - Ds)] } * L2 / 231
                volume = f.standard(dimensions[0], dimensions[1], dimensions[2], dimensions[3])
                formatted_volume = f.append_numerical_separator(volume)
                print("The volume of the Standard pool with your dimensions is %s gallons." %formatted_volume, sep = '')
                
            
            case "Ramp": 
                #print("Debug: case matched to Ramp")
                #v = (0.5 * (L1/3) * Ds + 2 * (L1/3) * Ds +   0.5 * (L1/3) * (Dd - Ds) ) * L2 / 231
                volume = f.standard(dimensions[0], dimensions[1], dimensions[2], dimensions[3])
                formatted_volume = f.append_numerical_separator(volume)
                print("The volume of the Ramp pool with your dimensions is %s gallons." %formatted_volume, sep = '')
            
            case "Round":
                #print("Debug: case matched to Round")
                #v = (L1^2 * pi * Ds + (1/3) * pi * (Dd - Ds) * (L2^2 + L2 * L1 + L1^2)) * L2 / 231
                volume = f.round(dimensions[0], dimensions[1], dimensions[2], dimensions[3])
                formatted_volume = f.append_numerical_separator(volume)
                print("The volume of the Round pool with your dimensions is %s gallons." %formatted_volume, sep = '')

                
    




if __name__ == "__main__":
    main()
>>>>>>> a998878671f29f8f2a90f144218016037d78c5a9
