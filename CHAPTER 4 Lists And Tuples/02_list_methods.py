friends = ["apple", "banana", "cherry", 5, 345.67, False, "Tushar", "Pragya"]

print(friends)

friends.append("Tushar")  # Adding an element at the end of the list
print(friends)
#append():-  method adds a single element to the end of the list. means element will be added at last position of list.
friends.insert(1, "Mango")  # Inserting an element at index 1
print(friends)
friends.insert(0, "kiwi")  # Inserting an element at index 0
print(friends)
#insert():- method inserts an element at a specified index in the list. It shifts the existing elements to the right to accommodate the new element.
friends.remove("kiwi")  # Removing the element "kiwi" from the list
print(friends)
#remove():- method removes the first occurrence of a specified element from the list. If the element is not found, it raises a ValueError.
friends.pop()  # Removing the last element from the list        
print(friends)
#pop():- method removes and returns the last element of the list by default. It can also remove an element at a specified index if provided.
friends.pop(2)  # Removing the element at index 2       
print(friends)
#pop(index):- method removes and returns the element at the specified index from the list.
friends.sort(key=str)  # Sorting the list in ascending order (only works if all elements are of the same data type)
print(friends)  

#sort():- method sorts the elements of the list in ascending order by default. It can also take a key function to customize the sorting behavior.
# Note: The sort() method will raise an error if the list contains elements of different data types that cannot be compared.
friends.reverse()  # Reversing the order of elements in the list
print(friends)
#reverse():- method reverses the order of elements in the list in place.    
# Note: The reverse() method does not sort the list; it simply reverses the current order of elements.
# Note: The insert() method allows you to add an element at a specific index, shifting existing elements to the right.
# Note: The remove() method only removes the first occurrence of the specified element. If there are multiple occurrences, only the first one will be removed.
# Note: The pop() method can be used to remove and return an element at a specific index, or the last element if no index is provided.
# Note: The sort() method sorts the list in place and does not return a new sorted
# list. It raises an error if the list contains elements of different data types that cannot be compared.
# Note: The reverse() method reverses the order of elements in the list in place and does not return a new list.
# Note: The append() method adds an element to the end of the list without needing to specify an index.
# Note: The append() method is used to add a single element to the end of the

# list, while the insert() method allows you to add an element at a specific index.
# Note: The remove() method removes the first occurrence of a specified element from the list, while the pop() method removes an element at a specified index or the last element by default.
# list without needing to specify an index.
# Note: The append() method is used to add a single element to the end of the
# list, while the insert() method allows you to add an element at a specific index.

# Note: The remove() method removes the first occurrence of a specified element from the list, while the pop() method removes an element at a specified index or the last element by default.
# Note: The sort() method sorts the list in place and does not return a new sorted

# list. It raises an error if the list contains elements of different data types that cannot be compared.
# Note: The reverse() method reverses the order of elements in the list in place and does not return a new list.    
# Note: The append() method adds an element to the end of the list without needing to specify an index.# Note: The append() method is used to add a single element to the end of the
# list, while the insert() method allows you to add an element at a specific index.
# Note: The remove() method removes the first occurrence of a specified element from the list, while the pop() method removes an element at a specified index or the last element by default.
# Note: The sort() method sorts the list in place and does not return a new sorted
# list. It raises an error if the list contains elements of different data types that cannot be compared.
# Note: The reverse() method reverses the order of elements in the list in place and
# does not return a new list.   
# Note: The append() method adds an element to the end of the list without needing to specify an index.# Note: The append() method is used to add a single element to the end of the
# list, while the insert() method allows you to add an element at a specific index.
# Note: The remove() method removes the first occurrence of a specified element from the list, while the pop() method removes an element at a specified index or the last element by default.
# Note: The sort() method sorts the list in place and does not return a new sorted  
# list. It raises an error if the list contains elements of different data types that cannot be compared.
# Note: The reverse() method reverses the order of elements in the list in place and    # does not return a new list.
# Note: The append() method adds an element to the end of the list without needing to specify an index.# Note: The append() method is used to add a single element to the end of the  
l1 = [23,25,41,25,12,2,1,0,15,10,9,7,8,21]
l1.sort()
print(l1)
l1 = [23,25,41,25,12,2,1,0,15,10,9,7,8,21]
print(l1)
l1.reverse()

print(l1)
# Some commonly used list methods are:  
l1 = [23,25,41,25,12,2,1,0,15,10,9,7,8,21]
l1.sort()
print(l1)
l1.insert(3,8)  
print(l1)

 
# l1.sort(): updates the list to [1,2,7,8,15,21]
# • l1.reverse(): updates the list to [15,21,2,7,8,1]
# • l1.append(8): adds 8 at the end of the list
# • l1.insert(3,8): This will add 8 at 3 index
# • l1.pop(2): Will delete element at index 2 and return its value.
# • l1.remove(21): Will remove 21 from the list. 