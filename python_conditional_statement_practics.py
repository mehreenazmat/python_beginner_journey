"""
Author: Mehreen
Topic: Python Loop Practice Programs

It includes programs such as
multiplication tables, prime number checking, factorial,
sum of numbers, and other loop-based problems with
example outputs.
"""

# -----------------------
# write a program for table of a number using for loop
# -----------------------
n = int(input("Enter a number for table:"))
for i in range(1, 11):
    print(n,"*",i,"=",n*i)
'''
output ::
Enter a number for table:3
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30
'''

# -----------------------
# write a program to greet names in a list starting with s
# -----------------------
s = ['mehreen','sajal','sachin','hiba']
for name in s:
    if(name.startswith('s')):
        print(f" Hello! {name.title()}")
'''
output :: Hello! Sajal
          Hello! Sachin
'''

# -----------------------
# write a program to check whether a number is prime or not
# -----------------------
num = int(input("Enter a number: "))
for i in range(2,num):
    if (num%i)==0:
        print(f"{num} number is not prime")
        break
else:
    print(f"{num} number is prime")
'''
output :: Enter a number : 4
          4 number is not prime
'''

# -----------------------
# write a program to print the sum of first n1 numbers
# -----------------------
n1 = int(input("Enter a number : "))
sum = 0
i = 1
while i <= n1:
    sum += i
    i += 1
print(f"Sum of first {n1} numbers is {sum}.")
'''
output :: Enter a number4
          Sum of first 4 numbers is 10.
'''

# -----------------------
# write a program to find fatcorial of a number using for loop
# -----------------------
n2 = int(input("Enter a number for factorial : "))
fact = 1
for i in range(1,n2+1):
    fact *= i    
print(f"Factorial of {n2} is {fact}")
'''
output :: Enter a number for factorial : 2
          Factorial of 2 is 2
'''

# -----------------------
# write a program to print a pyramid of asterisks 
# -----------------------
n3 = int(input("Enter a number: "))
for i1 in range(1,n3+1):
    print(" "*(n3-i1),"*"* (2*i1-1),end="")
    print("")
'''
output :: 
Enter a number: 3
   *
  ***
 *****
 '''

# -----------------------
# write a program to print sequence
# -----------------------
n4 = int(input("Enter a number : "))
for i2 in range(1,n4+1):
    print("*"*i2,end="")
    print("")
'''
output :: 
enter a number : 3
*
**
***
'''

# -----------------------
# write a program to print hollow triangle
# -----------------------
n5 = int(input("Enter a number : "))
for i3 in range (1,n5+1):
    if i3 == 1 or i3 == n5:
        print("*"*n5,end="")
    else:
        print("*",end="")
        print(" "*(n5-2),end="")
        print("*",end="")
    print("")
'''
output ::
Enter a number : 3
***
* *
***
'''

# -----------------------
# write a program to print sequence of numbers in a triangle
# -----------------------
m = int(input("Enter a number : "))
for j in range(1,m+1):
    print(" "*(m-j),end=" ")
    for k in range(1,j+1):
        print(k,end=" ")
    print("")
'''
output :: 
Enter a number : 3
   1 
  1 2
 1 2 3
'''

# -----------------------
# write a program to print alphabetic sequence in a triangle
# -----------------------   
b = int(input("Enter a number : "))
for l in range(1,b+1):
    for s in range(0,l):
        print(chr(65+s),end=" ")
    print("")

'''
output ::
Enter a number : 3
A 
A B
A B C
'''

# -----------------------
# write another program to print then sequence
# -----------------------     
b = int(input("Enter a number : "))
for l in range(1,b+1):
    print(" "*(b-l),end="")
    for s in range(0,l):
        print(chr(65+s),end=" ")
    print("")

'''
output :: 
Enter a number : 3
  A 
 A B
A B C
'''

# -----------------------
# write a program to print following sequence
# -----------------------
o = int(input("Enter a number : "))
for u in range(n,0,-1):
    for r in range(1,u+1):
        print(r,end=" ")
    print("")

'''
output ::
Enter a number : 3
1 2 3 
1 2
1
'''

# -----------------------
# Write another program to print a sequence
# -----------------------
p = int(input("enter a number : "))
p1 = 1
for y in range(1,p+1):
    for z in range(1,y+1):
        print(p1,end=" ")
        p1+=1
    print("")

'''
output ::
enter a number : 3
1 
2 3
4 5 6
'''

# -----------------------
# write a program to print following sequence
# -----------------------
o = int(input("Enter a number : "))
for u in range(o,0,-1):
    for r in range(0,u):
        print(chr(65+r),end=" ")
    print("")

'''
output ::
Enter a number : 3
A B C 
A B
A
'''

# -----------------------
# write a program to print another sequence
# -----------------------
x = int(input("Enter a number : "))
for v in range(1,x+1):
    print("  "*(x-v),end="")
    for a in range(1,v+1):
        print(a,end=" ")
    for a in range(v-1,0,-1):
        print(a,end=" ")
    print("")
'''
output ::
Enter a number : 3
    1 
  1 2 1
1 2 3 2 1
'''