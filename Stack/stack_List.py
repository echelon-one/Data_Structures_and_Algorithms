# WHEN TO USE/AVOID STACK

# USE:
# - When you want to implement LIFO functionality
# - The chance of data corruption is minimum

# AVOID:
# - Random access is not possible as we can only access the last/top element in the stack. 
#   So if we want to access the first/bottom element, we have to remove all other elements that sit on top.



class Stack:
    def __init__(self):
        self.list = []  # T & S COMPLEXITY: O(1)

    # OLD STR METHOD
    # def __str__(self):
    #    values = self.list.reverse()
    #    values = [str(x) for x in self.list]
    #    return '\n'.join(values)

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)



    # isEmpty method
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    # TIME AND SPACE COMPLEXITY: O(1)



    # push method
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted." 
    
    # TIME COMPLEXITY: Worst case is O(n^2)
    # SPACE COMPLEXITY: O(1)



    # pop method
    def pop(self):
        if self.isEmpty():
            return "There is no elements in the stack."
        else:
            return self.list.pop()
    
    # TIME AND SPACE COMPLEXITY: O(1)



    # peek method
    def peek(self):
        if self.isEmpty():
            return "There is no elements in the stack."
        else:
            return self.list[len(self.list)-1]
    
    # TIME AND SPACE COMPLEXITY: O(1)



    # delete method
    def delete(self):
        self.list = None
    
    # TIME AND SPACE COMPLEXITY: O(1)



        
    
customStack = Stack()
print("isEmpty METHOD:")
print(customStack.isEmpty())

print("")
print("PUSH METHOD:")
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


print("")
print("DELETE METHOD:")
print(customStack.delete())





    
