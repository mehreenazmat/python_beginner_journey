"""
Author: Mehreen
Topic: Python Sets Practice

This program demonstrates practice exercises using Python sets
and dictionaries.
"""

# -----------------------
# write a program that contain few urdu words and their english meanings
# -----------------------
data = {
    "larki": "girl",
    "piyari": "pretty",
    "madad": "help",
    "aur": "and",
}
print(data.keys())
word = input("Enter word for meaning :")
print(data[word])

# -----------------------
# write a program to input seven numbers from user and display uniquely at once
# -----------------------
s = set()
n = int(input("Enter a number: "))
s.add(n)
n = int(input("Enter a number: "))
s.add(n)
n = int(input("Enter a number: "))
s.add(n)
n = int(input("Enter a number: "))
s.add(n)
n = int(input("Enter a number: "))
s.add(n)
n = int(input("Enter a number: "))
s.add(n)
n = int(input("Enter a number: "))
s.add(n)
print(s)

# -----------------------
# Can we have 18 ( int ) and "18" ( str ) in a set?
# ----------------------- 
set1 = {18, "18"}
print(set1)
# output :: {18, '18'}
# yes beacause both are different

# ----------------------- 
"""
What will be the length of following string
s1 = set()
s1.add(20)
s1.add(20.0)
s1.add("20")
"""
# ----------------------- 
s1 = set()
s1.add(20)
s1.add(20.0)
s1.add("20")
print(len(s1))
# output :: 2 because 20=20.0 in python

# what would be the type of s2={}
s2 = {}
print(type(s2))
# output :: <class 'dict'>

# -----------------------
# create an empty dictionary and then allow 4 friends to enter their names and their favourite language keeping in mind names are unique
# -----------------------
d1 = {}
name = input("Enter name : ")
lang = input("Enter favourite language")
d1.update({name: lang})
name = input("Enter name : ")
lang = input("Enter favourite language")
d1.update({name: lang})
name = input("Enter name : ")
lang = input("Enter favourite language")
d1.update({name: lang})
name = input("Enter name : ")
lang = input("Enter favourite language")
d1.update({name: lang})
print(d1)

# can you change list inside a set s3={1,8,12,"Harry",[1,2]}
"""
lists are mutable, so they cannot be stored inside a set.
only immutable objects (such as numbers, strings, and tuples)
can be stored in a set.
"""

# -----------------------
# End of program
# -----------------------