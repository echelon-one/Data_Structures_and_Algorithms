# CODING EXERCISE 43: POWER

def power(base, exponent):
    # Step 3: Unintentional case - The constraint
    assert base >= 0 and exponent >= 0 and int(base) == base and int(exponent) == exponent, "The base and exponent must be positive integers!"
    # Step 2: Base case - The stopping criterion
    if exponent == 0:
        return 1
    # Step 1: Recursive case - the flow
    return base * power(base, exponent-1)

print(power(2, 0)) #1
print(power(2, 2)) #4
print(power(2, 4)) #16
# print(power(-2, 2)) # Will trigger assert error as base is a negative number
# print(power(2, -2)) # Will trigger assert error as exponent is a negative number
# print(power(2.2, 2)) # Will trigger assert error as base is not an integer
# print(power(2, 2.2)) # Will trigger assert error as exponent is not an integer






# CODING EXERCISE 44: FACTORIAL

# Write a function factorial which accepts a number and returns the factorial of that number. 
# A factorial is the product of an integer and all the integers below it; 
# e.g., factorial four ( 4! ) is equal to 24, because 4 * 3 * 2 * 1 equals 24. factorial zero (0!) is always 1.

# Examples

# factorial(1) # 1
# factorial(2) # 2
# factorial(4) # 24
# factorial(7) # 5040


def factorial(num):
    assert num >= 0 and int(num) == num, "The number must be a positive integer!"
    if num in (0,1):
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(1)) # 1
print(factorial(2)) # 2
print(factorial(4)) # 24
print(factorial(7)) # 5040
#print(factorial(-1)) # Will trigger assert error as number is not a positive number
#print(factorial(1.5)) # Will trigger assert error as number is not an integer






# CODING EXERCISE 45: Product of Array

# Write a function called productOfArray which takes in an array of numbers and returns the product of them all.

# Examples

# productOfArray([1,2,3]) #6
# productOfArray([1,2,3,10]) #60


def productOfArray(arr):
    if len(arr) == 0:
        return 1
    # Step 1: Recursive case - the flow
    return arr[0] * productOfArray(arr[1:])

print(productOfArray([1,2,3])) # 6
print(productOfArray([1,2,3,10])) # 60




# CODING EXERCISE 46: Recursive Range

# Write a function called recursiveRange which accepts a number and adds up all the numbers from 0 to the number passed to the function.

# Examples

# recursiveRange(6) # 21
# recursiveRange(10) # 55 

def recursiveRange(num):
    # Step 2: Base case - The stopping criterion/Step 3: Unintentional case - The constraint
    if num <= 0:
        return 0
    # Step 1: Recursive case - the flow
    return num + recursiveRange(num-1)

print(recursiveRange(6)) # 21
print(recursiveRange(10)) # 55
print(recursiveRange(-1)) # 0




# CODING EXERCISE 47: Fibonacci

# Write a recursive function called fib which accepts a number and returns the nth number in the Fibonacci sequence. 
# Recall that the Fibonacci sequence is the sequence of whole numbers 0,1, 1, 2, 3, 5, 8, ... which starts with 0 and 1, 
# and where every number thereafter is equal to the sum of the previous two numbers.

# Examples

# fib(4) # 3
# fib(10) # 55
# fib(28) # 317811
# fib(35) # 9227465


def fib(num):
    # Step 3: Unintentional case - The constraint
    # Step 2: Base case - The stopping criterion: 0 and 1
    if num in (0,1): # also if (num < 2)
        return num
    # Step 1: Recursive case - The flow
    return fib(num-1) + fib(num-2)


print(fib(4)) # 3
print(fib(10)) # 55
print(fib(28)) # 317811
print(fib(35)) # 9227465




# CODING EXERCISE 48: Reverse

# Write a recursive function called reverse which accepts a string and returns a new string in reverse.

# Examples

# reverse('python') # 'nohtyp'
# reverse('appmillers') # 'srellimppa'

def reverse(strng):
    if len(strng) <= 1:
        return strng
    return strng[len(strng) - 1] + reverse(strng[0:len(strng) - 1])



print(reverse('python')) # 'nohtyp'
print(reverse('appmillers')) # 'srellimppa'






# CODING EXERCISE 50: isPalindrome

# Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome (reads the same forward and backward). Otherwise it returns false.

# Examples

# isPalindrome('awesome') # false
# isPalindrome('foobar') # false
# isPalindrome('tacocat') # true
# isPalindrome('amanaplanacanalpanama') # true
# isPalindrome('amanaplanacanalpandemonium') # false

def isPalindrome(strng):
    if len(strng) == 0:
        return True
    if strng[0] != strng[len(strng)-1]:
        return False
    return isPalindrome(strng[1: - 1])


print(isPalindrome('awesome')) # false
print(isPalindrome('foobar')) # false
print(isPalindrome('tacocat')) # true
print(isPalindrome('amanaplanacanalpanama')) # true
print(isPalindrome('amanaplanacanalpandemonium')) # false





# CODING EXERCISE 50: someRecursive

# Write a recursive function called someRecursive which accepts an array and a callback. 
# The function returns true if a single value in the array returns true when passed to the callback. 
# Otherwise it returns false.

# Examples

# someRecursive([1,2,3,4], isOdd) # true
# someRecursive([4,6,8,9], isOdd) # true
# someRecursive([4,6,8], isOdd) # false

def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True

print(someRecursive([1,2,3,4], isOdd)) # true
# someRecursive([4,6,8,9], isOdd) # true
# someRecursive([4,6,8], isOdd) # false
