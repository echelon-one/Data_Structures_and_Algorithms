# Create a Queue
# Create an object of Linked List class - with blank head and blank tail

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Need to edit Python iter function to make LinkedList iterable:
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next
            

class Queue:
    def __init__(self):
        self.linkedList = LinkedList() # T & S: O(1)

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else: 
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    # TIME AND SPACE COMPLEXITY: O(1)



    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    # TIME AND SPACE COMPLEXITY: O(1)



    def dequeue(self):
        if self.isEmpty():
            return "There are no nodes in the Queue."
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode

    # TIME AND SPACE COMPLEXITY: O(1)


    def peek(self):
        if self.isEmpty():
            return "There are no nodes in the Queue."
        else:
            return self.linkedList.head
    
    # TIME AND SPACE COMPLEXITY: O(1)
    


    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None

    # TIME AND SPACE COMPLEXITY: O(1)



customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print("----------")
print(customQueue.dequeue())
print(customQueue)
print("----------")
print(customQueue.peek())
print(customQueue)
print("----------")
customQueue.delete()
print(customQueue)




    # TIME AND SPACE COMPLEXITY OF QUEUE OPERATIONS USING A LINKED LIST
    #
    # -----------------------------------------------------------------------
    # |     METHOD          |   TIME COMPLEXITY     |   SPACE COMPLEXITY    |
    # -------------------------------------------------------------------
    # | Create Queue        |           O(1)        |           O(1)        |
    # | Enqueue             |           O(1)        |           O(1)        |
    # | Dequeue             |           O(1)        |           O(1)        |
    # | Peek                |           O(1)        |           O(1)        |
    # | isEmpty             |           O(1)        |           O(1)        |
    # | Delete Entire Queue |           O(1)        |           O(1)        |
    # -----------------------------------------------------------------------




    # TIME AND SPACE COMPLEXITY QUEUE COMPARISON:- LIST VS LINKED LIST
    #
    #
    #                       -------------------------------------------------------------------------------
    #                       | LIST NO CAPACITY LIMIT  |   LIST WITH CAPACITY    |      LINKED LIST        |
    #                       |                         |    (CIRCULAR QUEUE)     |                         |
    # -----------------------------------------------------------------------------------------------------
    # |     METHOD          |    TIME    |   SPACE    |    TIME    |   SPACE    |    TIME    |   SPACE    | 
    # |                     | COMPLEXITY | COMPLEXITY | COMPLEXITY | COMPLEXITY | COMPLEXITY | COMPLEXITY |
    # -----------------------------------------------------------------------------------------------------
    # | Create Queue        |    O(1)    |    O(1)    |    O(1)    |    O(n)    |    O(1)    |    O(1)    |
    # | Enqueue             |    O(n)    |    O(1)    |    O(1)    |    O(1)    |    O(1)    |    O(1)    |
    # | Dequeue             |    O(n)    |    O(1)    |    O(1)    |    O(1)    |    O(1)    |    O(1)    |
    # | Peek                |    O(1)    |    O(1)    |    O(1)    |    O(1)    |    O(1)    |    O(1)    |
    # | isEmpty             |    O(1)    |    O(1)    |    O(1)    |    O(1)    |    O(1)    |    O(1)    |
    # | isFull              |     -      |     -      |    O(1)    |    O(1)    |     -      |     -      |
    # | Delete Entire Queue |    O(1)    |    O(1)    |    O(1)    |    O(1)    |    O(1)    |    O(1)    |
    # -----------------------------------------------------------------------------------------------------



