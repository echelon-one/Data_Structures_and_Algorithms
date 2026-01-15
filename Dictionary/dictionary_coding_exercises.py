# CODING EXERCISE 10: Count Word Frequency

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 


# Define a function count_word_frequency(words) that takes a list of words as it's input.
def count_word_frequency(words):
    # Initialize an empty dictionary 'word_count' to store the frequency of each word in the list
    word_count = {}
    # Iterate through the list of words using a for loop
    for word in words:
        # For each word use the get() method to retrieve the current count of the word in the 'word_count' dictionary
        # If the word is not yet present in the dictionary, 'get()' returns the default value 0.
        # Then, increment the count by 1 and update the dictionary
        word_count[word] = word_count.get(word, 0) + 1
    # After iterating through all the words, return the 'word_count' dictionary containing the frequencies
    return word_count

count_word_frequency(words)
    
# TIME COMPLEXITY: 
# The time complexity of this exercise is O(n), where n is the number of words in the input list. 
# The loop iterates through each word in the list once, and the dictionary operations (get and update) take constant time, O(1), on average.
# SPACE COMPLEXITY: 
# The space complexity of this exercise is also O(n), where n is the number of unique words in the input list. 
# In the worst case, all words are unique, and the word_count dictionary will have n entries.



# CODING EXERCISE 11: Common Keys
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def merge_dicts(dict1, dict2):
    # Create a copy of 'dict1' named 'result'.
    # This ensures that the original 'dict1' is not modified during the process.
    result = dict1.copy() # TIME AND SPACE COMPLEXITY O(N)
    # Iterate through the key-value pairs of 'dict2' using a for loop.
    # This loop runs for m iterations, where m is the number of elements in 'dict2'.
    for key, value in dict2.items():
        # For each key-value pair: 
        # a. Use the get() method to retrieve the current value associated with the key in the result dictionary. If the key is not present in 'result', get() returns the default value (0).
        # b. Add the value from 'dict2' to the current value (or 0, if the key is not in 'result') and update the 'result' dictionary with the new value for the key. 
        result[key] = result.get(key, 0) + value
    return result

print(merge_dicts(dict1, dict2))

# TIME COMPLEXITY:
# The overall time complexity of this function is O(n + m), where n is the number of elements in dict1 and m is the number of elements in dict2. The copy() method takes O(n) time, and the loop iterates m times with O(1) operations inside the loop.
# SPACE COMPLEXITY:
# The space complexity of this function is O(n + m) in the worst case, where all keys in dict1 and dict2 are distinct, and the merged dictionary has n + m elements. In the best case, where dict1 and dict2 have the same keys, the space complexity is O(n) (or O(m), whichever is larger), as the merged dictionary has the same number of elements as the input dictionaries.





# CODING EXERCISE 12: Key with the highest value.

my_dict = {'a': 5, 'b': 9, 'c': 2}

def max_value_key(my_dict):
    # Call the built-n max() function with the dictionary 'my_dict' as it's first argument
    # and the key=my_dict.get as it's second argument.
    # The max() function iterates through the keys in the dictionary and compares the values associated with each key using the get() mentod.
    # The key parameter specifies a custom function to extract a comparison key from each dictionary key.
    # In this case, the get() method returns the value associated with each key, so the max() function compares the values of the dictionary
    return max(my_dict, key=my_dict.get)

max_value_key(my_dict)

# Time complexity:
# The overall time complexity of this function is O(n), where n is the number of elements in the dictionary my_dict. This is determined by the max() function, which iterates through all the keys in the dictionary.

# Space complexity:
# The space complexity of this function is O(1), as it does not create any additional data structures or store any intermediate values. The max() function only keeps track of the current maximum value and its corresponding key, which requires constant space.






# CODING EXERCISE 13: Reverse Key-Value pairs

# My Solution
my_dict = {'a': 1, 'b': 2, 'c': 3}

def reverse_dict(my_dict):
    reversed = {}
    for key in my_dict:
        temp = key
        key = my_dict[key]
        value = temp
        reversed[key] = value
    return reversed

reverse_dict(my_dict)

