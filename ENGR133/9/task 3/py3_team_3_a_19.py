<<<<<<< HEAD
"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    code for team task 3 py 3

Assignment Information:
    Assignment:     mm.n - Py3 Team 3 A
    Team ID:        007 - 19 (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Mark Sheng, sheng65@purdue.edu
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



def main():
    n = int(input("Enter the value of n: "))
    x = float(input("Enter the value of x: "))

    approx_value = maclaurin_approximate(n, x)
    true_value = m.exp(x)
    error = (approx_value - true_value)/true_value
    

    print("Actual value: %.2f" %true_value)
    print("Approximate value: %.2f" %approx_value)
    print("Error: %.1f" %(error * 100), "%", sep = '')

def maclaurin_approximate(precision: int, power: float):
    #a maclaurin approximation calculates the approximate value of e^x, with its constraints being limited to a finite precision
    if(power == 0): 
        return 1 #any positive real base raised to power 1 is equivalent to 1
    else:
        dividends = [0] * (precision + 1)
        divisors = [0] * (precision + 1)


        output = 0
        for i in range (0, precision + 1):
            dividends[i] = m.pow(power, i)
            divisors[i] = my_factorial(i)
            output += dividends[i]/divisors[i]
        
        return output
        
def my_factorial(n: int) -> int:
    if n<0:
        return -999 #defined error flag by task B
    if n==0:
        return 1 #because mathematically 0! =1
    result=1 
    for i in range(1, n+1): #loop begins
        result *= i #multiplying the result with i
    return result

if __name__ == "__main__":
    main()
=======
"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    code for team task 3 py 3

Assignment Information:
    Assignment:     mm.n - Py3 Team 3 A
    Team ID:        007 - 19 (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Mark Sheng, sheng65@purdue.edu
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



def main():
    n = int(input("Enter the value of n: "))
    x = float(input("Enter the value of x: "))

    approx_value = maclaurin_approximate(n, x)
    true_value = m.exp(x)
    error = (approx_value - true_value)/true_value
    

    print("Actual value: %.2f" %true_value)
    print("Approximate value: %.2f" %approx_value)
    print("Error: %.1f" %(error * 100), "%", sep = '')

def maclaurin_approximate(precision: int, power: float):
    #a maclaurin approximation calculates the approximate value of e^x, with its constraints being limited to a finite precision
    if(power == 0): 
        return 1 #any positive real base raised to power 1 is equivalent to 1
    else:
        dividends = [0] * (precision + 1)
        divisors = [0] * (precision + 1)


        output = 0
        for i in range (0, precision + 1):
            dividends[i] = m.pow(power, i)
            divisors[i] = my_factorial(i)
            output += dividends[i]/divisors[i]
        
        return output
        
def my_factorial(n: int) -> int:
    if n<0:
        return -999 #defined error flag by task B
    if n==0:
        return 1 #because mathematically 0! =1
    result=1 
    for i in range(1, n+1): #loop begins
        result *= i #multiplying the result with i
    return result

if __name__ == "__main__":
    main()
>>>>>>> a998878671f29f8f2a90f144218016037d78c5a9
