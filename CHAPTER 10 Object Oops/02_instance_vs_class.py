class Employee:
    name = "Tushar"
    language = "py"   #This is a class attribute 
    salary = 15000000


Tushar = Employee()
Tushar.language = "javascript"  #This is an INSTANCE attribute 
print(Tushar.language, Tushar.name, Tushar.language)


# Note: Instance attributes, take preference over class attributes during assignment &
# retrieval.
# When looking up for harry.attribute it checks for the following:

# 1) Is attribute present in object?

# 2) Is attribute present in class?
