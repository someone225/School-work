"""
Course Number: ENGR 13300
Semester: fall 2025

Description:
    code for 7.2.1 pre task

Assignment Information:
    Assignment:     e.g. 7.2.1 Py1 Team 19 
    Team ID:        ### - ## (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Mark, sheng65@purdue.edu
    Date:           09/10/2025

Contributors:
    Mark, sheng65@purdue [repeat for each]

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
    equation_count = 3
    a, b, c = 20, 8, 9.81

    functions = [0] * equation_count


    func1 = a * m.cos(m.factorial(b))
    functions[0] = func1

    func2 = (m.pow(a,2) - m.pow(a * m.cos(b),2)) / (2 * c)
    functions[1] = func2

    func3 = (a * m.asin(0.5)) / c
    functions[2] = func3

    for i in range(1, equation_count + 1):
        print("equation %.0f: " %i, f"{functions[i - 1]:.4f}")


   



if __name__ == "__main__":
    main()
