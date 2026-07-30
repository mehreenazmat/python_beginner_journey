"""
Author: Mehreen
Topic: Python Loops

This program demonstrates different types of loops in Python,
including for loops, while loops, range(), break, continue,
pass, and for-else statements.
"""

# -----------------------
# loops are used to execute a statement for a number of times until they are stopped
# -----------------------
student = {                         # dictionary stores multiple datatypes and is mutable
 "name": "mehreen",
 "city": "Sargodha",
 "marks": [100, 45, 89]
}
# looping through dictionary
for key, value in student.items():
    print(key, ":", value)
'''
output :: 
name : mehreen
city : Sargodha
marks : [100, 45, 89]
'''

# -----------------------
# there are two types of loops for and while
# -----------------------


# -----------------------
# for loop
# -----------------------
for i in range(6):
    print(i)
'''
output ::
0
1
2
3
4
5
'''

# -----------------------
# while loop 
# -----------------------
n = 0
while n < 5:
    print("n= ",n)
    n += 1
'''
output ::
0
1
2
3
4
'''

# -----------------------
# accessing elements of list using loops
# -----------------------
s = [1, 'king', 'kali', 'pak']
for i1 in range(len(s)):
    print(s[i1])
n1 = 0
while n1 < len(s):
    print(s[n1])
    n1 += 1
'''
output ::
1
king
kali
pak
'''

# -----------------------
# start, stop and step size in for
# -----------------------
for i2 in range(1, 31, 3):
    print(i2)
'''
output :: 
1
4
7
10
13
16
19
22
25
28
'''

# -----------------------
# for loop with else
# -----------------------
l = [13, 26, 39]
for element in l:
    print(element)
else:
    print("Loop completed successfully")
'''
output ::
13
26
39
Loop completed successfully
'''

# -----------------------
# break statement
# -----------------------
for z in range(5):
    if z == 3:
        break    
    print(z)            # exits loop when condition is fulfilled
    '''
    output :: 
    0
    1
    2
    '''
for z in range(5):
    if z == 3:
        continue         # skips this iteration and continues with others
    print(z)
'''
output :: 
0
1
2
4
'''
for m in range(9):
    pass                 # used to skip a loop
print("Loop finished")

# -----------------------
# End of program
# -----------------------