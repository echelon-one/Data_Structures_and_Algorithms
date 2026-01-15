
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    # TIME AND SPACE COMPLEXITY: O(1)


    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)


    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    # TIME AND SPACE COMPLEXITY: O(1)


    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    # TIME AND SPACE COMPLEXITY: O(1)


    # def pop()
    def pop(self):
        if self.isEmpty():
            return "There is no elements in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    # TIME AND SPACE COMPLEXITY: O(1)



    def peek(self):
        if self.isEmpty():
            return "There is no elements in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue

    # TIME AND SPACE COMPLEXITY: O(1)


    def delete(self):
        self.LinkedList.head = None
    
    # TIME AND SPACE COMPLEXITY: O(1)


customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print("-----------------")
customStack.pop()
print(customStack)
print("-----------------")
print(customStack.peek())
print("-----------------")
customStack.delete()
print(customStack.isEmpty())




    # TIME AND SPACE COMPLEXITY OF STACK OPERATIONS WITH LINKED LIST
    #
    # |     METHOD          |   TIME COMPLEXITY     |   SPACE COMPLEXITY    |
    # -------------------------------------------------------------------
    # | Create Stack        |           O(1)        |           O(1)        |
    # | Push                |           O(1)        |           O(1)        |
    # | Pop                 |           O(1)        |           O(1)        |
    # | Peek                |           O(1)        |           O(1)        |
    # | isEmpty             |           O(1)        |           O(1)        |
    # | Delete Entire Stack |           O(1)        |           O(1)        |
