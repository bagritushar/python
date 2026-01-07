# A variable is the name given to a memory location in a program. For example. 

a= 30 # variables = container to store a value.
b= "harry" # keywords = reserved words in python
c= 71.22 # identifiers = class/function/variable name


# DATA TYPES
# Primarily these are the following data types in Python:
# 1. Integers
# 2. Floating point numbers
# 3. Strings
# 4. Booleans
# 5. None
# Python is a fantastic language that automatically identifies the type of data for us.
# a= 71 # identifies a as class <int>
# b=88.44 # identifies b as class <float>
# name= "harry" # identifies name as class <str>


# RULES FOR CHOOSING AN IDENTIFIER
# • A variable name can contain alphabets, digits, and underscores.
# • A variable name can only start with an alphabet and underscores.
# • A variable name can’t start with a digit.
# • No while space is allowed to be used inside a variable name.
# Examples of a few variable names are: harry, one8, seven, _seven etc.
# OPERATORS IN PYTHON
# Following are some common operators in python:
# 1. Arithmetic operators: +, -, *, / etc.
# 2. Assignment operators: =, +=, -= etc.
# 3. Comparison operators: ==, >, >=, <, != etc.
# 4. Logical operators: and, or, not
# 5. Bitwise operators: &, |, ^, ~, <<, >> etc.
# 6. Membership operators: in, not in
# 7. Identity operators: is, is not
# COMMENTS IN PYTHON
# Comments are used to explain code and make it more readable.  
# In Python, comments start with a # symbol and extend to the end of the line.
# This is a single line comment

''' 
This is a
multi-line comment
''' 
# You can also use multi-line strings as comments
"""
This is another way
to write multi-line comments
"""
# PRINTING IN PYTHON
# The print() function is used to display output in Python.
print("Hello, World!")  # This will print Hello, World! to the console
print(a)  # This will print the value of variable a
print(b)  # This will print the value of variable b
print(c)  # This will print the value of variable c
print(a, b, c)  # This will print all three variables in one line
print(a)
print(b)
print(c)  # This will print each variable on a new line
print("The value of a is:", a)  # This will print a message along with the value of a

# INPUT IN PYTHON
# The input() function is used to take input from the user.
name = input("Enter your name: ")  # This will prompt the user to enter their name
age = input("Enter your age: ")  # This will prompt the user to enter their age
print("Hello, " + name + "! You are " + age + " years old.")
# This will print a greeting message along with the user's name and age

# TYPE CONVERSION IN PYTHON
# You can convert data from one type to another using type conversion functions.
num_str = "123"  # This is a string
num_int = int(num_str)  # Convert string to integer
num_float = float(num_str)  # Convert string to float
print(num_int)  # This will print 123 as an integer
print(num_float)  # This will print 123.0 as a float
# You can also convert numbers to strings
num = 456   
num_str2 = str(num)  # Convert integer to string
print(num_str2)  # This will print "456" as a string    

# BASIC MATH OPERATIONS
x = 10
y = 3
addition = x + y  # Addition
subtraction = x - y  # Subtraction

multiplication = x * y  # Multiplication

division = x / y  # Division
floor_division = x // y  # Floor Division

modulus = x % y  # Modulus
exponentiation = x ** y  # Exponentiation
print("Addition:", addition)
print("Subtraction:", subtraction)

print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)
# This will print the results of various math operations between x and y    
# OUTPUT:
# Addition: 13
# Subtraction: 7

# Multiplication: 30
# Division: 3.3333333333333335
# Floor Division: 3
# Modulus: 1
# Exponentiation: 1000
# END OF THE FILE
