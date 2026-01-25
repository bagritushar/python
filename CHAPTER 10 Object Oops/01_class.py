class Employee:
    name = "Tushar"
    language = "py"   #This is a class attribute 
    salary = 15000000


Tushar = Employee()
Tushar.name = "Tushar"  #This is an INSTANCE attribute 
print(Tushar.name, Tushar.name, Tushar.language)

Rohan = Employee()
Rohan.name = "Rohan"
print(Rohan.name, Tushar.name, Tushar.language)


# Here name is object attributes and salary and language are class attributes as they directly belong to the class.

# INSTANCE ATTRIBUTES

# An attribute that belongs to the Instance (object). Assuming the class from the previous
# example: