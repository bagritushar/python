# Sometimes we want to play PUBG on our phone if the day is Sunday.
# Sometimes we order Ice Cream online if the day is sunny.
# Sometimes we go hiking if our parents allow.
# All these are decisions which depend on a condition being met.
# In python programming too, we must be able to execute instructions on a condition(s)
# being met.
# This is what conditionals are for!

# Let's see how we can use conditionals in Python.
# The syntax for conditionals in Python is as follows:
# if <condition>:
#     <code to be executed if condition is true>
# elif <another condition>:
#     <code to be executed if the another condition is true>
# else:
#     <code to be executed if none of the above conditions are true>
# Note: elif and else are optional.
# Let's see some examples of conditionals in Python.
a = int(input("Enter your age:"))

if (a>=18):
    print("you are above the age of consent")
    print("Good for you")

elif (a<0):
    print(("you are entering an invalid age"))
    


else:
    print("you are below the age of consent")

# In the above example, we check if the age entered by the user is greater than 18.
# If the condition is true, we print "you are above the age of consent".

print("End of program")


# Syntax:

# if (condition1): # if condition1 is True
# print ("yes")
# elif(condition2): # if condition2 is True
# print("no")
# else: # otherwise
# print("maybe") 

