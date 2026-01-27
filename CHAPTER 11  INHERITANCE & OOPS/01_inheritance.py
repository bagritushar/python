class employee :
    company = "ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary} ")


# class programmer:
#     company = "ITC Infotech" 
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary} ")

class programmer(employee): #Inheritance is a way of creating a new class from an existing class.
    company = "ITC Infotech"
    def ShowLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = employee()
b = programmer()

print(a.company , b.company)



#TYPES OF INHERITANCE
# • Single inheritance
# • Multiple inheritance
# • Multilevel inheritance