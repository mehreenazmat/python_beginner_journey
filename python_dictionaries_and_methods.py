"""
Author: Mehreen
Topic: Python Dictionaries and Dictionary Methods

This program demonstrates dictionary creation, accessing values,
commonly used dictionary methods, and basic dictionary operations.
"""

# -----------------------
# dictionary initialization
# -----------------------
student = {                         #dictionary stores multiple datatypes and is mutable
 "name": "John",
 "city": "Florida",
 "marks": [100, 45, 89]
}
print(student)
# output :: {'name': 'John', 'city': 'Florida', 'marks': [100, 45, 89]}
print(student["city"])            # this is used to access a particular key value
# output :: Florida
print(type(student))
# output :: <class 'dict'>
print(type(student["marks"]))
# output :: <class 'list'>
print(student["marks"][0])        # this prints the value of list marks present at 0 index
# output :: 100

# -----------------------
# methods of dictionaries
# -----------------------
# get() method
print(student.get("name"))        # used to get a specific key's value
# output :: "John"
print(student.get("age"))
# output :: none                  # as no key is age
print(student.get("marks")[1])    # used to get a specific value of list in dictionary
# output :: 45

# key() method
print(student.keys())             # returns keys of the dictionary
# output :: dict_keys(['name', 'city', 'marks'])

# values() method
print(student.values())          # returns values of the dictionary
# output :: dict_values(['John', 'Florida', [100, 45, 89]])

# item() method
print(student.items())           # returns items of the dictionary as tuples
# output :: dict_items([('name', 'John'), ('city', 'Florida'), ('marks', [100, 45, 89])])

# update() method
student.update({"age": 21, "city": "New York"}) # used for adding new value and changing old
print(student)
# output :: {'name': 'John', 'city': 'New York', 'marks': [100, 45, 89], 'age': 21}

# pop() method 
age = student.pop("age")         # removes an item from dict and returns the removed value
print(age)
# output :: 21
print(student)
# output :: {'name': 'John', 'city': 'New York', 'marks': [100, 45, 89] }

# popitem() method
student.popitem()                # removes and returns the last inserted key-value pair
print(student)
# output :: {'name': 'John', 'city': 'New York'}

# clear() method
student.clear()                  # removes everything from the dictionary
print(student)
# output :: {}
# copy() method                  # copies a whole dictionary to another
# in operator                    # checks whether a key exists in the dictionary

print(student.get("name1"))
# output :: none                  # if no key value matches it returns none
# print(student["name1"])         # if no key value matches error occurs
# output :: error

# -----------------------
# End of program
# -----------------------