# Actual solution
def reverse_dict(my_dict):
    # Use dictionary comprehension to create a new dictionary by iterating through the key-value pairs in the input dictionary 'my_dict' using the items() method.
    # The items() method returns an iterable that produces key-value pairs as tuples.
    # For each key-value pair (k, v) from the input dictionary, the dictionary comprehension creates a new entry in the reversed dictionary with the value v as the key and the key 'k' as the value.
    # The syntax is {v: k for k, v in my_dict.items()}.
    return {v: k for k, v in my_dict.items()}

reverse_dict(my_dict)

# TIME COMPLEXITY:
# The overall time complexity of this function is O(n), where n is the number of elements in the dictionary my_dict. 
# This is determined by the dictionary comprehension, which iterates through all the key-value pairs in the input dictionary.

# SPACE COMPLEXITY:
# The space complexity of this function is O(n), where n is the number of elements in the dictionary my_dict. 
# This is because the function creates a new dictionary with the same number of elements as the input dictionary but with reversed key-value pairs.






# CODING EXERCISE 14: Conditional Filter

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 

# My solution
def filter_dict(my_dict, condition):
    filtered_dict = {}
    for key, value in my_dict.items():
        if condition(key, value):
            filtered_dict[key] = my_dict.get(key, value)
    return filtered_dict



# Actual Solution:
def filter_dict(my_dict, condition):
    # Use dictionary comprehension to create a new dictionary by iterating through the key-value pairs in the input dictionary 'my_dict' using the items() method.
    # The items() method returns an iterable that produces key-value pairs as tuples.
    # For each key-value pair (k, v) from the input dictionary, the dictionary comprehension checks if the condition is met by calling the condition(k, v) function.
    # The condition function takes a key and a value as arguments and returns a boolean value.
    # If the condition is met, the dictionary comprehension creates a new entry in the filtered dictionary with the same key-value pair.
    # The syntax is {k: v for k, v in my_dict.items() if condition(k, v)}
    return {k: v for k, v in my_dict.items() if condition(k, v)}

filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0) 
print(filtered_dict)

# TIME COMPLEXITY:
# The overall time complexity of this function is O(n), where n is the number of elements in the dictionary my_dict. 
# This is determined by the dictionary comprehension, which iterates through all the key-value pairs in the input dictionary.

# SPACE COMPLEXITY:
# The space complexity of this function depends on the number of elements in the filtered dictionary, which in turn depends on the condition function. 
# In the worst case, when all key-value pairs meet the condition, the space complexity is O(n), where n is the number of elements in the dictionary my_dict. In the best case, when no key-value pairs meet the condition, the space complexity is O(1) as the function creates an empty dictionary.






# CODING EXERCISE 15: Same Frequency

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]

# My solution (Actually the permutation solition in FAANG questions)
def check_same_frequency(list1, list2):
    # TODO
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
    

# Official solution:
def check_same_frequency(list1, list2):
    # Define an inner function count_elements(lst) that counts the frequency of elements in a list 'lst.'
    def count_elements(lst):
        # The function creates an empty dictionary 'counter',
        counter = {}
        # iterates through the list,
        for element in lst:
            # and increments the count for each element using the get() method.
            counter[element] = counter.get(element, 0) + 1
        # The function returns the 'counter' dictionary.
        return counter
    # Call the count_elements() function on both input lists 'list1' and 'list2'.
    # Compare the resulting dictionaries using the == operator.
    # Return the result of the comparison (True if the dictionaries are equal, False otherwise).
    return count_elements(list1) == count_elements(list2)

check_same_frequency(list1, list2)


# TIME COMPLEXITY:
# The overall time complexity of this function is O(n1 + n2 + min(m1, m2)), where n1 and n2 are the lengths of list1 and list2, and m1 and m2 are the numbers of distinct elements in list1 and list2, respectively. 
# This is determined by the time complexity of the count_elements() function and the dictionary comparison.

# SPACE COMPLEXITY:
# The space complexity of this function is O(m1 + m2), where m1 and m2 are the numbers of distinct elements in list1 and list2, respectively. 
# This is because the function creates two dictionaries with as many keys as there are distinct elements in the input lists.
