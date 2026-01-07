friends = ["apple", "banana", "cherry", 5, 345.67, False, "Tushar", "Pragya"]

print(friends[0])        # Accessing the first element
print(friends[3])        # Accessing the fourth element
friends[0] = "Grapes"  # Modifying the first element
print(friends[0])

# LIST ARE MUTEABLE (CAN BE CHANGED) 
# Python lists are containers to store a set of values of any data type


# LIST INDEXING 
# 1. A list can be indexed just like a string.
print(friends[-1])       # Accessing the last element using negative indexing
print(friends[-3])       # Accessing the third last element using negative indexing
print(friends[2:5])     # Slicing the list from index 2 to 4