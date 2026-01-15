
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return result

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    # TIME AND SPACE COMPLEXITY = O(1)


    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    # TIME AND SPACE COMPLEXITY = O(1)#
    

    def insert(self, index, value):
        new_node = Node(value)
        if index > self.length or index < 0:
            raise Exception("Index is out of range!")
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            # The for loop loops from the start until the specified index - 1, 
            # to ensure it is inserted after the node at the index before the specified index, 
            # and before the node at the specified index. This ensures it is inserted AT the specified index.
            for _ in range(index-1):
                # This moves the pointer a step at a time in the loop
                temp_node = temp_node.next
            # Once the specified index is reached, we point the new_node to the location the temp_node is pointing to
            new_node.next = temp_node.next
            # The temp_node pointer is then moved to point to the new_node
            temp_node.next = new_node
        self.length += 1
    
    # TIME COMPLEXITY: O(N) due to the for loop.
    # SPACE COMPLEXITY: O(1)


    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            if current == self.head:
                break
    
    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)



    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False
    
    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)


    def get(self, index):
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
            if current == self.head:
                break
        return current
    
    # TIME COMPLEXITY: O(N) - because of the for loop
    # SPACE COMPLEXITY: O(1)

    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    # TIME COMPLEXITY: O(N) - because of the for loop in the get method
    # SPACE COMPLEXITY: O(1)


    def pop_first(self):
        popped_node = self.head
        # EDGE CASE 1: If list is empty return none
        if self.length == 0:
            return None
        # EDGE CASE 2: Only one node
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    # TIME AND SPACE COMPLEXITY: O(1)


    def pop(self):
        popped_node = self.tail
        # EDGE CASE 1: No elements in the linked list
        if self.length == 0:
            return None
        # EDGE CASE 2: Only one node
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            # Update second last node's next reference to point to the first node/head
            temp.next = self.head
            # Move tail to point to second-last node
            self.tail = temp
            # Update popped_node's next reference to point to none.
            # This will remove the link between the last note and the first node.
            popped_node.next = None
        # After this, decrease the size of the linked list
        self.length -= 1
        return popped_node
    
    # TIME COMPLEXITY: O(N) because of the while loop
    # SPACE COMPLEXITY: O(1) because no additional space is required in the memory


    def remove(self, index):
        # EDGE CASE 1: If a negative index or an index greater than the size of the linked list is passed
        if index < 0 or index >= self.length:
            return None
        # EDGE CASE 2: If an index of 0 is passed
        elif index == 0:
            return self.pop_first()
        # EDGE CASE 3: If the index of the last node is passed
        elif index == self.length - 1:
            return self.pop()
        # Use get method to get the node before the node to be removed, and set prev_node to that
        prev_node = self.get(index-1)
        # Create pointer to node that we want to delete
        popped_node = prev_node.next
        # Update prev_node's next reference to point to the node located after the popped_node
        prev_node.next = popped_node.next 
        # Update the popped node's next reference to None to delete the link to the popped_node and the next node
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    # TIME COMPLEXITY: O(N) because of the loop in the pop() and get() methods called.
    # SPACE COMPLEXITY: O(1)

    def delete_all(self):
        # EDGE CASE: If no nodes exist.
        if self.length == 0:
            return
        # Update the next reference of the last node to None to delete the circular link to the first node.
        self.tail.next = None
        # Update head to point to None 
        self.head = None
        # Update tail to point to None
        self.tail = None
        # Set size of linked list to 0
        self.length = 0

    # TIME AND SPACE COMPLEXITY: O(1)



            




csLinkedList = CSLinkedList()
csLinkedList.append(10)
csLinkedList.append(20)
csLinkedList.append(30)
csLinkedList.append(40)
print(csLinkedList)
csLinkedList.prepend(50)
print(csLinkedList)
csLinkedList.insert(5, 60)
print(csLinkedList)
#print(csLinkedList.head.next.value)
csLinkedList.traverse()
print(csLinkedList.search(70))

print("The node at index 3 is: ")
print(csLinkedList.get(3))

print(csLinkedList.set_value(3,17))

print("The popped node value is: ")
print(csLinkedList.pop_first())

print("The popped node value is: ")
print(csLinkedList.pop())

print("The removed node value is: ")
print(csLinkedList.remove(1))
print(csLinkedList)

print(csLinkedList.delete_all())
print("All nodes have now been deleted")


    # TIME AND SPACE COMPLEXITY OF CIRCULAR LINKED LIST
    #
    # |     METHOD          |   TIME COMPLEXITY     |   SPACE COMPLEXITY    |
    # -------------------------------------------------------------------
    # | Create              |           O(1)        |           O(1)        |
    # | Append              |           O(1)        |           O(1)        |
    # | Prepend             |           O(1)        |           O(1)        |
    # | Insert              |           O(n)        |           O(1)        |
    # | Search              |           O(n)        |           O(1)        |
    # | Traverse            |           O(n)        |           O(1)        |
    # | Get                 |           O(n)        |           O(1)        |
    # | Set                 |           O(n)        |           O(1)        |
    # | Pop First           |           O(1)        |           O(1)        |
    # | Pop                 |           O(n)        |           O(1)        |
    # | Remove              |           O(n)        |           O(1)        |
    # | Delete all nodes    |           O(1)        |           O(1)        |
