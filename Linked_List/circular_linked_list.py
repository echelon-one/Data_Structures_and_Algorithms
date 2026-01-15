

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class CircularDoublyLinkedList:
    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Example Constructor for creating cdll with one node
    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     new_node.prev = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1



    def __str__(self):
        current_node = self.head
        result = ''
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
            result += ' <-> '
        return result
    
    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)



    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    # TIME AND SPACE COMPLEXITY: O(1)



    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    # TIME AND SPACE COMPLEXITY: O(1)



    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break

    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)



    def reverse_traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev
            if current_node == self.tail:
                break

    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)



    def search(self, target):
        current_node = self.head
        while current_node:
            if current_node.value == target:
                return True
            current_node = current_node.next
            if current_node == self.head:
                break
        return False

    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)



    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current_node = None
        if index < self.length // 2:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for i in range(self.length - 1, index, -1):
                current_node = current_node.prev
        return current_node

    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)



    def set_value(self, index, value):
        target_node = self.get(index)
        if target_node:
            target_node.value = value
            return True
        return False

    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)



    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Index is out of bounds!")
            return
        if index == 0:
            self.prepend(value)
            return
        if index == self.length:
            self.append(value)
            return
        new_node = Node(value)
        temp_node = self.get(index-1)
        new_node.next = temp_node.next
        new_node.prev = temp_node 
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1

    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)



    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            return popped_node
        else:
            self.head = self.head.next
            popped_node.prev = None
            popped_node.next = None
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1
        return popped_node
    
    # TIME AND SPACE COMPLEXITY: O(1)



    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            return popped_node
        else:
            self.tail = self.tail.prev
            popped_node.next = None
            popped_node.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail
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



    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    # TIME AND SPACE COMPLEXITY: O(1)





new_cdll = CircularDoublyLinkedList()
new_cdll.append(10)
new_cdll.append(20)
new_cdll.append(30)
new_cdll.prepend(50)
#new_cdll.traverse()
#new_cdll.reverse_traverse()
#print(new_cdll.search(90))
#print(new_cdll.get(1))
#print(new_cdll.set_value(1, 70))
new_cdll.insert(2, 75)
#print(new_cdll)
#new_cdll.pop_first()
#new_cdll.pop()
#new_cdll.remove(2)
new_cdll.delete_all()
print(new_cdll)




    # TIME AND SPACE COMPLEXITY OF CIRCULAR DOUBLY LINKED LIST
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
