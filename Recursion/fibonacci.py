# FIBONACCI NUMBERS - RECURSION

# Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceeding ones 
# and the sequence starts from 0 and 1.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

# Step 1: Recursive case - the flow
# 5 = 3 + 2 so f(n) = f(n-1) + f(n-2)

# Step 2: Base case - the stopping criterion
# 0 and 1

# Step 3: Unintentional case - the constraint
# fibonacci(-1) ?? - negative number
# fibonacci(1.5) ??  - non-integer


def fibonacci(n):
    # Step 3: Unintentional case - the constraint
    assert n >= 0 and int(n) == n, "Fibonacci number cannot be a negative number or non integer"
    # Step 2: Base case - the stopping criterion
    if n in (0, 1):
        return n
    else:
        # Step 1: Recursive case - the flow
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
