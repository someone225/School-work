<<<<<<< HEAD
"""
Course Number: ENGR 13300
Semester: e.g. Spring 2025

Description:
    Replace this line with a description of your program.

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

import numpy as np


def main():
    print("FOR loop:")
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    for i in range (len(x)):
        for j in range(len(x)):
            print(f"X[{i},{j}] = {x[i,j]} ", sep = '' )

    print("WHILE loop:")
    i = 0
    while(i < len(x)):
        j = 0
        while(j < len(x)):
            print(f"X[{i},{j}] = {x[i,j]} ", sep = '' )
            j += 1
        i += 1


if __name__ == "__main__":
    main()
=======
"""
Course Number: ENGR 13300
Semester: e.g. Spring 2025

Description:
    Replace this line with a description of your program.

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

import numpy as np


def main():
    print("FOR loop:")
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    for i in range (len(x)):
        for j in range(len(x)):
            print(f"X[{i},{j}] = {x[i,j]} ", sep = '' )

    print("WHILE loop:")
    i = 0
    while(i < len(x)):
        j = 0
        while(j < len(x)):
            print(f"X[{i},{j}] = {x[i,j]} ", sep = '' )
            j += 1
        i += 1


if __name__ == "__main__":
    main()
>>>>>>> a998878671f29f8f2a90f144218016037d78c5a9
