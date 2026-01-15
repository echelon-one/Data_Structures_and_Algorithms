# INTERVIEW QUESTION 1 - How to find the sum of digits of a positive integer number using recursion?

# Step 1: Recursive case = the flow

# Examples:
# 10 10/10 = 1 and Remainder = 0
# 54 54/10 = 5 and Remainder = 4
# 112 112/10 = 11 and Remainder = 2 then divide 11/10 = 1 and Remainder = 1

# Equation: f(n) = n%10 + f(n/10)


# Step 2: Base case - the stopping criterion
# n = 0

# Step 3: Unintentional case - the constraint
# Must be a positive number - sumOfDigits(-11)??
# Must be an integer - sumOfDigits(1.5)??




def sumOfDigits(n):
    # Step 3: Unintentional case - the constraint
    assert n >= 0 and int(n) == n, "The number must be a positive integer!"
    # Step 2: Base case - the stopping criterion
    if n == 0:
        return 0
    # Step 1: Recursive case - the flow
    else:
        return int(n%10) + sumOfDigits(int(n/10))

print(sumOfDigits(4)) # Sum will be 4. 4 + 0 = 4
print(sumOfDigits(11111)) # Sum will be 5. 1 + 1 + 1 + 1 + 1 = 5
# print(sumOfDigits(-11)) # Will trigger assert error as -11 is not a positive number
# print(sumOfDigits(1.5)) # Will trigger asser error as 1.5 is not an integer










# INTERVIEW QUESTION 2 - How to calculate the power of a number using recursion?

# x^n = x * x * x * ...(n times)... * x

# Step 1: Recursive case - the flow

# 2^4 = 2 * 2 * 2 * 2
# x^a * x^b = x^a+b
# x^3 * x^4 = x^3+4
# x^n = x * x^n-1


# Step 2: Base case - the stopping criterion
# n = 0


# Step 3: Unintentional case - the constraint
# 1. base as negative integer, exponent as positive integer: power(-1, 2) ??
# 2. base as non-integer number, exponent as positive integer: power(3.5, 2) ??
# 3. base as positive integer, exponent as non-integer number: power(2, 1.2) ??
# 4. base as positive integer, exponent as negative integer: power(2, -1) ??


def power(base, exponent):
    # Step 3: Unintentional case - the constraint
    assert base >= 0 and exponent >= 0 and int(base) == base and int(exponent) == exponent , "The base and exponent must be positive integers!"
    # Step 2: Base case - the stopping criterion
    if exponent == 0:
        return 1
    # Step 3: Unintentional case - the constraint - ALTERNATIVE TO USING MULTIPLE and CONDITIONS IN ASSERT ABOVE
    #elif exponent < 0:
        #return 1/base * power(base, exponent + 1)
    # Step 1: Recursive case - the flow
    return base * power(base, exponent - 1)

print(power(2, 4))
#print(power(-1, 2)) # Will trigger assert error as base -1 is not a positive number
#print(power(3.5, 2)) # Will trigger assert error as base 3.5 is not an integer
#print(power(2, 1.2)) # Will trigger assert error as exponent 1.2 is not an integer
#print(power(2, -1)) # Will trigger assert error as exponent -1 is not a positive number







# INTERVIEW QUESTION 3 - How to find the GCD (Greatest Common Divisor) of two numbers using recursion?

# Step 1: Recursive case - the flow

# GCD is the largest positive integer that divides the numbers without a remainder
# gcd(8, 12) = 4
# To find the prime factorisation of two numbers
# We can write:
#
#               8 = 2 * 2 * 2
#               12 = 2 * 2 * 3
#
# 2 * 2 appears in both, if we multiply 2 * 2 we get 4
# 
#       Euclidean algorithm:
#           gcd(48, 18)
#           Step 1: 48 / 18 = 2 remainder 12
#           Step 2: 18 / 12 = 1 remainder 6
#           Step 3: 12 / 6 = 2 remainder 0
#
#           Once we get to remainder 0 this tells us that our gcd is 6
#
# So the recursive algorithm is:
# gcd(a, 0) = a
# gcd(a, b) = gcd(b, a mod b)
#
#
#
# Step 2: Base case - the stopping criterion
#   b = 0
#
#
# Step 3: Unintentional case - the constraint
#   Positive integers
#   Convert negative numbers to positive 


def gcd(a, b):
    # Step 3: Unintentional case - the constraint
    assert int(a) == a and int(b) == b, "a and b must be integers"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    # Step 2: Base Case: The stopping criterion
    if b == 0:
        return a
    # Step 1: The recursive case - the flow
    else:
        return gcd(b, a%b)

print(gcd(48, 18)) # Result will be 6
#print(gcd(-48, 18)) # Result will be 6
#print(gcd(48, -18)) # Result will be 6
#print(gcd(4.8, 18)) # Will trigger assertion error as a is not an integer
#print(gcd(48, 1.8)) # Will trigger assertion error as b is not an integer





# # INTERVIEW QUESTION 4 - How to convert a number from Decimal to Binary using recursion?

# Step 1: Recursive case - the flow
#       Step 1: Divide the number by 2
#       Step 2: Get the integer quotient for the next iteration
#       Step 3: Get the remainder for the binary digit
#       Step 4: Repeat the steps until the quotient is equal to 0
#
#       Example 1:
#       Convert 13 to binary
#       -----------------------------------------
#       | Division by   | Quotient  | Remainder |
#       |---------------|-----------|-----------|
#       |       13/2    |       6   |       1   |
#       |---------------|-----------|-----------|
#       |        6/2    |       3   |       0   |
#       |---------------|-----------|-----------|
#       |        3/2    |       1   |       1   |
#       |---------------|-----------|-----------|
#       |        1/2    |       0   |       1   |
#       -----------------------------------------
#
#       Taking the remainders in reverse, the Binary of 13 is 1101
#
#
#       Example 2:
#       Convert 10 to binary
#       -----------------------------------------
#       | Division by   | Quotient  | Remainder |
#       |---------------|-----------|-----------|
#       |       10/2    |       5   |       0   |
#       |---------------|-----------|-----------|
#       |        5/2    |       2   |       1   |
#       |---------------|-----------|-----------|
#       |        2/2    |       1   |       0   |
#       |---------------|-----------|-----------|
#       |        1/2    |       0   |       1   |
#       -----------------------------------------
#
#       Taking the remainders in reverse, the Binary of 10 is 1010
#
#       So the recursive algorithm is:
#       Take remainder and add value from next iteration and multiply by 10:
#           f(n) = n mod 2 + 10 * f(n/2)

# Step 2: Base case - the stopping criterion
#   number = 0
#
#
# Step 3: Unintentional case - the constraint
#   Number must be an integer  




def decimalToBinary(number):
    # Step 3: Unintentional case - the constraint
    assert int(number) == number, "The paramater must be an integer only!"
    # Step 2: Base case - the stopping criterion
    if number == 0:
        return 0
    # Step 1: The recursive case - the flow
    else:
        return number % 2 + 10 * decimalToBinary(int(number / 2))


print(decimalToBinary(13))
#print(decimalToBinary(1.3)) # Will trigger an assertion error as 1.3 is not an integer
