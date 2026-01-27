class employee:
    company = "ITC"
    name= "Default name"
    def show(self):
      print(f"the name of thr employee is {self.name} and the company is {self.company} ")

class coder:
    language = "python"
    def printlanguage(self):
       print(f"out of all the languages here is your language: {self.language}")




class programmer(employee , coder):
    company = "ITC Infotech"
    def ShowLanguage(self):
      print(f"The name is {self.company} and he is good with {self.language} language")

a = employee()
b = programmer()


b.show()
b.printlanguage()
b.ShowLanguage()



# MULTIPLE INHERITANCE
# Multiple Inheritance occurs when the child class inherits from more than one parent
# classes.

#TYPES OF INHERITANCE
# • Single inheritance
# • Multiple inheritance
# • Multilevel inheritance