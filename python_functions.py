"""
Author: Mehreen
Topic: Python Functions

This program demonstrates the fundamentals of Python
functions, including function definition, parameters,
default parameters, return values, recursion, and
beginner-friendly practice programs with sample outputs.
"""

# -----------------------
# Function is a block of code that is used for performing a tasks without repeating it.
# -----------------------
def greet():
    print("Good Morning")
greet()
# output : Good Morning

# -----------------------
# Functions with parameters
# -----------------------
def greet1(name):
    print(f"Good Morning {name}")
greet1("Mehreen")
greet()
'''
output :
Good Morning Mehreen
Good Morning
'''
# -----------------------
# sum of 2 numbers
# -----------------------
def add_numbers(a, b):
    return a + b
print(f"Sum= {add_numbers(3,8)}")
# output : Sum= 11

# -----------------------
# default parameter
# -----------------------
def country(name="Pakistan"):
    print(f"Country: {name}")
country()
country("Turkey")
'''
output :
Country: Pakistan
Country: Turkey
'''

# -----------------------
# Function to print multiplication table
# -----------------------
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
num = int(input("Enter a number for table: "))
print(f"Table of {num}")
table(num)
'''
output :
Enter a number for table: 7
Table of 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
'''

# -----------------------
# make a function that say good morning to user
# -----------------------
def greet_user(name):
    print(f"Good morning {name}")
user_name = input("Enter your name : ")
greet_user(user_name.title())
'''
output :
Enter your name : neerhem
Good morning Neerhem
'''

# -----------------------
# Write a function square(num) that returns the square of a number.
# -----------------------
def square(num):
    return num*num
number =  int(input("Enter a number to find the square of a number: "))
print(f"Square of {number} is {square(number)}")
'''
output :
Enter a number to find the square of a number: 64
Square of 64 is 4096
'''

# -----------------------
# Write a function is_even(num) that returns True if the number is even, otherwise False.
# -----------------------
def is_even_num(num):
    if num%2 == 0:
        return True
    else:
        return False
number = int(input("Enter a number to check whether it is even or not: "))
print(f"Is {number} an even number ? \t {is_even_num(number)}")
'''
output :
Enter a number to check whether it is even or not: 235214647
Is 235214647 an even number ?    False
'''

# -----------------------
# Write a function largest(a, b, c) that returns the largest of three numbers.
# -----------------------
def largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
a1 = int(input("Enter first number: "))
b1 = int(input("Enter second number: "))
c1 = int(input("Enter third number: "))
print(f"Largest number among {a1}, {b1} and {c1} is {largest_number(a1, b1, c1)}")
'''
output :
Enter first number: 34
Enter second number: 64
Enter third number: 64 
Largest number among 34, 64 and 64 is 64
'''

# -----------------------
# Write a function factorial(n) that returns the factorial of a number.
# -----------------------
def factorial(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return n*factorial(n-1)
fact = int(input("Enter a number to find factorial : "))
print(f"Factorial of {fact} is {factorial(fact)}")
'''
output :
Enter a number to find factorial : 7
Factorial of 7 is 5040
'''

# -----------------------
# Write a function count_vowels(text) that counts the number of vowels in a string.
# -----------------------
def vowel_count(text):
    count = 0
    for char in text:
        if char.lower() in 'aeiou':
            count += 1
    return count
string = input("Enter a string for counting vowels: ")
print(f"Number of vowels in {string} is {vowel_count(string)}")
'''
output :
Enter a string for counting vowels: Number of vowels in sfsnkwrep qgfpjlefogepkt sbzqcsyjcrpjqfdqhvatjnivg flhlvnlqjsvgzhfhrmbanzwjrokzklgymrljuyjalvxqwnoaq q mgkwiapjsyzqlkjwupicsarcsvrzvbqecerwegyhzeubzzd     
Number of vowels in Number of vowels in sfsnkwrep qgfpjlefogepkt sbzqcsyjcrpjqfdqhvatjnivg flhlvnlqjsvgzhfhrmbanzwjrokzklgymrljuyjalvxqwnoaq q mgkwiapjsyzqlkjwupicsarcsvrzvbqecerwegyhzeubzzd  is 28
'''
# -----------------------
# Write a function reverse_string(text) that returns the reversed string.
# -----------------------
def reverse_string(text):
    return text[ : :-1]                  # Slicing is used to reverse the string by using a step value of -1.
print(f"Reversed string of {string} is {reverse_string(string)}")
'''
output :
Enter a string to reverse: yeorbc
Reversed string of yeorbc is cbroey
'''

# -----------------------
# End of program
# -----------------------