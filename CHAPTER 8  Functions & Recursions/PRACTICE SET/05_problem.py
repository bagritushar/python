# 5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

def pattren(n):
    if(n==0):
       return
    print("*" * n)
    pattren(n-1)

pattren(3)
