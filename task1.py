#! python3

"""
Count by 2's and display all the numbers, 1 on each line.
Continue until the current value is 20
(2 marks)
Inputs:
none

Outputs:
Example:
2
4
6
8
10
...
"""
name=0
count=0
while name!=20:
    name=name+2
    print(name)
    count=count+1
    if count>15:
        break