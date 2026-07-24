"""
Author: Mehreen
Topic: Python Lists and List Methods

This program demonstrates basic list operations, commonly used list methods,
and simple practice exercises using Python lists.
"""

# -----------------------
# list initialization
# -----------------------
l1= [ "john" , "is" , 21 , 0.01 , "years" , "old" ]
print(l1)

# -----------------------
# commonly used methods in lists
# -----------------------
l1.append("hehehehe...")       # append adds a value at the end of list
print(l1)

l1.extend("meow")              # adds each character of the string as separate elements
print(l1)

l1.insert(0,6)                 # adds a value at a specific index #syntax insert(index,value to be added)
print(l1)

l1.remove("hehehehe...")
print(l1)                      # removes specific value

l1.pop(-1)
print(l1)                      # removes specific value and returns the removed value

print(l1.index("john"))        # returns the index of the value

print(l1.count("john"))        # returns the number of times a value is in a list

l2 = [0,4,2,6,5,1,8]
print(sorted(l2))              # sorts the list in ascending order by default.
                               # for descending order, use reverse=True.

l2.reverse()                   # reverses the order of list
print(l2)

l3 = l2.copy()                 # copies list 
print(l3)
l3.clear()                     # clears the whole list
l1.clear()
print(l1)
print(l2)
print(l3)

# -----------------------
# practice questions
# -----------------------
# enter 7 fruits from users and store them in a list

fruits = []
f1 = input("Enter a fruit here: ")
fruits.append(f1)
f2 = input("Enter a friut here: ")
fruits.append(f2)
f3 = input("Enter a friut here: ")
fruits.append(f3)
f4 = input("Enter a fruit here: ")
fruits.append(f4)
f5 = input("Enter a friut here: ")
fruits.append(f5)
f6 = input("Enter a friut here: ")
fruits.append(f6)
f7 = input("Enter a fruit here: ")
fruits.append(f7)
print(f"Fruits entered by user are :{fruits}")

# write a program that accepts marks of 7 students in sorted way

marks = []
f1 = input("Enter a mark here: ")
marks.append(int(f1))
f2 = input("Enter a mark here: ")
marks.append(int(f2))
f3 = input("Enter a mark here: ")
marks.append(int(f3))
f4 = input("Enter a mark here: ")
marks.append(int(f4))
f5 = input("Enter a mark here: ")
marks.append(int(f5))
f6 = input("Enter a mark here: ")
marks.append(int(f6))
f7 = input("Enter a mark here: ")
marks.append(int(f7))

print(f"Marks are :{sorted(marks)}")

#print the sum of 4 elements inn a list
l = [1,2,3,4]

print(sum(l))                # this function prints the sum of elements of a list