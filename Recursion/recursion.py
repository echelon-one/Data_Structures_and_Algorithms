# HOW TO WRITE RECURSION IN 3 STEPS?
# 
# Factorial: 
# - It is the product of all positive integers less than or equal to n.
# - Denoted by n! (Christian Kramp in 1808) .
# - Only positive numbers.
# - O!=1.
# 
# Example 1
# 4! = 4*3*2*1 = 24
#
# Example 2
# 10! = 10*9*8*7*6*5*4*3*2*1 = 3,628,800
# 
# 
#
# STEP 1: Recursive Case - the flow
# n! = n*(n-1)*(n-2)*...*2*1  ----> n! = n*(n-1)!
#
# STEP 2: Base case - the stopping criteria
# 0! = 1
# 1! = 1
#
# STEP 3: Unintentional case - the constraint
# factorial(-1) ??
# factorial(1.5) ??


def factorial(n):
    # STEP 3: Unintentional case - the constraint
    assert n >= 0 and int(n) == n, 'The number must be a positive integer only!'
    # STEP 2: Base case - the stopping criteria
    if n in (0,1):
        return 1
    # STEP 1: Recursive Case - the flow
    else:
        return n * factorial(n-1)


print(factorial(3)) # This will return 6 - 3*2*1 = 6
print(factorial(10)) # This will return 6 - 10*9*8*7*6*5*4*3*2*1 = 3,628,800
# Edge Case 1
#print(factorial(-1)) # This will throw the assertion error - STEP 3
# Edge Case 2
#print(factorial(1.5)) # This will throw the assertion error - STEP 3










# HOW TO MEASURE RECURSIVE ALGORITHMS?

# sampleArray = [5, 4, 10, ... 8, 11, 68, 87, 10]

# Function to return the maximum number in an Array, recursively
def findMaxNumRec(sampleArray, n): # Time Complexity: M(n)
    if n == 1: # Time Complexity: O(1)
        return sampleArray[0] # Time Complexity: O(1)
    return max(sampleArray[n-1], findMaxNumRec(sampleArray, n-1)) # Time Complexity: M(n-1)

A = [11,4,12,7]

print(findMaxNumRec(A, 4))

# Explanation:
# A = [11,4,12,7]  
# So the size of this array is n=4

# If we run findMaxNumRec(A, 4) ---> max(A[4-1], 12) ---> max(7, 12) = 12
# The function will check if n == 1:
# It doesn't as the last element at 4 is 7, so the function will then check n-1:

# findMaxNumRec(A, 3) ---> max(A[3-1], 11) ---> max(12, 11) ---> max(12, 11) = 12
# The function will check if n == 1:
# It doesn't as the element at 3 is 12, so the function will then check n-1:

# findMaxNumRec(A, 2) ---> max(A[2-1], 11) ---> max(4, 11) = 11
# The function will check if n == 1:
# It doesn't as the element at 2 is 4, so the function will then check n-1:

# findMaxNumRec(A, 1) ---> A[0] = 11
# The function will check if n == 1,
# It does, so the function will return 11.


# TIME COMPLEXITY:
# M(n) = O(1)+M(n-1)                    M(n) = 1 + M(n-1)
# M(1) = O(1)                   }            = 1 + (1 + M((n-1) - 1))           
# M(n-1) = O(1)+M((n-1)-1)       }           = 2 + M(n-2)
# M(n-2) = O(1)+M((n-2)-1)       }           = 2 + 1 + M((n-1) -1)
# M(n-3) = O(1)+M((n-3)-1)      }            = 3 + M(n-3)
#                                                -
#                                                -
#                                            = a + M(n-a)
#                                            = n - 1 + M(n-(n-1))
#                                            = n - 1 + 1
#                                            = n





# HOW TO MEASURE RECURSIVE ALGORITHMS THAT MAKE MULTIPLE CALLS?

# Function that calls itself twice
def f(n):
    if n == 1:
        return 1
    return f(n-1) + f(n-1)

# If we call this function for f(4), the calls will be as follows:

#                       f(4)
#                      /    \
#                     /      \
#                    /        \
#                   /          \
#                  /            \
#                 /              \
#              f(3)               f(3)
#             /    \             /    \
#            /      \           /      \
#         f(2)      f(2)      f(2)     f(2)
#         / \       / \       /  \     /  \ 
#        /   \     /   \     /    \   /    \
#      f(1) f(1) f(1) f(1) f(1) f(1) f(1) f(1) 


#  -----------------------------------------------------------------
# | N | Level | Node# | Also can be expressed as..           | or.. |
# |-----------------------------------------------------------------|
# | 4 |   0   |   1   |                                      | 2^0  |
# |-----------------------------------------------------------------|
# | 3 |   1   |   2   | 2 * Previous level = 2               | 2^1  |
# |-----------------------------------------------------------------|
# | 2 |   2   |   4   | 2 * Previous level = 2 * 2^1 = 2^2   | 2^2  |
#  -----------------------------------------------------------------

# So 2^0 + 2^1 + 2^2 + ... + 2^n = 2^n+1 - 1
#       = 2^n-1 ------> O(2^n)

# Equation:
# O(branches^depth) 
# Where branches = Number of children in each node, which is the number of times each recursive call... (next word is inaudible)
# and depth = Parameter of function, which is n
# This means that for parameter n, the time complexity is n^2
