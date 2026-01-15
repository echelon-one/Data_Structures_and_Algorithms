# CREATING A TUPLE:
firstTuple = ('a', 'b', 'c', 'd', 'e')

# Use a comma if only one element in tuple so interpreter can differentiate between tuple and a string
secondTuple = ('a',)


# HOW TO ACCESS ELEMENTS IN A TUPLE?

newTuple = ('a', 'b', 'c', 'd', 'e')

# Tuple elements are stored in memory contiguously. So  bracket [] operator and index can be used to access them.
# Syntax is tupleName[indexNumber]
print(newTuple[1]) # This will print 'b'

# Slice [:] operator can also be used 
# Syntax is tupleName[leftIndex:rightIndex]
print(newTuple[1:3]) # This will print ('b', 'c') as index 3 is not included. Leave left and right index blank [:] to get all elements



# HOW TO TRAVERSE THROUGH A TUPLE

for i in newTuple: 
    print(i)

for i in range(len(newTuple)):
    print(newTuple[i]) 

# TIME COMPLEXITY: O(n). 
# SPACE COMPLEXITY: O(1).




# HOW TO SEARCH FOR AN ELEMENT IN A TUPLE?

# Use in operator
print('a' in newTuple) # Will return boolean. T: O(n)

# Use index() method
print(newTuple.index('a')) # Will return index of argument. T: O(n)

# Use a function
def searchTuple(p_tuple, element):
    for i in range(0, len(p_tuple)):
        if p_tuple[i] == element:
            return f"The element is found at index: {i}"
    return f"The element is not found."

print(searchTuple(newTuple, 'f'))

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1).





# TUPLE OPERATIONS/FUNCTIONS
myTuple = (1,4,3,2,5,2)
myTuple1 = (1,2,6,9,8,7)

# Use the + operator to concatenate the two tuples
print(myTuple + myTuple1)

# Use the * operator to repeat
print(myTuple * 4)


# Use the count() method to count the number of times an element appears in a tuple
print(myTuple.count(2))


# Use the len() function to return the number of elements in a tuple
print(len(myTuple)) 


# Use the max()/min() functions to return the maximum or minimum element
print(max(myTuple1))
print(min(myTuple1))


# Use the tuple() function to convert a list to a tuple
myList = [1,5,7,6]
print(tuple(myList))


# Using a generator expression. Syntax: n for _, n in tupleName
init_tuple = [(0,1),(1,2),(2,3)]
# The expression iterates through each tuple in init_tuple and extracts the second element of each tuple (denoted by n),
# discarding the first element (denoted by _).
# The generator expression produces the following sequence of values: 1,2,3.
# The sum() function calculates the sum of the generated values: 1+2+3, which is 6.
# result is assigned the value 6.
result = sum(n for _, n in init_tuple)
# The print function then prints the result.
print(result)




# TUPLES VS LISTS

# The main difference is that:
# TUPLES ARE IMMUTABLE (can't be changed), whereas 
# LISTS ARE MUTABLE (can be changed)

# We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
# Iterating through a tuple is faster than with a list.
# Tuples that contain immutable elements can be used as a key for a dictionary.
# If you have data that doesn't change, implementing it as a tuple will guarantee that it remains write-protected.

list1 = [0,1,2,3,4,5,6,7]

list1[1] = 3 # This will change the element at index 1 to 3
print(list1)

list1 = [7,6,5,4,3,2,1,0] # This will reassign all elements in list1 to the new elements
print(list1)

del list1[0] # This will delete the element at index 0
print(list1)


# If we try the same operations on a tuple...
tuple1 = 0,1,2,3,4,5,6,7

# tuple1[1] = 3 # This will throw an error as a tuple does not support assignment of a single element
print(tuple1)

# However we can reassign all elements in a tuple...
tuple1 = 4,5,6,7,8
print(tuple1)

# We can't use the del() operator to delete a single element in a tuple...
# del tuple1[0] # This will throw an error

# but we can use the del() operator to delete an entire tuple...
# del tuple1
print(tuple1)

# We can use the index() method
tuple1 = 0,1,2,3,4,5,6,7
print(tuple1.index(1))

# and the count() method
print(tuple1.count(2))

# Tuples can be stored in lists:
list1 = [(1,2), (9,0), (2,4)]
print(list1)

# Lists can be stored in tuples.
tuple1 = ([1,2], [3,4], [5,6])
print(tuple1)

# Both tuples and lists can be nested




# TIME AND SPACE COMPLEXITY IN PYTHON TUPLES

#----------------------------------------------------------------------------
#       OPERATION           |   TIME COMPLEXITY     |   SPACE COMPLEXITY    |
#---------------------------|-----------------------|-----------------------|
# Creating a Tuple          |       O(1)            |       O(n)            |
# Traversing a given Tuple  |       O(n)            |       O(1)            |
# Accessing a given element |       O(1)            |       O(1)            |
# Searching a given element |       O(n)            |       O(1)            |
#----------------------------------------------------------------------------







