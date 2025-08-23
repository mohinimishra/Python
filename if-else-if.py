# Flow Control - if else elif

x = 1
if x == 2:
    print(f"x is {x}")
elif x>=1:
    print(f'yes x is equal or greater than one')
else:
    print (f"x is not {x}")
    
"""
Assignment
- Create a variable grade holding an integer between 0 - 100

- Code if, elif, else statements to print the letter grade of the number grade variable

Grades:

A = 90 - 100

B = 80 - 89

C = 70-79

D = 60 - 69

F = 0 - 59

Example:

if grade = 87 then print('B')
"""

grades = 67

if grades <=100 and grades>=90 :
    print('A')
elif grades<=89 and grades>=80 :
    print('B')
elif grades<=79 and grades>=70:
    print('C')
elif grades<=69 and grades>=60:
    print('D')
else:
    print('F')
    

if grades>=90 :
    print('A')
elif 90>grades>=80 :
    print('B')
elif 80>grades>=70:
    print('C')
elif 70>grades>=60:
    print('D')
else:
    print('F')
