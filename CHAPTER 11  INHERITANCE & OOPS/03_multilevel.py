class Employee:
    a = 1

class programmer(Employee):
    b = 2

class Manager(programmer):
    c = 3

o = Employee()
print(o.a) # print the attribute
# Print (o.a) # Show an error as there is no b attribute in employee class


o = programmer()
print(o.a, o.b)


o = Manager()
print(o.a , o.b, o.c)

#MULTILEVEL INHERITANCE
# When a child class becomes a parent for another child class.