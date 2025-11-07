%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Course Number: ENGR 13300
% Semester: Fall 2025
%
% Description:
%     Replace this line with a description of your program.
%
% Assignment Information:
%     Assignment:     14.2.1 MA1 Team 3 (for MATLAB 1 Team task 3)
%     Team ID:        007 - 19 (e.g. LC1 - 01; for section LC1, team 01)
%     Author:         Mark, Sheng65@purdue.edu
%     Date:           e.g. 03/24/2025
%
% Contributor:
%     Name, login@purdue [repeat for each]
%
%     My contributor(s) helped me:
%     [ ] understand the assignment expectations without
%         telling me how they will approach it.
%     [ ] understand different ways to think about a solution
%         without helping me plan my solution.
%     [ ] think through the meaning of a specific error or
%         bug present in my code without looking at my code.
%     Note that if you helped somebody else with their code, you
%     have to list that person as a contributor here as well.
%
% Academic Integrity Statement:
%     I have not used source code obtained from any unauthorized
%     source, either modified or unmodified; nor have I provided
%     another student access to my code.  The project I am
%     submitting is my own original work.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
x = input("Enter the value of x: ");
tar = input("Enter the target error threshold percentage: ");
fprintf("Target error threshold: %d%s\n", tar, "%");
terms = 0;

approximate = 0;
actual = exp(x);
diff = 0;
error = 100;

while error > tar
    approximate = maclaurin(x, terms);
    diff = approximate - actual;
    error = abs( diff/actual * 100 );
    %%fprintf("  debug: erorr = %f\n", error);
    terms = terms + 1;
end

fprintf("Actual value: %.2f\n", actual);
fprintf("Terms needed: %d\n", terms);
fprintf("Approximate value: %.2f\n", approximate);


function out = f(n)
    t = 1;
    for i = n:-1:1
        t = t * i;
    end

    if n == 0
        out = 1;
    else
        out = t;
    end
end


function out = maclaurin(num, precision)
    sum = 0;
    for i = 0:1:precision
        sum = sum + ( num^i / f(i) );
    end
    out = sum;
end