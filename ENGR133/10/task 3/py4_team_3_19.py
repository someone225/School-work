"""
Course Number: ENGR 13300
Semester: fall 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     10.2.3 Py4 Team 19 (for Python 4 Team task 4)
    Team ID:        (LC1 - 01; for section LC1, team 19)
    Author:         erdem, eamarsa@purdue.edu
    Date:           10/2/2025

Contributors:
    mark, msheng@purdue.edu 

    My contributor(s) helped me:
    [x] understand the assignment expectations without
        telling me how they will approach it.
    [x] understand different ways to think about a solution
        without helping me plan my solution.
    [x] think through the meaning of a specific error or
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

import math
import sys

def absorb_calc(absorbancy, path_length, coefficient) -> float:
    #absorbancy = path_length * coefficient * concentration
    #concentration = absorbancy / (path_length * coefficient)
    return (absorbancy / (path_length * coefficient) )

def count_lines(input):
    lines = 1
    for i in range(0, len(input)):
        if(input[i] == "\n"):
            lines += 1
    return lines

def main():
    file_name = "py4_task3_input.txt"

    #the reason this code's output was breaking was because while strings and character lists are mostly identical,
    #.strip() and .split() will run but actually do nothing on character lists, while they work as intended on strings

    file = open(file_name, "r") 
    data_line = file.read().strip()
    lines = count_lines(data_line)
        
    input_values = [''] * lines

    #parsing algorithm
    start_index = 0
    end_index = 0
    cur_line = 0
    for i in range (0, len(data_line)): 

        if(data_line[i] == ':'):
            start_index = i
        if(data_line[i] == '\n'):
            #print("debug: cur line - %d" %cur_line)
            end_index = i
            for j in range(start_index + 2, end_index):
                input_values[cur_line] += data_line[j]
            cur_line += 1

            #special case handling for last line parsing
            if(cur_line == (lines - 1) ):
                for j in range(len(data_line) - 6, len(data_line) ):
                    input_values[cur_line] += data_line[j]
        
    #print(input_values)

    file.close()
    
    my_substance = substance()
    my_substance.initialize(input_values)
    my_substance.output()


class substance:
    name = ''
    path_length = 0
    extincion_coefficient = 0
    absorbancy = 0
    concentration = 0
    def initialize(self, values) -> None:
        self.absorbancy = [0] * (len(values) - 3)
        self.concentration = [0] * (len(values) - 3)
        indexer = 0
        for i in range(0, len(values)):
            match i:
                case 0:
                    self.name = values[i]
                case 1:
                    self.path_length = float(values[i])
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
            print("For %.4f " %self.absorbancy[i], "absorbency value, the concentration is %.7f" %self.concentration[i], sep = '')












if __name__ == "__main__":
    main()
