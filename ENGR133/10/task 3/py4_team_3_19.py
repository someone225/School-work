"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    calculate photon absorbtion of a material given an input file containint relevant data

Assignment Information:
    Assignment:     e.g. 10.2.3 Py4 Team 3
    Team ID:        007 - 19
    Author:         mark, sheng65@purdue.edu
    Date:           e.g. 01/23/2025

Contributors:
    Mark, sheng65@purdue
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
#imports
import math as m
import requests
#MAKE SURE TO RUN 'pip install requests' BEFORE RUNNING FOR THE FIRST TIME

#global constants



def main():
    #pull input file data from github repo
    url = "https://raw.githubusercontent.com/someone225/School-work/refs/heads/main/ENGR133/10/task%203/py4_task3_input.txt"
    load_repo = requests.get(url)
    #load input contents into a local file for local access
    with open("input.txt", "w") as t:
        t.write(load_repo.text)
    parsed_input = [''] * 6
    input_values = [''] * 6

    #open local file for reading
    input_file = open("input.txt", "r")   
    
    for i in range (0, len(parsed_input)): 
        parsed_input[i] = str(input_file.readlines(1))

        start_index = 0
        start_reached = False

        for j in range(0, len(parsed_input[i])):
            if(parsed_input[i][start_index] == ':'):
                start_reached = True

            if(start_reached == False):
                start_index += 1
        for j in range (start_index + 1, len(parsed_input[i]) - 4):
            #lower bound set as start_index + 1 as start_index counts the index that the colon is at
            #upper bound set as len() - 4 as the last 4 characters \n'] must be removed
            input_values[i] += parsed_input[i][j]

    input_file.close()


    new_sub = substance()
    new_sub.initialize(input_values)
    new_sub.output()
     
'''
substance is a class which contains data about the target substance

basic class calls:
first declare a class as class_name = substance() in main
then reference a target value using class_name.value
eg. to get substance name, use class_name.name
'''

class substance:
    name = ''
    path_length = 0
    extincion_coefficient = 0
    absorbancy = [0] * 3
    concentration = [0] * 3

    def initialize(self, values) -> None:
        indexer = 0
        for i in range(0, len(values)):
            match i:
                case 0:
                    self.name = values[i]
                case 1:
                    self.path_length = int(values[i])
                case 2:
                    self.extincion_coefficient = int(values[i])
                case _:
                    self.absorbancy[indexer] = float(values[i])
                    indexer += 1
        for i in range(0, len(self.absorbancy)):
            self.concentration[i] = absorb_calc(self.absorbancy[i], self.path_length, self.extincion_coefficient)
        

    #well it seems the autograder doesn't accept helper functions that reference self
    #and we have to program absorb_calc to take in 3 args instead of a class

    def output(self) -> None:
        print("The name of the substance is %s " %self.name, sep = '')
        for i in range (0, len(self.absorbancy)):
            print("For %.4f " %self.absorbancy[i], " absorbancy value, the concentration is %.7f" %self.concentration[i], sep = '')
            
    
def absorb_calc(absorbancy, path_length, coefficient) -> float:
    #absorbancy = path_length * coefficient * concentration
    #concentration = absorbancy / (path_length * coefficient)
    return (absorbancy / (path_length * coefficient) )
    


if __name__ == "__main__":
    main()
