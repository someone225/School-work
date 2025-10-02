<<<<<<< HEAD
"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    code for team task 3 py 3

Assignment Information:
    Assignment:      mm.n - Py3 Team 3 B
    Team ID:        007 - 19 (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Name, login@purdue.edu
    Date:           09/23/2025

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

import math as m
import numpy as np
import py3_team_3_a_19 as p #type:ignore

MAX_SEARCH_DEPTH = 10000

def main():
    x = float(input("Enter the value of x: "))
    target_p = float(input("Enter the target error threshold: "))

    attemps = 0
    approximate_value = 0

    #this loop will calculate the degree of precision required to reach the target error
    for i in range(0, MAX_SEARCH_DEPTH):
        if(find_maclaurin_error_percent(i, x) <= target_p):
            attemps = i + 1 
            '''
            what i truly calculates is the index of the loop required to reach target
            since the index of a value is actually one behind the actual position of the value 1 is added to the final result
            '''
            approximate_value = p.maclaurin_approximate(i, x)
            break


    #note: this creates a ton of nested function calls, which is not ideal for performance
    #the closer target_p approaches to zero, the time required to compute rises quickly
    #therefore, the maximum search depth of this loop is bounded to 10000

    print("Terms needed: %d" %attemps)
    print("Actual value: %.2f" %m.exp(x))
    print("Approximate value: %.2f" %approximate_value)
    print("Target error threshold: %.1f" %target_p, "%", sep = '')

def find_maclaurin_error_percent(precision: int, power: float):
    approx_value = p.maclaurin_approximate(precision, power)
    true_value = m.exp(power)
    return m.fabs(((approx_value - true_value)/true_value) * 100)



if __name__ == "__main__":
    main()
=======
"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    code for team task 3 py 3

Assignment Information:
    Assignment:      mm.n - Py3 Team 3 B
    Team ID:        007 - 19 (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Name, login@purdue.edu
    Date:           09/23/2025

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

import math as m
import numpy as np
import py3_team_3_a_19 as p #type:ignore

MAX_SEARCH_DEPTH = 10000

def main():
    x = float(input("Enter the value of x: "))
    target_p = float(input("Enter the target error threshold: "))

    attemps = 0
    approximate_value = 0

    #this loop will calculate the degree of precision required to reach the target error
    for i in range(0, MAX_SEARCH_DEPTH):
        if(find_maclaurin_error_percent(i, x) <= target_p):
            attemps = i + 1 
            '''
            what i truly calculates is the index of the loop required to reach target
            since the index of a value is actually one behind the actual position of the value 1 is added to the final result
            '''
            approximate_value = p.maclaurin_approximate(i, x)
            break


    #note: this creates a ton of nested function calls, which is not ideal for performance
    #the closer target_p approaches to zero, the time required to compute rises quickly
    #therefore, the maximum search depth of this loop is bounded to 10000

    print("Terms needed: %d" %attemps)
    print("Actual value: %.2f" %m.exp(x))
    print("Approximate value: %.2f" %approximate_value)
    print("Target error threshold: %.1f" %target_p, "%", sep = '')

def find_maclaurin_error_percent(precision: int, power: float):
    approx_value = p.maclaurin_approximate(precision, power)
    true_value = m.exp(power)
    return m.fabs(((approx_value - true_value)/true_value) * 100)



if __name__ == "__main__":
    main()
>>>>>>> a998878671f29f8f2a90f144218016037d78c5a9
