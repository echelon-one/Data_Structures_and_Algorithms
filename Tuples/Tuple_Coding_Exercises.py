# CODING EXERCISE 16: Sum and Product

# Write a function that calculates the sum and product of all elements in a tuple of numbers.

input_tuple = (1, 2, 3, 4)

# Define a function called "sum_product" that takes a tuple "input_tuple" as an argument.
def sum_product(input_tuple):
    # Initialize a variable "sum_result" to store the sum of the elements in the tuple.
    # Set its initial value to 0
    sum_result = 0
    # Initialize a variable "product_result" to store the product of the elements in the tuple.
    # Set its initial value to 1
    product_result = 1
    # Start a for loop that iterates through each element "num" in the tuple "input_tuple".
    for num in input_tuple:
        # Add the current element "num" to the "sum_result".
        sum_result += num
        # Multiply the current element "num" with the "product_result".
        product_result *= num
    # After the loop is done, return a tuple containing the "sum_result" and "product_result".
    return sum_result, product_result
    
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)  # Expected output: 10, 24

# TIME COMPLEXITY:
# Overall time complexity of the function is O(n) because the loop iterates through each element in the tuple once.
# The rest of the operations have constant time complexity O(1). 

# SPACE COMPLEXITY:
# The overall space complexity is O(1) because the function uses a constant amount of additional memory to store the sum and product, regardless of the size of the input tuple.




# CODING EXERCISE 17: Elementwise Sum

# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Solution 1
def tuple_elementwise_sum(tuple1, tuple2):
    
    return tuple(map(sum, zip(tuple1, tuple2)))

# Solution 2

# Define a function called "tuple_elementwise_sum" that takes two tuples "t1" and "t2" as arguments.
def tuple_elementwise_sum(t1, t2):
    # Check if the lengths of the input tuples are not equal.
    if len(t1) != len(t2):
        # If the lengths of the tuples are not equal, raise a ValueError with a descriptive message.
        raise ValueError("Input tuples must have the same length.")
 
    # Use the zip() function to pair corresponding elements of the input tuples,
    # then use a generator expression to compute the element-wise sum,
    # and finally pass the generator expression to the tuple() constructor to create a new tuple with the sums.
    result = tuple(a + b for a, b in zip(t1, t2))
    # Return the resulting tuple containing the element-wise sums.
    return result

output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)  # Expected output: (5, 7, 9)

# TIME COMPLEXITY:
# Overall time complexity of the function is O(n) because it iterates through each pair of elements in the input tuples once. 

# SPACE COMPLEXITY:
# The overall space complexity is O(n) because the function creates a new tuple with the same length as the input tuples to store the element-wise sums.






# CODING EXERCISE 18: Insert at the Beginning

# Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.

input_tuple = (2, 3, 4)
value_to_insert = 1

# My Solution

def insert_value_front(input_tuple, value_to_insert):
    newTuple = (value_to_insert,)
    return tuple(newTuple + input_tuple)



# Official Solution

# Define a function called "insert_value_at_beginning" that takes a tuple "input_tuple" and a value "value_to_insert" as arguments.
def insert_value_at_beginning(input_tuple, value_to_insert):
    # Create a new tuple with the given value as the first element and concatenate the original tuple "input_tuple" to it.
    # THE COMMA AFTER THE VALUE IS NECESSARY TO CREATE A SINGLE-ELEMENT TUPLE!!
    # Return the new tuple.
    return (value_to_insert,) + input_tuple

output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)  # Expected output: (1, 2, 3, 4)


# TIME COMPLEXITY:
# The overall time complexity of the function is O(n) because it iterates through the elements of the input tuple once to create a new tuple. 

# SPACE COMPLEXITY:
# The overall space complexity is O(n) because it creates a new tuple with n+1 elements.



# CODING EXERCISE 19: Concatenate
# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.

input_tuple = ('Hello', 'World', 'from', 'Python')

# My Solution
def concatenate_strings(input_tuple):
    output_string = ""
    for i in input_tuple:
        output_string += i + " "
    return output_string[:-1]


# Official Solution

# Define a function called "concatenate_strings" that takes a tuple of strings "input_tuple" as an argument.
def concatenate_strings(input_tuple):
    # Use the join() method on a space character to concatenate the strings in the input tuple "input_tuple" with a space as the separator.
    # Return the resulting concatenated strings.
    return ' '.join(input_tuple)

output_string = concatenate_strings(input_tuple)
print(output_string)  # Expected output: 'Hello World from Python'

# TIME COMPLEXITY:
# The overall time complexity of the function is O(n) because it iterates through the strings in the input tuple once to create a new concatenated string. 

# SPACE COMPLEXITY:
# The overall space complexity is O(n) because it creates a new concatenated string with the length equal to the sum of the lengths of the strings in the input tuple plus the spaces in between.





# CODING EXERCISE 20: Diagonal

# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Official Solution
# Define a function called "get_diagonal" that takes a tuple of tuples "input_tuple" as an argument.
def get_diagonal(tup):
    # Use a generator expression to iterate through the indices i from 0 to length of the input tuple minus one,
    # and select the diagonal elements by indexing the inner tuples with the same index i.
    # Create a new tuple containing the selected diagonal elements and return it.
    return tuple(tup[i][i] for i in range(len(tup)))

output_tuple = get_diagonal(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9)

# TIME COMPLEXITY: 
# The overall time complexity of the function is O(n) because it iterates through the indices of the input tuple once to create a new tuple with the diagonal elements. 

# SPACE COMPLEXITY:
# The overall space complexity is O(n) because it creates a new tuple containing the diagonal elements, which has a length equal to the length of the input tuple.



# CODING EXERCISE 21: Common Elements

# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

# My Solution
def common_elements(tuple1, tuple2):
    newList = []
    for i in tuple1:
        for j in tuple2:
            if i == j:
                newList.append(i)
    output_tuple = tuple(newList)
    return output_tuple


# Official Solution
# Define a function called "common_elements" that takes two tuples "tuple1" and "tuple2" as arguments.
def common_elements(tuple1, tuple2):
    # Convert both input tuples into sets using the set() constructor,
    # then use the set intersection operator '&' to find the common elements between the two sets.
    # Convert the resulting set of common elements back to a tuple and return it.
    return tuple(set(tuple1) & set(tuple2))

output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)

# TIME COMPLEXITY:
# The overall time complexity of the function is O(n).

# SPACE COMPLEXITY:
# The overall space complexity is also O(n), where n is the length of the input tuples.
