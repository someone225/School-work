"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     10.2.2 team 19
    Team ID:        007 - 19 
    Author:         Name, login@purdue.edu
    Date:           10/01/2025

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

import math as m

#all global variables are constants to prevent accidental modification
TARGET_OUTPUT_FILE = 'py4_team_2_teamnumber.txt'
DAYS_IN_YEAR = 365.242199
HOURS_IN_DAY = 24
SECONDS_IN_HOUR = 3600

def main():
    #probably not needed to do this but the fun thing about helper functions in a class
    #is that the main can just be one declaration and 4 function calls
    new_user = person()
    new_user.calc_total_age()
    new_user.calc_age_seconds()
    new_user.print_results()
    new_user.print_results_to_file()





class person:
    lastName = ''
    firstName = ''
    fullName = ''
    age = 0
    days_from_birthday = 0
    total_age = 0
    age_seconds = 0

    #__init__() is an automatic call when a class is declared, there is no need to externally reference this function
    def __init__(self) -> None:
        self.lastName = str(input("Enter your last name: "))
        self.firstName = str(input("Enter your first name: "))
        self.age = int(input("Enter your age in whole years: "))
        self.days_from_birthday = int(input("Enter the days elapsed since your birthday: "))
        self.fullName = self.firstName + ' ' + self.lastName

    def calc_total_age(self) -> None:
        self.total_age = (self.age + (self.days_from_birthday/DAYS_IN_YEAR) )

    def calc_age_seconds(self) -> None:
        #this function intentionally does not use self.total_age in order to not be reliant on other helper functions
        self.age_seconds = m.floor( (self.age + (self.days_from_birthday/DAYS_IN_YEAR) ) * DAYS_IN_YEAR * HOURS_IN_DAY * SECONDS_IN_HOUR )

    def print_results(self) -> None:
        print(self.fullName)
        print(f"You are {self.total_age} years old.")
        print(f"You are {self.age_seconds} seconds old.")

    def print_results_to_file(self) -> None:
        output_file = open(TARGET_OUTPUT_FILE, 'w')
        #python file writes can only write strings for some reason so everything has to be typecasted
        output_file.write(str(self.fullName))
        output_file.write("\n")
        output_file.write(str(self.total_age))
        output_file.write("\n")
        output_file.write(str(self.age_seconds))
        #line breaks are for formatting reasons
        #it's a lot easier to read, both for algorithms and humans, when there is a distinguishable separator 

        


    


if __name__ == "__main__":
    main()
