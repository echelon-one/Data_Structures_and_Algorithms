

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    # OLD STR METHOD
    # def __str__(self):
    #    values = self.list.reverse()
    #    values = [str(x) for x in self.list]
    #    return '\n'.join(values)

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    # TIME AND SPACE COMPLEXITY O(1)



    # push method
    def push(self, value):
        if self.isFull():
            return "The stack is full."
        else:
            self.list.append(value)
            return "The element has been successfully inserted."
        
    # TIME COMPLEXITY: Amortised constant OR O(N)
    # SPACE COMPLEXITY: O(1)


    # pop method
    def pop(self):
        if self.isEmpty():
            return "There is no elements in the stack."
        else:
            return self.list.pop()


    # peek method
    def peek(self):
        if self.isEmpty():
            return "There is no elements in the stack."
        else:
            return self.list[len(self.list)-1]

    

    # delete method
    def delete(self):
        self.list = None


customStack = Stack(4)
print("")
print("isEmpty METHOD:")
print(customStack.isEmpty())

print("")
print("isFull METHOD:")
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

print("")
print("POP METHOD:")
print(customStack.pop())

print("")
print("PEEK METHOD:")
print(customStack.peek())






    # TIME AND SPACE COMPLEXITY OF STACK OPERATIONS WITH LIST
    #
    # |     METHOD          |   TIME COMPLEXITY     |   SPACE COMPLEXITY    |
    # -------------------------------------------------------------------
    # | Create Stack        |           O(1)        |           O(1)        |
    # | Push                |       O(1)/O(n^2)     |           O(1)        |
    # | Pop                 |           O(1)        |           O(1)        |
    # | Peek                |           O(1)        |           O(1)        |
    # | isEmpty             |           O(1)        |           O(1)        |
    # | Delete Entire Stack |           O(1)        |           O(1)        |
