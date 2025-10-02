<<<<<<< HEAD
"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Creating a loop with the mathematical factorial series.

Assignment Information:
    Assignment:     9.2.2. Py3 Team 2 B
    Team ID:        007 - 19
    Author:         Akshada Dake, dakea@purdue.edu
    Date:           09/23/2025

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

from math import factorial
def my_factorial(n: int) -> int:
    if n<0:
        return -999 #defined error flag by task B
    if n==0:
        return 1 #because mathematically 0! =1
    result=1
    i=1 
    while i<=n: #loop begins
        result *= i #multiplying the result with i
        i += 1 #incrementing i
    return result

def main():
    n=input("Enter a number: ")
    result=my_factorial(int(n))
    if result==-999:
        print("Error -999 [Negative input].")
    else:
        print(f"The Factorial of {n} is {result}.")

if __name__ == "__main__":
    main()
=======
"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Creating a loop with the mathematical factorial series.

Assignment Information:
    Assignment:     9.2.2. Py3 Team 2 B
    Team ID:        007 - 19
    Author:         Akshada Dake, dakea@purdue.edu
    Date:           09/23/2025

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

from math import factorial
def my_factorial(n: int) -> int:
    if n<0:
        return -999 #defined error flag by task B
    if n==0:
        return 1 #because mathematically 0! =1
    result=1
    i=1 
    while i<=n: #loop begins
        result *= i #multiplying the result with i
        i += 1 #incrementing i
    return result

def main():
    n=input("Enter a number: ")
    result=my_factorial(int(n))
    if result==-999:
        print("Error -999 [Negative input].")
    else:
        print(f"The Factorial of {n} is {result}.")

if __name__ == "__main__":
    main()
>>>>>>> a998878671f29f8f2a90f144218016037d78c5a9
