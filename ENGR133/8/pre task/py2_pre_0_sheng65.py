<<<<<<< HEAD
"""
Course Number: ENGR 13300
Semester: e.g. Spring 2025

Description:
    code for 8.1.2 pre-class task

Assignment Information:
    Assignment:     e.g. 7.2.1 Py1 Team 1 (for Python 1 Team task 1)
    Team ID:        ### - ## (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Name, login@purdue.edu
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

""" Write any import statements here (and delete this line)."""
import math as m

def main():
    a = float(input("Input a number for variable a (can be negative): "))
    b, c = 104, 17
    print("The result of the function was %.2f" %calc_perform(a, b, c), sep='')
    
    
    
    
    
    



def calc_perform(a, b, c):
    output = 0
    if a >= 5:
        output = (m.pow(a, 2) + m.cos(b) - m.log(c)) / (b - (a * c))
    else:
        output = (m.sqrt(a + b)) / ((c / a) + m.sin(b))
    return output

def test(a, b):

    """
    Args:
        arg1: arg1 desc.
        arg2: arg2 desc.

    Returns:
        return desc.
    
    """
    return b


    


if __name__ == "__main__":
    main()

=======
"""
Course Number: ENGR 13300
Semester: e.g. Spring 2025

Description:
    code for 8.1.2 pre-class task

Assignment Information:
    Assignment:     e.g. 7.2.1 Py1 Team 1 (for Python 1 Team task 1)
    Team ID:        ### - ## (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Name, login@purdue.edu
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

""" Write any import statements here (and delete this line)."""
import math as m

def main():
    a = float(input("Input a number for variable a (can be negative): "))
    b, c = 104, 17
    print("The result of the function was %.2f" %calc_perform(a, b, c), sep='')
    
    
    
    
    
    



def calc_perform(a, b, c):
    output = 0
    if a >= 5:
        output = (m.pow(a, 2) + m.cos(b) - m.log(c)) / (b - (a * c))
    else:
        output = (m.sqrt(a + b)) / ((c / a) + m.sin(b))
    return output

def test(a, b):

    """
    Args:
        arg1: arg1 desc.
        arg2: arg2 desc.

    Returns:
        return desc.
    
    """
    return b


    


if __name__ == "__main__":
    main()

>>>>>>> a998878671f29f8f2a90f144218016037d78c5a9
