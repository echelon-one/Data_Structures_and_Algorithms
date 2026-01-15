# AKA CIRCULAR QUEUE

class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    # TIME COMPLEXITY: O(1)
    # SPACE COMPLEXITY: O(n) as maxSize = n


    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    


    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
        
    # TIME AND SPACE COMPLEXITY: O(1)


    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    # TIME AND SPACE COMPLEXITY: O(1) 



    def enqueue(self, value):
        if self.isFull():
            return "The queue is full."
        else:
            if self.top +1 == self.maxSize:
                self.top = 0
            else:
                self.top +=1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue."
        
    # TIME AND SPACE COMPLEXITY: O(1) 



    def dequeue(self):
        if self.isEmpty():
            return "There are no elements in the queue."
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start +1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement
        
    # TIME AND SPACE COMPLEXITY: O(1) 



    def peek(self):
        if self.isEmpty():
            return "There are no elements in the queue."
        else:
            return self.items[self.start]
        
    # TIME AND SPACE COMPLEXITY: O(1) 



    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1

    



customQueue = Queue(3)
print(customQueue.isFull())
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.isFull())
print(customQueue.dequeue())
print("--------")
print(customQueue.peek())
print("--------")
print(customQueue.delete())




    # TIME AND SPACE COMPLEXITY OF CIRCULAR QUEUE OPERATIONS
    #
    # -----------------------------------------------------------------------
    # |     METHOD          |   TIME COMPLEXITY     |   SPACE COMPLEXITY    |
    # -------------------------------------------------------------------
    # | Create Queue        |           O(1)        |           O(n)        |
    # | Enqueue             |           O(1)        |           O(1)        |
    # | Dequeue             |           O(1)        |           O(1)        |
    # | Peek                |           O(1)        |           O(1)        |
    # | isEmpty             |           O(1)        |           O(1)        |
    # | isFull              |           O(1)        |           O(1)        |
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




