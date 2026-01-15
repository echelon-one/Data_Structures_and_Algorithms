import array


my_array1 = array.array('i', [1,2,3,4])

def linear_search(arr, target):
    for i in range(len(arr)):       # Time: O(n), Space: O(1)
        if arr[i] == target:        # Time: O(1), Space: O(1)
            return i                # Time: O(1), Space: O(1)
    return -1                       # Time: O(1), Space: O(1)

print(linear_search(my_array1, 5))
