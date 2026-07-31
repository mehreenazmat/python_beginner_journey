"""
Author: Mehreen
Topic: Python Pattern Printing

This program demonstrates various pattern printing
techniques using nested for loops. It includes star
patterns, number patterns, alphabet patterns, Pascal's
Triangle, Floyd's Triangle, binary patterns, hollow
patterns, and other beginner-friendly examples with
sample outputs.
"""

# -----------------------
# write a program to print right handed triangle
# -----------------------
n = int(input("Enter a number : "))
for i in range(1,n+1):
    print("*"*i)
'''
output ::
Enter a number : 3
*
**
***
'''

# -----------------------
# write a program to print right handed triangle upside down
# -----------------------
n1 = int(input("Enter a number : "))
for i1 in range(n1,0,-1):
    print("*"*i1)
'''
output :: 
Enter a number : 3
***
**
*
'''

# -----------------------
# write a program to print square
# -----------------------
n2 = int(input("Enter a number : "))
for i2 in range(1,n2+1):
    print("*"*n2)
'''
output :: 
Enter a number : 3
***
***
***
'''

# -----------------------
# write a program to print right angled triangle with numbers
# -----------------------
n3 = int(input("Enter a number : "))
for i3 in range(1,n3+1):
    for j3 in range(1,i3+1):
        print(j3,end="")
    print("")
'''
output ::
Enter a number : 3
1
12
123
'''

# -----------------------
# write a program to print right handed triangle upside down with numbers
# -----------------------
n4 = int(input("Enter a number : "))
for i4 in range(n4,0,-1):
    for j4 in range(1,i4+1):
        print(j4,end="")
    print("")
'''
output ::
Enter a number : 3
123
12
1
'''

# -----------------------
# write a program to  print a right angled triangle of reversed numbers
# write a program to print right handed triangle upside down with numbers
# -----------------------
n5 = int(input("Enter a number : "))
for i5 in range(1,n5+1):
    for j5 in range(i5,0,-1):
        print(j5,end="")
    print("")
'''
output ::
Enter a number : 3
1
21
321
'''

# -----------------------
# write a program to print pyramid of *
# -----------------------
n6 = int(input("Enter a number : "))
for i6 in range(1,n6+1):
    print(" "*(n6-i6),end="")
    print("*"*(2*i6-1),end="")
    print("")
'''
output ::
Enter a number : 3
  *
 ***
***** 
'''

# -----------------------
# write a program to print reversed pyramid of *
# -----------------------
n7 = int(input("Enter a number : "))
for i7 in range(n7,0,-1):
    print(" "*(n7-i7),end="")
    print("*"*(2*i7-1),end="")
    print("")
'''
output ::
Enter a number : 3
*****
 ***
  *
'''

# -----------------------
# write a program to print a diamond shape of *
# -----------------------
n8 = int(input("Enter a number : "))
for i8 in range(1,n8+1):
    print(" "*(n8-i8),end="")
    print("*"*(2*i8-1))
for j8 in range(n8-1,0,-1):
    print(" "*(n8-j8),end="")
    print("*"*(2*j8-1))
'''
output ::
Enter a number : 3
  *
 ***
*****
 ***
  *
'''  

# -----------------------
# write a program to print pascal triangle
# -----------------------
n9 = int(input("Enter a number : "))
for  i9 in range(n9+1):
    val = 1
    print(" "*(n9-i9),end=" ")
    for j9 in range(i9+1):
        print(val,end=" ")
        val=val*(i9-j9) // (j9+1)
    print()
'''
output ::
Enter a number : 3
    1 
   1 1
  1 2 1
 1 3 3 1
 '''

# -----------------------
# write a program to print floyd's triangle
# -----------------------
num = int(input("Enter a number : "))
k = 1
for s in range(1,num+1):
    for t in range(1,s+1):
        print(k,end=" ")
        k += 1
    print("")
'''
output ::
Enter a number : 3
1 
2 3
4 5 6
'''

# -----------------------
# write a program to print even number triangle
# -----------------------
num1 = int(input("Enter a number : "))
k1 = 2
for s1 in range(1,num1+1):
    for t1 in range(s1):
        print(k1,end=" ")
        k1+=2
    print("")

# -----------------------
# write a program to print binary triangle 
# -----------------------
num2 = int(input("Enter number of rows : "))
for s2 in range(1,num2+1):
    start = 1 if (s2%2)!=0 else 0
    val1 = start
    for t2 in range(1,s2+1):
        print(val1,end=" ")
        val1 = 1-val1
    print()
'''
output ::
Enter number of rows : 3
1 
0 1
1 0 1
'''

# -----------------------
# write a program to print alphabetic triangle
# -----------------------
num3 = int(input("Enter number of rows : "))
for s3 in range(num3+1):
    for t3 in range(s3):
        print(chr(65+t3),end=" ")
    print()
'''
output :: 
Enter number of rows : 3
A 
A B
A B C
'''

# -----------------------
# write a program to print inverted alphabetic triangle
# -----------------------
num3 = int(input("Enter number of rows : "))
for s3 in range(num3,0,-1):
    for t3 in range(s3):
        print(chr(65+t3),end=" ")
    print()
'''
output ::
Enter number of rows : 3
A B C 
A B
A
'''

# -----------------------
# write a program to print hollow triangle 
# -----------------------
num4 = int(input("Enter number of rows : "))
for s4 in range(1,num4+1):
    for t4 in range(1,s4+1):
        if t4==1 or t4==s4 or s4==num4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
output ::
Enter number of rows : 4
* 
* *
*   *
* * * *
'''

# -----------------------
# write a program to print  hollow pyramid 
# -----------------------
num4 = int(input("Enter number of rows : "))
for s4 in range(1,num4+1):
    print(" " * (num4-s4),end="")
    for t4 in range(1,s4+1):
        if t4==1 or t4==s4 or s4==num4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
output ::
Enter number of rows : 4
   * 
  * *
 *   *
* * * *
'''

# -----------------------
# write a program to print hollow diamond
# -----------------------
num5 = int(input("Enter number of rows : "))
for s5 in range(1,num5+1):
    print(" " * (num5-s5),end="")
    for t5 in range(1,2*s5):
        if t5 == 1 or t5 == 2*s5-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for u5 in range(num5-1,0,-1):
    print(" "*(num5-u5),end="")
    for v5 in range(1,2*u5):
        if v5 == 1 or v5 == 2*u5-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
output ::
Enter number of rows : 5
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
'''