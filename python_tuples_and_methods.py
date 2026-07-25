"""
Author: Mehreen
Topic: Python Tuples and Tuple Methods

This program demonstrates tuple creation, indexing, commonly used tuple methods,
and simple practice exercises using Python tuples.
"""
# -----------------------
# tuple initialization
# -----------------------
tup = ("john",0.9,786,True)
tup1 = ()                   # empty tuple
tup2 = (1,)                 # tuple with one value needds to have comma (,) at the end
print(tup)                  # output ("john",0.9,786,True) 
print(tup1)                 # output ()
print(tup2)                 # output (1,)      
print(type(tup))

# -----------------------
# indexing in tuple
# -----------------------
print(tup[:-1])             # output ('john', 0.9, 786)
print(tup[2:-1])            # output (786,)

# -----------------------
# commonly used methods of tuples
# -----------------------
no = tup.count("john")      # counts the number of occurrences of a particular value in the tuple
print(no)                   # 1
n1 = tup.index(786)         # returns the first index of a value in tuple
print(n1)                   # 2

print(len(tup))             # returns the number of elements in the tuple

my_tup = (1,3,2)
repeat = my_tup*3           # repeats the tuple three times
print(repeat)

print(3 in my_tup)          # Checks whether an element exists in the tuple and returns True or False.

a, b, c = my_tup          # unpack the tuple into three variables
print(a , b , c)

# -----------------------
# tuple practice questions
# -----------------------
# check whether a value changes in tuple or not

a = (1,2,3,4)
#a[0]=5                     # this cannot happen as tuples are immutable

# count the number of zeros in the following tuple (7,0,8,0,0,9)

a1=(7,0,8,0,0,9)
n=a1.count(0)
print(n)

# -----------------------
# End of program
# -----------------------