# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]) # Time: O(nn)
print(twoDArray)

# insert new column or row at index 0
#newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis=1) # axis parameter: axis=1 specifies column, axis=0 specifies row
#print(newTwoDArray)

# append new row to end of array - note there is no index parameter specified here, just the axis.
#newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0) # axis parameter: axis=1 specifies column, axis=0 specifies row
#print(newTwoDArray)
# Time complexity is O(mn) where m is number of rows and n is number of columns, but if no of rows and columns are equal it is quadratic





# ACCESSING AN ELEMENT OF 2D ARRAY
# a[i][j] where a is name of array, i is row index and j is column index

# Function to access 2D Array elements
def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]): # 0 index specifies column and not row length. Time/Space complexity O(1)
        print("Incorrect index") # Time/Space complexity O(1)
    else:
        print(array[rowIndex] [colIndex])  # Time/Space complexity O(1)

accessElements(twoDArray, 2, 3)




# TRAVERSAL OF 2D ARRAY

#
def traverseTDArray(array):
    # First traverse through rows
    for i in range(len(array)): # Time complexity: O(mn) where m is number of rows and n is number of columns, but if no of rows and columns are equal it is quadratic
        # Then for each row visit column
        for j in range(len(array[0])): # Time complexity: O(n) where n is number of columns
            print(array[i][j]) # Time complexity: O(1)

traverseTDArray(twoDArray)
# Space complexity is O(1)




# SEARCHING A 2D ARRAY USING LINEAR SEARCH
def searchTDArray(array, target):
    # First traverse through rows
    for i in range(len(array)): # Time complexity: O(mn) but if no of rows and columns are equal it is quadratic
        # For each row visit each column
        for j in range(len(array[0])): # Time complexity: O(n) where n is the number of columns
            if array[i][j] == target: # Time complexity: O(1)
                return 'The value is located at index: ' + "ROW:" +str(i) + " " + "COLUMN:"+str(j)
    return 'The element is not found'

print(searchTDArray(twoDArray, 73))
# Space complexity is O(1)




# DELETING A ROW OR COLUMN FROM A 2D ARRAY USING NUMPY DELETE FUNCTION
# Create a new array that excludes the deleted row or column - Time and Space complexity is O(mn) where m is the number of columns and n is the number of rows

newTDArray = np.delete(twoDArray, 0, axis=0) # Index 0, axis=0 will delete the first row of the array. Index 0, Axis=1 will delete the first column. Index 1, axis=1 will delete the second column and so on.
print(newTDArray)





# TIME AND SPACE COMPLEXITY OF 2D ARRAY

# OPERATION                             | TIME COMPLEXITY   | SPACE COMPLEXITY  |
# -------------------------------------------------------------------------------
# Creating an empty array               |       O(1)        |       O(1)        |
# Creating an array with elements       |       O(mn)       |       O(mn)       |
# Inserting a column/row in an array    |       O(mn)       |       O(mn)       |
# Traversing a given array              |       O(mn)       |       O(1)        |
# Accessing a given cell                |       O(1)        |       O(1)        |
# Searching a given value               |       O(mn)       |       O(1)        |
# Deleting a column/row                 |       O(mn)       |       O(mn)       |






# WHEN TO USE/AVOID ARRAYS

# WHEN TO USE:
# - To store multiple variables of the same type
# - Random Access (e.g. When we want to access random numbers)

# WHEN TO AVOID:
# - Storing same data type elements
# - When we need to reserve memory

