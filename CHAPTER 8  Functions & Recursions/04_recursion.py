'''
RECURSION

Recursion is a function which calls itself.
It is used to directly use a mathematical formula as function.
Example:
factorial(n) = n x factorial (n-1)
This function can be defined as follows:
'''

'''
def factorial(n)
if i == 0 or i==1: # base condition which doesn’t call the function
any further
return 1
else:
 return n*factorial(n-1) # function calling itself

'''




'''
This works as follows:


factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1

factorial(n) = n x n-1 x.........3 x 2 x 1

factorial(n) = n * factorial(n-1)


The programmer needs to be extremely careful while working with recursion to ensure
that the function doesn’t infinitely keep calling itself. Recursion is sometimes the most
direct way to code an algorithm.


'''

def factorial(n):
    if (n==1 or n==0):
        return 1
    return  n * factorial(n-1)
n = int(input("Enter a number: "))
print(f"The factorial number is : {factorial(n)}")

# The programmer needs to be extremely careful while working with recursion to ensure
# that the function doesn’t infinitely keep calling itself. Recursion is sometimes the most
# direct way to code an algorithm.