"""
Author: Mehreen
Topic: Python String Slicing and String Methods

This program demonstrates basic string slicing and commonly used string methods.
"""


# -----------------------
# String Slicing
# -----------------------
text = "John Abraham"
print(text[0:len(text)])     # display the complete string
print(text[4:-1])            # display string characters from 4 index to second-last character
print(text[ :-1])            # display all characters except the last one
print(text[0:])              # display the complete string 

# -----------------------
# String Methods
# -----------------------
num = 123
print(len(text))             #display length of string
print(str(num))              #type cast integer value to string

# -----------------------
# Case Conversion
# -----------------------
print(text.lower())          # convert string to lower case
print(text.upper())          # convert string to upper case
print(text.capitalize())     # convert first letter of string to capital
print(text.title())          # convert first letter of every word in string
print(text.swapcase())       # convert to opposite case

# -----------------------
# Replace & Trim
# -----------------------
print(text.replace("Abraham","prince"))   #replaces all old string with new *syntax replace("old","new")
print(text.strip())          # removes starting and ending spaces ->works only if string have spaces
print(text.lstrip())         # removes leading spaces
print(text.rstrip())         # removes ending spaces

# -----------------------
# Split & Join
# -----------------------
print(text.split())          # splits string by separator or whitespace
print(text.rsplit())         # splits string but from right side
words = text.split()
print("-".join(words))       # join words using "-"

# -----------------------
# Testing Methods
# -----------------------
print("johnabraham".isalpha())      # returns True if the string contains only letters
# ->works only if the string have no spaces

# -----------------------
# Formatting
# -----------------------
print(f"brilliant student ever {text} .")     # f-string inserts the value of a variable into a string

# -----------------------
# Searching
# -----------------------
print(text.find("m"))          # finds and gives index of a particular item in string

# End of program