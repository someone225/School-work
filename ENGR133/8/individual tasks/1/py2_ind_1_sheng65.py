"""
Course Number: ENGR 13300
Semester: e.g. Spring 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     e.g. 8.3.1 Py1 individual
    Team ID:        ### - ## (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Mark, Sheng65@purdue.edu
    Date:           09/18/2025

Contributors:
    Mark, Sheng65@purdue.edu

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

T_MAX = 344.14
P_MAX = 137
MAX_STAT = [T_MAX, P_MAX]

CO2_CRITICAL_T = 304.2
CO2_CRITICAL_P = 73.8
CRITICAL_STAT = [CO2_CRITICAL_T, CO2_CRITICAL_P]

status = [0,0]

def main():
    t = float(input("Enter the temperature of carbon dioxide in Kelvin: "))
    p = float(input("Enter the pressure of carbon dioxide in bar: "))
    if(t < 0):
        print("Error: Please enter a valid temperature.")
    elif(p < 0):
        print("Error: Please enter a valid pressure.")
    else:
        user_input = [t, p]

        check_status(user_input)

        for i in range(0, 2):
            #print("debug: status[%.0f] " %i, "= %.0f" %status[i], sep = '')
            print_feedback(i, user_input)
            
def print_feedback(selector, input) -> None:
    """
    prints out feedback statements depending on the information contained in input list
    Args:
        selector: a value of 0 or 1, indicating printout of temperature or pressure
        input: a list of length 2 containing input temperature and pressure
        additionally uses global list 'status'

    Returns: 
        void
    """
    if(status[0] == 0 and status[1] == 0):
        print("CO2 is at the critical point.")
    else:
        #temperature printouts
        if(selector == 0):
            if(status[0] < 0):
                print("CO2 is below the critical temperature")
                print("Increase the temperature by at least %.2f Kelvin" %(CO2_CRITICAL_T - input[0]), sep = '')
                
            elif(status[0] == 0 or status[0] == 2):
                print("Temperature is within safe operating conditions.")
            else:
                print("Warning! Reduce the temperature!")
                print("Decrease the temperature by at least %.2f Kelvin" %(input[0] - (0.95 * T_MAX)), sep = '')
        #pressure printouts
        else: 
            if(status[1] < 0):
                print("CO2 is below the critical pressure")
                print("Increase the pressure by at least %.2f bar" %(CO2_CRITICAL_P - input[1]), sep = '')
            elif(status[1] == 0 or status[1] == 2):
                print("Pressure is within safe operating conditions.")
            else:
                print("Warning! Reduce the pressure!")
                print("Decrease the pressure by at least %.2f bar" %(input[1] - (0.95 * P_MAX)), sep = '')

def check_status(status_in) -> None:
    """
    checks the status of an input list to global compare values and updates a global output list accordingly
    Args:
        status_in: user inputted data on temperature and pressure
        additionally uses global list 'status'

    Returns: 
        void
    """
    for i in range(0, 2):
        if(status_in[i] < CRITICAL_STAT[i]):
            status[i] = -1
        
        elif(status_in[i] == CRITICAL_STAT[i]):
            status[i] = 0

        elif(status_in[i] >= 0.95 * MAX_STAT[i]):
            status[i] = 1
        else: 
            status[i] = 2

if __name__ == "__main__":
    main()
