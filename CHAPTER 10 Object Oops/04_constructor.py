class Employee:
    name = "Tushar"
    language = "py"   #This is a class attribute 
    salary = 15000000

    def __init__(self , name, salary, language): # dunder method which is automatically called.
        self.name = name
        self.salary = salary
        self.language = language
        print(" I'm creating an object")
        

    def getInfo(self):
        print(f"The language is  {self.language}. The salary is {self.salary}")
        


Tushar = Employee("Tushar","150000000", "py")
# Tushar.language = "javascript"  #This is an INSTANCE attribute 

Tushar.getInfo()




# __INIT__() CONSTRUCTOR


# __init__() is a special method which is first run as soon as the object is created.
# __init__() method is also known as constructor.
# It takes ‘self’ argument and can also take further arguments