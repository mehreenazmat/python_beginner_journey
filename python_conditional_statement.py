"""
Author: Mehreen
Topic: Python Conditional Statements

This program demonstrates:
- if statement
- else statement
- elif statement
- Nested if
- Even/Odd Checker
- Simple Calculator

Each section contains example outputs for beginners.
"""

# -----------------------
# if statement           
# -----------------------        
age = int(input("Enter your age: "))
if age >= 18:                                 # if is used to check whether a condition is satisfied if so it works otherwise ignores
    print("You meet the required criteria...")
'''
output :: Enter your age: 18
          You meet the required criteria...
'''

# -----------------------
# else statement
# -----------------------
age = int(input("Enter your age: "))
if age >= 18:   
    print("You are eligible")
else:                                         # else works when if condition is false
    print("You are not eligible")                 
'''
output :: Enter your age: 4
          You are not eligible
'''

# -----------------------
# elif statement
# -----------------------
age = int(input("Enter your age: "))
if age < 0:   
    print("Age cannot be less than zero")
elif age >= 18:                            # elif adds another condition which is checked when if condition is false also with it multiple conditions could be checked
    print("You are eligible")
else:                                         
    print("You are not eligible") 

'''
output :: Enter your age: -9
          Age cannot be less than zero
'''

# -----------------------
# nested condition        
# -----------------------             # in this another condition is applied with in a condition
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Your grade is A")
    if marks >= 95:
        print("You have top score..")
elif marks >= 70:
    print("Your grade is B")
else:
    print("Your grade is C")

'''
output :: Enter your marks: 96
          Your grade is A
          You have top score..
'''

# -----------------------
# even odd checker
# -----------------------
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive even number..")
    else:
        print("Positive odd number..")
elif num == 0:
    print("You entered zero..")
else:
    print("You entered a negative number")

'''
output :: Enter a number: 4
          Positive even number..
'''

# -----------------------
# simple calculator
# -----------------------
num = int(input("Enter a number: "))
num1 = int(input("Enter another number: "))
sign = input("Enter sign which operation you want to perform(+,-,*,/): ")
if sign == '+':
    print("Your answer is: ", num + num1)
elif sign == '-':
    print("Your answer is: ", num - num1)
elif sign == '*':
    print("Your answer is: ", num * num1)
elif sign == '/':
    if num1 == 0:
        print("Cannot divide by zero")
    else:
        print("Your answer is: ", num / num1)
else:
    print("Invalid sign")
'''
output :: Enter a number: 3
          Enter another number: 2
          Enter sign which operation you want to perform(+,-,*,/): +
          Your answer is: 5
'''

# -----------------------
# End of program
# -----------------------