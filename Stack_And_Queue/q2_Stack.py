# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? 
# Push, pop and min should ALL OPERATE IN O(1). 



# Create a stack with min method
# Note: Use a linked list to allow O(1) Time Complexity

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ', ' + str(self.next)
        return string


class Stack:
    def __init__(self):
        self.top = None
        self.minNode = None

    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value

    def push(self, item):
        # If the minNode exists and is less than the value of the item...
        if self.minNode and (self.minNode.value < item):
            # Set the value of minNode to the item value
            self.minNode = Node(value = self.minNode.value, next = self.minNode)
        # Otherwise the value of the minNode stays as it was.
        else:
            self.minNode = Node(value = item, next = self.minNode)
        self.top = Node(value = item, next = self.top)

    def pop(self):
        if not self.top:
            return None
        # Otherwise set minNode to next value of minNode
        self.minNode = self.minNode.next
        # set item to value of top to return it
        item = self.top.value
        # Then set top to value of top.next to delete the original top value from the beginning of the linked list
        self.top = self.top.next
        return item
    
customStack = Stack()
customStack.push(5)
print(customStack.min())
customStack.push(6)
print(customStack.min())
customStack.push(3)
print(customStack.min())
customStack.pop()
print(customStack.min())

