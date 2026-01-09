#logical operators in python are used to combine conditional statements. 
# They return a Boolean value (True or False) based on the evaluation of the combined conditions.
# The common logical operators in Python are:
# 1️⃣ and: Returns True if both conditions are True.
# 2️⃣ or: Returns True if at least one of the conditions is True.
# 3️⃣ not: Returns True if the condition is False (negates the condition).
# Let's see some examples of logical operators in Python.


# Example of and operator
a = 10
b = 5
c = 15
print((a > b) and (c > a))  # True because both conditions are True
print((a > b) and (c < a))  # False because the second condition is False 



# Example of or operator
a = 10
b = 5
print((a > b) or (a < b))  # True because at least one condition is True
print((a < b) or (a == b))  # False because both conditions are False


# Example of not operator


a = 10
b = 5
print(not(a > b))  # False because the condition is True, so not True is False
print(not(a < b))  # True because the condition is False, so not False is True



# You can use these logical operators in conditional statements to create more complex conditions.



age = int(input("Enter your age:"))
citizenship = input("Enter your citizenship (yes/no):").lower()
if (age >= 18) and (citizenship == "yes"):  
    print("You are eligible to vote.")
else:   
    print("You are not eligible to vote.")




# In this example, we use the and operator to check if the user's age is 18 or older and if they are a citizen. 
# Depending on the result of the combined conditions, we print whether the user is eligible to vote or not.
# You can also use the or operator to check if at least one condition is met.