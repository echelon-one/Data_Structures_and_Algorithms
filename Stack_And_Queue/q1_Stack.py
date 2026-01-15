# INTERVIEW QUESTIONS - 1: THREE IN ONE

# Describe how you could use a single Python list to implement three stacks

# One solution is to divide it into three stacks. 
# i.e A list with 9 elements can be divided into 3. So index 0 - 2 would be the first stack, 3 - 5 would be the second stack and 6 - 8 would be the final/third stack.

# For Stack 1 - [0], [1], [2] -----> [0, n/3)
# For Stack 2 - [3], [4], [5] -----> [n/3, 2n/3)
# For Stack 3 - [7], [8], [9] -----> [2n/3, n)
# NOTE: SQUARE BRACKET MEANS INCLUDED, SIMPLE BRACKET MEANS ELEMENT NOT INCLUDED


# Use a single list to implement trhee stacks

class MultiStack:
    def __init__(self, stacksize):
        self.numberstacks = 3
        self.custList = [0] * (stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize
    
    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False

    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False

    # Helper method
    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum]-1

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return "The stack is full."
        else:
            self.sizes[stacknum] += 1
            self.custList[self.indexOfTop(stacknum)] = item
    
    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty."
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            self.custList[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value


    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty."
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            return value


customStack = MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1)) # This calls the isEmpty method for the second stack, by using 1 as an argument.
# We now insert two elements to the first stack and one element to the third stack, leaving the second stack empty.
customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(3, 2)
print(customStack.peek(1)) # This calls the peek method for the second stack, by using 1 as an argument. This will return "The stack is empty."
print(customStack.peek(0)) # This calls the peek method for the first stack, by using 0 as an argument. This will return the element 2.
print(customStack.peek(2)) # This calls the peek method for the third stack, by using 2 as an argument. This will return the element 3.
# We  will now push an element into the second stack
customStack.push(5, 1)
# ...and call the peek method for the second stack again
print(customStack.peek(1)) # This time it will return the element 5, that we have just pushed into it.

# Now we can call the pop method for the first stack, using 0 as the argument 
print(customStack.pop(0)) # This will remove 2 from the first stack and return it in the terminal below
