class Employee:
    name = "Tushar"
    language = "py"   #This is a class attribute 
    salary = 15000000

    def getInfo(self):
        print(f"The language is  {self.language}. The salary is {self.salary}")
        


Tushar = Employee()
# Tushar.language = "javascript"  #This is an INSTANCE attribute 

Tushar.getInfo()

# SELF PARAMETER

# self refers to the instance of the class. It is automatically passed with a function call
# from an object.