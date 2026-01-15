from array import *

arr1 = array('i', [1,2,3,4,5,6]) # Time: O(N), Space: O(N). Note: Creating empty array is T: O(1), S: O(1)
arr2 = array('d', [1.3, 1.5, 1.6]) # As above

arr1.remove(4) # Time: O(n), Space: O(1)
# remove(x) will remove the element 'x', not the element at index 'x'

print(arr1)

# print(arr2)

# arr1.insert(2, 9)
# print(arr1)

# def traverseArray(array):
#    for i in array: # Time: O(n), Space: O(1)
#        print(i)    # Time: O(1), Space: O(1)


# traverseArray(arr2)


#def accessElement(array, index):
#    if index >= len(array):                         # Time: O(1), Space: O(1)
#        print("ERROR: No element at this index")    # Time: O(1), Space: O(1)
#    else:
#        print(array[index])                         # Time: O(1), Space: O(1)

#accessElement(arr1, 6)


