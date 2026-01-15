


class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values  = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    # TIME AND SPACE COMPLEXITY: O(1)



    def enqueue(self, value):
        self.items.append(value)
        return "Item successfully added to the end of the Queue."

    # TIME COMPLEXITY: O(n^2) worst case
    # SPACE COMPLEXITY: O(1)


    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty."
        else:
            return self.items.pop(0)

    # TIME COMPLEXITY: O(n) as removing the first element in a list requires all other elements to shift to the right
    # SPACE COMPLEXITY: O(1)



    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.items[0]

    # TIME AND SPACE COMPLEXITY: O(1)



    def delete(self):
        # self.items = None # Tutorial solution
        self.items = [] # My solution
            



customQueue = Queue()
print(customQueue.isEmpty())
print("-----------")
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print("-----------")
customQueue.dequeue()
print(customQueue)
print("-----------")
print(customQueue.peek())
print(customQueue)
print("-----------")
print(customQueue.delete())
print(customQueue.isEmpty())
print(customQueue) # This throws an error using the tutorial solution for delete method because a NoneType object is not iterable.






    # TIME AND SPACE COMPLEXITY OF QUEUE OPERATIONS WITH PYTHON LIST
    #
    # -----------------------------------------------------------------------
    # |     METHOD          |   TIME COMPLEXITY     |   SPACE COMPLEXITY    |
    # -------------------------------------------------------------------
    # | Create Queue        |           O(1)        |           O(1)        |
    # | Enqueue             |           O(n)        |           O(1)        |
    # | Dequeue             |           O(n)        |           O(1)        |
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
