"""
Author: Mehreen
Topic: Python File Handling

This program demonstrates basic file handling in Python
using open(), read(), write(), append(), loops,
exception handling, and simple practice programs.
"""

# -----------------------
# File handling 
# -----------------------

# -----------------------
# Reading a file
# -----------------------
with open( "notes.txt" , "r" ) as file:                     # open() opens a file if file does not exists it will generate an error
    notes=file.read()
    print(notes)

# -----------------------
# Writing to a file
# -----------------------
with open( "student.txt" , "w" ) as file:                   # open() with w writes item in the file
    file.write("Name: John\nCourse: Python")
print ("Data successfully written!")

# -----------------------
# Appending data to a file
# -----------------------
with open( "student.txt" , "a" ) as file:                    # open() with a add new item to a file
    file.write("\nCity: Florida\nStatus: Active")
print ("New record appended.")

# -----------------------
# write a program that prints lines of a file loop.
# -----------------------
with open( "student.txt" , "r" ) as file:
    for line in file:
        print(line.strip())

# -----------------------
# try_except method to find files
# -----------------------
try:
    with open( "teachers.txt" , "r" ) as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")

# -----------------------
# practice question
# -----------------------
user_log = input("Enter log message= ")
try:
    with open( "logs.txt" , "a" ) as log:
        log.write(user_log+"\n")
        print("New reccord appended")
except FileNotFoundError :
    print("file does not exist")

try:
    with open( "logs.txt" , "r" ) as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("file does not exist")

# -----------------------
# End of program
# -----------------------