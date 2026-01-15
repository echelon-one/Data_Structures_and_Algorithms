class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        # return f"{self.prev} <- {self.value} -> {self.next}"
        return str(self.value)

    # TIME AND SPACE COMPLEXITY: O(1)

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += ' <-> '
            temp_node = temp_node.next
        return result
    
    # TIME COMPLEXITY: O(n)
    # SPACE COMPLEXITY: O(1)


    def prepend(self, value):
        new_node = Node(value)

        # EDGE CASE 1: Empty list
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    # TIME AND SPACE COMPLEXITY: O(1)


    def append(self, value):
        new_node = Node(value)

        # EDGE CASE 1: Empty list
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
    
    # TIME AND SPACE COMPLEXITY: O(1)


    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)


    def reverse_traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev

    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)


    def search(self, target):
        current_node = self.head 
        index = 0 # To return index create an index variable...
        while current_node:
            if current_node.value == target:
                # return True # To return boolean value
                return index
            current_node = current_node.next
            index += 1 # ...and iterate 
            if current_node == self.head:
                break
        # return False # For boolean
        return -1 

    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)



    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev
        return current_node
    
    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)



    def set_value(self, index, value):
        # Use get method to get the node at the specified index
        node = self.get(index)
        # If the returned node is not none...
        if node:
            # ...set the value of the node to the specified value...
            node.value = value
            # ...and rturn true
            return True
        # Otherwise if the node is none, return False        
        return False
    
    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)



    def insert(self, index, value):
        new_node = Node(value)
        # EDGE CASE 1: If specified index is out of bounds
        if index < 0 or index > self.length:
            print("Specified index is out of bounds!")
            return
        # EDGE CASE 2: If we want to insert at beginning of the double linked list i.e. at index 0
        if index == 0:
            self.prepend(value)
            return
        # EDGE CASE 3: If we want to insert at the end of the double linked list
        elif index == self.length:
            self.append(value)
            return
        
        # Get the node at the index BEFORE the target index
        temp_node = self.get(index-1)            
        new_node.next = temp_node.next
        # Set the newly created nodes previous reference to point to the temp node, 
        # which is the node appearing at the index BEFORE the target index
        new_node.prev = temp_node
        # Set the previous reference for the node after the temp node to point to the new node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1

    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)



    def pop_first(self):
        popped_node = self.head
        # EDGE CASE 1: If list is empty
        if self.length == 0:
            return None
        # EDGE CASE 2: If list only has one node
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node

    # TIME AND SPACE COMPLEXITY: O(1)



    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
    
    # TIME AND SPACE COMPLEXITY: O(1)



    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        popped_node = self.get(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = None
        popped_node.prev = None
        self.length -= 1
        return popped_node
    
    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)
        



        
       
         
            


newDLL = DoublyLinkedList()
newDLL.append(10)
newDLL.append(20)
newDLL.append(30)
newDLL.append(40)
newDLL.prepend(50)
print(newDLL)
newDLL.remove(0)
print(newDLL)







    # TIME AND SPACE COMPLEXITY OF DOUBLE LINKED LIST
    #
    # |     METHOD          |   TIME COMPLEXITY     |   SPACE COMPLEXITY    |
    # -------------------------------------------------------------------
    # | Create              |           O(1)        |           O(1)        |
    # | Append              |           O(1)        |           O(1)        |
    # | Prepend             |           O(1)        |           O(1)        |
    # | Insert              |           O(n)        |           O(1)        |
    # | Search              |           O(n)        |           O(1)        |
    # | Traverse            |           O(n)        |           O(1)        |
    # | Reverse Traverse    |           O(n)        |           O(1)        |
    # | Get                 |           O(n)        |           O(1)        |
    # | Set                 |           O(n)        |           O(1)        |
    # | Pop First           |           O(1)        |           O(1)        |
    # | Pop                 |           O(1)        |           O(1)        |
    # | Remove              |           O(n)        |           O(1)        |
    # | Delete all nodes    |           O(1)        |           O(1)        |
