# Relational Operators in Python are used to compare two values. They return a Boolean value (True or False) based on the comparison. Here are the common relational operators:
# == (equal to)
# != (not equal to)
# > (greater than)
# < (less than)
# >= (greater than or equal to)
# <= (less than or equal to)
#example 
# Equal to ==
a = 10
b = 10

print(a == b) 

# 2️⃣ Not equal to !=
a = 10
b = 5

print(a != b)  

# 3️⃣ Greater than >
a = 10
b = 7

print(a > b)    # True
 

# 4️⃣ Less than <
a = 10
b = 7

print(a < b)    # False

# 5️⃣ Greater than or equal to >=
a = 10
b = 10
print(a >= b)   # True

# 6️⃣ Less than or equal to <=
a = 10
b = 15
print(a <= b)   # True

# You can use these relational operators in conditional statements to make decisions based on comparisons.
age = int(input("Enter your age:"))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
# In this example, we use the greater than or equal to (>=) operator to check if the user's age is 18 or older. 
# Depending on the result of the comparison, we print whether the user is an adult or a minor.
# You can also combine multiple relational operators using logical operators (and, or, not) to create more complex conditions.





