<<<<<<< HEAD
"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py2 Ind 2 Functions
    Team ID:        idk - 19 (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Mark Sheng, Sheng65@purdue.edu
    Date:           09/24/2025

Contributors:
    Mark Sheng, sheng65@purdue [repeat for each]

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
CUBIC_INCHES_TO_GALLONS = 231

def append_numerical_separator(number) -> str:
    #print("debug: unformatted number: %.2f" %number)
    end = str( m.modf(m.ceil(number * 100)/100))

    end_list = [''] * 4
    
    
    if( (m.ceil(number * 10)/10) == (m.ceil(number * 100)/100)):
        end_list = ['', '.', '', '0']
        end_list[2] = end[3]
    elif( (m.ceil(number )) == (m.ceil(number * 100)/100)):
        end_list = ['', '.', '0', '0']
    else:
        end_list = ['', '.', '', '']
        end_list[2] = end[3]
        end_list[3] = end[4]

    digits = determine_non_decimal_digits(m.floor(number))
    number_converted = str(int(m.floor(number)))
    output = ""
    num_apostrophes = -1
    for i in range(0, digits):
        if(i % 3 == 0):
            num_apostrophes += 1
    
    j = 0
    for i in range(digits - 1, -1, -1):
        output += number_converted[j]
        j += 1
        if( i % 3 == 0 and num_apostrophes > 0):
            output += ','
            num_apostrophes -= 1
    

    for i in range(1, 4):
        #print("end list [%d]" %i , " = %s" %end_list[i], sep = '')
        output += end_list[i]
    
    

    return output

    

def determine_non_decimal_digits(number):
    digits = 1
    while( (number / m.pow(10, digits) ) >= 10):
        digits += 1
    return digits + 1

def calc_volume_rectangular_prism(w, l, h):
    return w * l * h

def calc_volume_right_triangular_prism(w, l, h):
    return 1/2 * w * l * h

def calc_volume_cylinder(r, h):
    return m.pow(r, 2) * m.pi * h

def calc_volume_partial_cone(r2, r1, h):
    return ((1/3) * m.pi * h * (m.pow(r1, 2) + (r1 * r2) + m.pow(r2, 2) ))

def standard(L1, L2, Ds, Dd):
    if(L1 < 0 or L2 < 0 or Ds < 0 or Dd < 0):
        print("Please enter valid dimensions.")
        return None
    else:
        return (3 * calc_volume_rectangular_prism(L2, L1/3, Ds) + 2 * calc_volume_right_triangular_prism(L2, L1/3, (Dd - Ds)) ) / CUBIC_INCHES_TO_GALLONS

def ramp(L1, L2, Ds, Dd):
    if(L1 < 0 or L2 < 0 or Ds < 0 or Dd < 0):
        print("Please enter valid dimensions.")
        return None
    else:
        return (calc_volume_right_triangular_prism(L2, L1/3, Ds) + 2 * calc_volume_rectangular_prism(L2, L1/3, Ds) + calc_volume_right_triangular_prism(L2, L1/3, (Dd - Ds)) ) / CUBIC_INCHES_TO_GALLONS

def round(L1, L2, Ds, Dd):
    if(L1 < 0 or L2 < 0 or Ds < 0 or Dd < 0):
        print("Please enter valid dimensions.")
        return None
    else:
=======
"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py2 Ind 2 Functions
    Team ID:        idk - 19 (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Mark Sheng, Sheng65@purdue.edu
    Date:           09/24/2025

Contributors:
    Mark Sheng, sheng65@purdue [repeat for each]

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
CUBIC_INCHES_TO_GALLONS = 231

def append_numerical_separator(number) -> str:
    #print("debug: unformatted number: %.2f" %number)
    end = str( m.modf(m.ceil(number * 100)/100))

    end_list = [''] * 4
    
    
    if( (m.ceil(number * 10)/10) == (m.ceil(number * 100)/100)):
        end_list = ['', '.', '', '0']
        end_list[2] = end[3]
    elif( (m.ceil(number )) == (m.ceil(number * 100)/100)):
        end_list = ['', '.', '0', '0']
    else:
        end_list = ['', '.', '', '']
        end_list[2] = end[3]
        end_list[3] = end[4]

    digits = determine_non_decimal_digits(m.floor(number))
    number_converted = str(int(m.floor(number)))
    output = ""
    num_apostrophes = -1
    for i in range(0, digits):
        if(i % 3 == 0):
            num_apostrophes += 1
    
    j = 0
    for i in range(digits - 1, -1, -1):
        output += number_converted[j]
        j += 1
        if( i % 3 == 0 and num_apostrophes > 0):
            output += ','
            num_apostrophes -= 1
    

    for i in range(1, 4):
        #print("end list [%d]" %i , " = %s" %end_list[i], sep = '')
        output += end_list[i]
    
    

    return output

    

def determine_non_decimal_digits(number):
    digits = 1
    while( (number / m.pow(10, digits) ) >= 10):
        digits += 1
    return digits + 1

def calc_volume_rectangular_prism(w, l, h):
    return w * l * h

def calc_volume_right_triangular_prism(w, l, h):
    return 1/2 * w * l * h

def calc_volume_cylinder(r, h):
    return m.pow(r, 2) * m.pi * h

def calc_volume_partial_cone(r2, r1, h):
    return ((1/3) * m.pi * h * (m.pow(r1, 2) + (r1 * r2) + m.pow(r2, 2) ))

def standard(L1, L2, Ds, Dd):
    if(L1 < 0 or L2 < 0 or Ds < 0 or Dd < 0):
        print("Please enter valid dimensions.")
        return None
    else:
        return (3 * calc_volume_rectangular_prism(L2, L1/3, Ds) + 2 * calc_volume_right_triangular_prism(L2, L1/3, (Dd - Ds)) ) / CUBIC_INCHES_TO_GALLONS

def ramp(L1, L2, Ds, Dd):
    if(L1 < 0 or L2 < 0 or Ds < 0 or Dd < 0):
        print("Please enter valid dimensions.")
        return None
    else:
        return (calc_volume_right_triangular_prism(L2, L1/3, Ds) + 2 * calc_volume_rectangular_prism(L2, L1/3, Ds) + calc_volume_right_triangular_prism(L2, L1/3, (Dd - Ds)) ) / CUBIC_INCHES_TO_GALLONS

def round(L1, L2, Ds, Dd):
    if(L1 < 0 or L2 < 0 or Ds < 0 or Dd < 0):
        print("Please enter valid dimensions.")
        return None
    else:
>>>>>>> a998878671f29f8f2a90f144218016037d78c5a9
        return (calc_volume_cylinder(L1, Ds) + calc_volume_partial_cone(L1, L2, (Dd - Ds))) / CUBIC_INCHES_TO_GALLONS