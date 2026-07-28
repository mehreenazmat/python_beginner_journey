"""
Author: Mehreen
Topic: Python Sets Practice

This program demonstrates practice exercises using Conditions with Python 
"""

# -----------------------
# check greatest of four numbers entered by user using nested loops
# -----------------------
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
d = int(input("Enter number d: "))
if a > b:
    if a > c:
        if a > d:
            print("a is greatest")
elif b > a:
    if b > c:
        if b > d:
            print("b is greatest")
elif c > a:
    if c > b:
        if c > d:
            print("c is greatest")
else:
    print("d is greatest")
'''
output :: Enter number a: 2
          Enter number b: 3
          Enter number c: 4
          Enter number d: 1
          c is greatest
'''

# -----------------------
# check greatest of four numbers entered by user
# -----------------------
a1 = int(input("Enter number a1: "))
b1 = int(input("Enter number b1: "))
c1 = int(input("Enter number c1: "))
d1 = int(input("Enter number d1: "))
if a1 > b1 and a1 > c1 and a1 > d1:
    print("Greatest number is a1: ",a1)
elif b1 > a1 and b1 > c1 and b1 > d1:
    print("Greatest number is b1: ",b1)
elif c1 > a1 and c1 > b1 and c1 > d1:
    print("Greatest number is c1: ",c1)
else:
    print("Greatest number is d1: ",d1)
'''
output :: Enter number a1: 4
          Enter number b1: 3
          Enter number c1: 2
          Enter number d1: 1
          Greatest number is a1:  4
'''

# -----------------------
# input 3 subject marks from user and find their percentage if percentage is greater than 40 print pass else fail 
# -----------------------
phy = int(input("Enter marks in physics: "))
chem = int(input("Enter marks in chem: "))
maths = int(input("Enter marks in maths: "))
total_marks = 150
percentage = ((phy + chem + maths)/total_marks)*100
if percentage >= 40 and phy > 20 and chem > 20 and maths > 20:
    print("Congratulations your are passed with",percentage,"%")
else:
    print("Your have failed. ",percentage,"%")

'''
output :: Enter marks in physics: 30  
          Enter marks in chem: 30
          Enter marks in maths: 30
          Congratulations you have passed with 60.0 %
'''

# -----------------------
'''A spam comment is defined under the following cotext
"make alot of money","buy now","subscribe this","click now" . 
write a program to identify spam comments.'''
# -----------------------
c1 = 'make alot of money'
c2 = 'buy now'
c3 = 'subscribe this'
c4 = 'click now'
comment = input("Enter a comment : ").lower().strip()
if (c1 in comment) or (c3 in comment) or (c2 in comment) or (c4 in comment):
    print("Spam comment")
else:
    print(comment)
'''
output :: Enter a comment : beautiful
          beautiful
'''

# -----------------------
# get username and determine whether it contains less than 10 characters or not
# -----------------------
username = input("Enter username: ")
if len(username) < 10:
    print("Your username contains less than 10 characters")
elif len(username) == 10:
    print("Your username contain 10 characters")
else:
    print("Your username contain greater than 10 characters")

'''
output :: Enter username: mehreen azmat
          Your username contain greater than 10 characters
'''

# -----------------------
# check if a name is present in a list or not.
# -----------------------
list_of_name = ["mehreen","aroma","tayyaba","jiya","fatima","aiman"]
name = input("Enter your name : ")
if name in list_of_name:
    print("Your name is present in list.")
else:
    print("Your name is not present in list.")

'''
output :: Enter your name : mehreen
          Your name is present in list.
'''

# -----------------------
# End of program
# -----------------------