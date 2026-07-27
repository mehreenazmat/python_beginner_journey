"""
Author: Mehreen
Topic: Python Sets and Set Methods

This program demonstrates set creation and commonly used set methods in Python.
"""

# -----------------------
# set is unordered , unindexed collection of unique elements.
# -----------------------
s1 = {1, 2, 3}
print(s1,type(s1))
#output :: {1, 2, 3} <class 'set'>

#for an empty set 
e = set()
print(e,type(e))                # do not use set={} this will create a dictionary
#output :: set() <class 'set'>

# -----------------------
# methods of set
# -----------------------
# add() method
s1.add(4)                       # adds an element to the set
print(s1)                       
#output ::  {1, 2, 3, 4}

# remove() method 
s1.remove(4)                    # removes an element from the set
print(s1)                       
#output ::  {1, 2, 3}

# discard() method
s1.discard(4)             # removes an element from the set. If the element is not present, no error occurs.
print(s1)                       
# output ::  {1, 2, 3}

# pop() method
s1.pop()                  # removes and returns an arbitrary element from the set
print(s1)
#output :: {2, 3}

# clear() method
s1.clear()                # removes all elements from the set
print(s1)
# output :: set()

# update() method
s1.update([1, 2, 3])        # adds multiple elements to set
print(s1)
# output :: {1, 2, 3}

# union() method
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))           # returns a new set containing all unique elements from both sets.
# output :: {1, 2, 3, 4, 5}

# intersection method
a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))         # displays the common elements of both sets
# output :: {3}
# difference() method
a = {1, 2, 3}
b = {3, 4, 5}
print(a.difference(b))           # returns elements that are present in set a but not in set b.
# output :: {1, 2}

# symmetric_difference() method
a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b)) # displays those elements that are not common in both sets
# output :: {1, 2, 4, 5}

# issubset() method
a1 = {1, 2}
b1 = {1, 2, 3}
print(a1.issubset(b1))           # checks whether all elements of a are present in b.
# output :: True

# issuperset() method
a = {1, 2, 3}
b = {3, 4, 5}
print(a.issuperset(b))           # checks whether set a contains all elements of set b.
# output :: False

# isdisjoint() method
a = {1, 2, 3}
b = {3, 4, 5}
print(a.isdisjoint(b))           # checks if a and b have no same elements
# output :: False                # because they have common element 3

# -----------------------
# End of program
# -----------------------