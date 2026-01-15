# CREATING A DICTIONARY

my_dict = dict()
print(my_dict)
my_dict2 = {}
print(my_dict2)

# Dictionary that maps english to spanish

# Syntax1: Using the dict() constructor - my_dict = dict(key1='value1', key2='value2', key3='value3')
eng_sp = dict(hello='hola', want='querer', need='necisitar')
print(eng_sp)

# Syntax 2 - my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
eng_sp2 = {'hello':'hola', 'want':'querer', 'need':'necesitar'}
print(eng_sp2)

# Syntax 3: Using a tuple and the dict() constructor 
# - my_list = [('key1','value1'), ('key2','value2'), ('key3','value3')]
# my_dict = dict(my_list)
eng_sp_list = [('hello','hola'), ('want','querer'), ('need','necesitar')]
eng_sp3 = dict(eng_sp_list)
print(eng_sp3)

# Time and Space Complexity: O(n)





# UPDATE / ADD AN ELEMENT TO THE DICTIONARY

myDict = {'name':'Edy', 'age': 26}
# To update/change a value (e.g. 'age') use assignment operator:
myDict['age'] = 27 # TIME AND SPACE COMPLEXITY: O(1)
print(myDict)

# To add an element also use assignment operator:
myDict['address'] = 'London' # TIME COMPLEXITY: O(1). SPACE COMPLEXITY: amortized O(1)
print(myDict)






# TRAVERSE THROUGH A DICTIONARY

myDict = {'name':'Edy', 'age': 26, 'address': 'London'}

def traverseDict(dict):
    for key in dict: # O(n)
        print(key, dict[key]) # O(1)

traverseDict(myDict) 

# TIME COMPLEXITY: O(n). 
# SPACE COMPLEXITY: O(1).







# SEARCH FOR AN ELEMENT IN A DICTIONARY

myDiction = {'name':'John', 'age':35, 'address':'Glasgow'}

def searchDict(dict, value):
    for key in dict: # O(n)
        if dict[key] == value: # O(1)
            return key, value # O(1)
    return 'The value does not exist' # O(1)
        
print(searchDict(myDiction, 'Glasgow'))

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)







# DELETE AN ELEMENT FROM A DICTIONARY

my_dict = {"name": "Bob", "age": 37, "address": "Edinburgh", "Education": "Masters"}

# 1. Delete using del function

del my_dict['age'] 
print(my_dict)

# TIME AND SPACE COMPLEXITY: O(1)


# 2. Delete using pop() method

my_dict = {"name": "Bob", "age": 37, "address": "Edinburgh", "Education": "Masters"}

removed_element = my_dict.pop('address')
print(removed_element)
print(my_dict)

# TIME AND SPACE COMPLEXITY: O(1)


# 3. Delete using popitem() method to remove last element

my_dict = {"name": "Bob", "age": 37, "address": "Edinburgh", "Education": "Masters"}

removed_element = my_dict.popitem()
print(removed_element)
print(my_dict)

# TIME AND SPACE COMPLEXITY: O(1)


# 4. Delete all elements from a dictionary using clear() method 

my_dict = {"name": "Bob", "age": 37, "address": "Edinburgh", "Education": "Masters"}

my_dict.clear() 
print(my_dict)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)





# DICTIONARY METHODS

# 1. clear() method. Syntax: dictionaryName.clear()

my_dict = {"name": "Bob", "age": 37, "address": "Edinburgh", "Education": "Masters"}

my_dict.clear() 
print(my_dict)


# 2. copy() method. Syntax: dictionaryName.copy()

my_dict = {"name": "Bob", "age": 37, "address": "Edinburgh", "Education": "Masters"}

copy_of_original = my_dict.copy() 
print(my_dict)
print(copy_of_original)


# 3. fromkeys() method. Syntax: dictionaryName.fromkeys(sequence[], value)

my_dict = {"name": "Bob", "age": 37, "address": "Edinburgh", "Education": "Masters"}

new_dict = {}.fromkeys([1,2,3], 0)
print(new_dict)


# 4. get() method. Syntax: dictionaryName.get(key, value)

my_dict = {"name": "Bob", "age": 37, "address": "Edinburgh", "Education": "Masters"}

my_dict.get('age', 27) # Returns the correct value for the specified key. If the key doesn't exist it will just return the value specified in the argument
print(my_dict)


# 5. items() method. Syntax: dictionaryName.items()

my_new_dict = {"name": "Simon", "age": 45, "address": "Liverpool", "Education": "Masters"}

