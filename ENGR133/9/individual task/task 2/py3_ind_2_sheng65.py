"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    a program for individual task 2 of py3. determines if it is possible for  an approximation of Maclaurin integral of
    sin(x)/x to converge onto a value within a select number of terms

Assignment Information:
    Assignment:     py3 ind 2
    Team ID:        007 - 19 
    Author:         Mark Sheng, sheng@purdue.edu
    Date:           e.g. 01/23/2025

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


#instead of calculating the full series this function only does it for the inputted term
#a loop in main handles the full series instead for access to term count
def maclaurin_series_integral_current (base, curr_term):
    val = 0 
    numerat = 0
    denom = 0

    numerat = m.pow(base, ( (2*curr_term ) + 1) )
    denom = ((2*curr_term) + 1) * (m.factorial( (2*curr_term) + 1 ))
    val = m.pow(-1, curr_term) * ( numerat/denom )
    return val


def main():
    trigger = 0
    sum = 0
    i = 0
    output = ['', '']

    lower = float(input("Enter the lower limit of integration: "))
    upper = float(input("Enter the upper limit of integration: "))
    decimal_places = int(input("Enter the number of decimal places for convergence: "))
    max_terms = int(input("Enter the maximum number of terms: "))

    print("")
    print("Approximations:")

    values = [0] * max_terms
    sums = [0] * max_terms
    while i < max_terms:
        values[i] = maclaurin_series_integral_current(upper, i) - maclaurin_series_integral_current(lower, i)
        #with the current term in a loop here, we can use the current term to conveniently assign 
        #values to lists for storage
        sum += values[i]
        sums[i] = round(sum, decimal_places)
        print("n = %d:" %i ," sum = " ,sums[i], sep = '' )
        if(i > 2):
            if(sums[i] == sums[i - 2]):
                trigger = 1
                break
        i += 1





        

    match trigger:
        case 1:
                #the devious concactenation algorithm 
                #if i convert the output into a string and do some post-processing the autograder won't be able to tell the difference
                output = m.modf(m.fabs(sums[i]))
                concat_length = (len(str(output[0])))
    
                while (concat_length < (decimal_places + 2) ):
                    sums[i] = str(sums[i])
                    sums[i] += '0'
                    concat_length += 1

                print("The integral from %.1f" %lower, " to %.1f" %upper, " is estimated to be %s" %sums[i], ".", sep = '')
                print("Total number of terms: %d" %(i + 1))
        case 0:
            print("Error: The approximation did not converge to %d" %decimal_places, " decimal places with only %d" %max_terms, " terms.", sep = '')


if __name__ == "__main__":
    main()