print(my_new_dict.items()) # Returns a dictionary's key:value tupple pairs


# 6. keys() method. Syntax: dictionaryName.keys()

my_new_dict = {"name": "Simon", "age": 45, "address": "Liverpool", "Education": "Masters"}

print(my_new_dict.keys()) # Returns a dictionary's keys


# 7. popitem() method. Syntax: dictionaryName.popitem()

my_new_dict = {"name": "Sam", "age": 21, "address": "Glasgow", "Education": "Highschool"}

print(my_new_dict.popitem()) # Removes last key:value pair from dictionary


# 8. setdefault() method. Syntax: dictionaryName.setdefault(key.default_value)

my_new_dict = {"name": "Sam", "age": 21, "address": "Glasgow", "Education": "Highschool"}

print(my_new_dict.setdefault('name1', 'added')) # Adds key:value pair to dictionary if the key doesn't exist already. Otherwise it returns the value for the specified key.


# 9. pop() method. Syntax: dictionaryName.pop(key, default_value)

my_new_dict = {"name": "Sam", "age": 21, "address": "Glasgow", "Education": "Highschool"}

print(my_new_dict.pop('address', 'Glasgow')) 


# 10. values() method. Syntax: dictionaryName.values()

my_new_dict = {"name": "Sam", "age": 21, "address": "Glasgow", "Education": "Highschool"}

print(my_new_dict.values()) # Returns a list of the dictionary values


# 11. update() method. Syntax: originalDictionary.update(dictionaryToBeAdded)

my_orig_dict = {"name": "Sam", "age": 21, "address": "Glasgow", "Education": "Highschool"}

new_dictionary = {'A': 1, 'B': 2, 'C': 3}

my_orig_dict.update(new_dictionary) # Adds the elements in a new dictionary to the original dictionary - A union

print(my_orig_dict)





# DICTIONARY OPERATIONS / BUILT-IN FUNCTIONS

# 1. in operator
my_dict = {3: "three", 5: "five", 9: "nine", 2: "two", 1: "one", 4: "four"}

print(3 in my_dict) # Returns True
print("three" in my_dict) # Returns False as the in operator works with keys not values. 
# Use .values() method with in operator to check for values
print("three" in my_dict.values()) # This will return True


# 2. len() function
my_dict = {3: "three", 5: "five", 9: "nine", 2: "two", 1: "one", 4: "four"}

print(len(my_dict)) # Counts the number of pairs in the dictionary


# 3. all() function
my_dict = {3: "three", 5: "five", 9: "nine", 2: "two", 1: "one", 4: "four"}

print(all(my_dict)) # Returns True if values for all keys are True but returns False if any value for a key is False


# 4. any() function
my_dict = {3: "three", 5: "five", 9: "nine", 2: "two", 1: "one", 4: "four"}

print(any(my_dict)) # Returns True if a value for any key is True 


# sorted() function
my_dict = {3: "three", 5: "five", 9: "nine", 2: "two", 1: "one", 4: "four"}

print(sorted(my_dict)) # Returns a sorted list of the keys in the dictionary





# TIME AND SPACE COMPLEXITY IN PYTHON DICTIONARY

#               OPERATION               |   TIME COMPLEXITY |   SPACE COMPLEXITY    |
#------------------------------------------------------------------------------------
#   Creating a Dictionary               |   O(len(dict))    |       O(n)            |
#   Inserting a value in a Dictionary   |   O(1)/O(n)       |       O(1)            |
#   Traversing a given Dictionary       |       O(n)        |       O(1)            |
#   Accessing a given cell              |       O(1)        |       O(1)            |
#   Searching a given value             |       O(n)        |       O(1)            |
#   Deleting a given value              |       O(1)        |       O(1)            |




# DICTIONARY COMPREHENSION - A way of creating a dictionary using short syntax

# Syntax: new_dict = {new_key:new_value for item in list}

# We can use the syntax to create a new dictionary from an existing one, and even use the if condition
# new_dict = {new_key:new_value for (key, value) in dict.items() if condition}

import random

city_names = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']

# Create a new dictionary 'city_temp' using the list above 'city_names' adding random temperatures for each city 
city_temps = {city:random.randint(20, 30) for city in city_names}

print(city_temps)


# Create a new dictionary from the dictionary above, including only cities where the temperature is greater than 25 degrees
above_25 = {city: temp for (city, temp) in city_names in city_temps.items() if temp > 25}


