class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

# TIME AND SPACE COMPLEXITY: O(1)



class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# TIME AND SPACE COMPLEXITY: O(1)

first_linked_list = LinkedList(10)
print(first_linked_list.head.value)
print(first_linked_list.length)





class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.value = None
        self.length = 0

    # Create a string method to enable node value to be printed
    def __str__(self):
        temp_node = self.head
        result = ' '
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result 

    
    # INSERT A NODE AT THE BEGINNING OF THE LINKED LIST USING PREPEND METHOD
    def prepend(self, value):
        # Create new node
        new_node = Node(value)
        # Check if linked list is empty 
        if self.head is None:
            # Update head and tail to point to new node
            self.head = new_node
            self.tail = new_node
        # Otherwise point new node to head
        else:
            # Update next reference of the new node to point to the head node
            new_node.next = self.head
            self.head = new_node
        # Increase length by one as new node has been added to linked list
        self.length += 1
    # TIME AND SPACE COMPLEXITY: O(1)


    # INSERT A NODE AT THE END OF THE LINKED LIST USING APPEND() METHOD
    def append(self, value):
        # Create new node
        new_node = Node(value)
        # If there are no nodes in the linked_list (i.e the list is empty), point to new_node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Access last node's next pointer and set it to new_node
            self.tail.next = new_node
            self.tail = new_node 
        self.length += 1
    # TIME AND SPACE COMPLEXITY OF APPEND METHOD IS O(1)


    # INSERT METHOD
    def insert(self, index, value):
        new_node = Node(value)
        # Edge case 1: If index is less than zero or greater than the length of the linked list, return false.
        if index < 0 or index > self.length:
            return False
        # Edge case 2: If linked list is empty, create new list
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        # Edge case 3: If index is zero, insert at beginning of list
        elif index == 0:
            new_node = self.head
            self.head = new_node
        # Otherwise insert at specified index
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    # TIME COMPLEXITY IS O(n) because of for loop. 
    # SPACE COMPLEXITY IS O(1).


    # TRAVERSAL OF LINKED LIST
    def traverse(self):
        current = self.head
        # While current is not equal to None
        while current:
            print(current.value)
            current = current.next
    # TIME COMPLEXITY: O(n)
    # SPACE COMPLEXITY: O(1)


    # SEARCH METHOD
    def search(self, target):
        # Current variable starts at first node
        current = self.head
        # Index variable
        index = 0
        # While current is not equal to None
        while current:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    # TIME COMPLEXITY: O(n)
    # SPACE COMPLEXITY: O(1)


    # GET METHOD: Get the value at the specified index
    def get(self, index):
        # EDGE CASE 1: If index is specified as -1, return the value of the last node in the list
        if index == -1:
            return self.tail
        # EDGE CASE 2: If index is less than minus 1 or greater than the length of the list, return None.
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    # TIME COMPLEXITY: O(n)
    # SPACE COMPLEXITY: O(1)


    # SET METHOD: Set the value of the node, at the specified index, to the specified value
    def set_value(self, index, value):
        # Use the get method to get the node at the specified index and store in temp node
        temp = self.get(index)
        # If temp is not equal to None, set the value of the temp node to the specified value and return True
        if temp:
            temp.value = value
            return True
        return False
    # TIME COMPLEXITY: O(n)
    # SPACE COMPLEXITY: O(1)


    # POP FIRST METHOD: To remove and return first node.
    def pop_first(self):
        # EDGE CASE 1: If list is empty return None
        if self.length == 0:
            return None
        popped_node = self.head
        # EDGE CASE 2: Only one node
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node.value
    # TIME AND SPACE COMPLEXITY: O(1)


    # POP METHOD: To remove and return the last node.
    def pop(self):
        # EDGE CASE 1: List is empty
        if self.length == 0:
            return None
        popped_node = self.tail
        # EDGE CASE 2: Only one node
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node.value
    # TIME COMPLEXITY: O(n)
    # SPACE COMPLEXITY: O(1)


    # REMOVE METHOD: Remove and return node at specified index
    def remove(self, index):
        # EDGE CASE 1: If specified index doesn't exist or list is empty return none
        if index >= self.length or index < 0:
            return None
        # EDGE CASE: If only one node in list, remove and return node
        if index == 0:
            return self.pop_first()
        # EDGE CASE: If specified index references the last element, remove and return last node
        if index == self.length-1 or index == -1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node.value
    # TIME COMPLEXITY: O(n)
    # SPACE COMPLEXITY: O(1)


    # DELETE ALL NODES METHOD
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
    # TIME AND SPACE COMPLEXITY: O(1)


new_linked_list = LinkedList() 
new_linked_list.append(10) # This call will insert an element in the empty linked list
new_linked_list.append(20) # This call will insert an element to the end of the linked list
new_linked_list.append(30)
print(new_linked_list)
new_linked_list.prepend(40) # This call will insert an element to the start of the linked list
new_linked_list.insert(1, 50) # NOTE: CHANGE INDEX TO TEST EDGE CASES
print(new_linked_list)
print(new_linked_list.search(40))
print(new_linked_list.get(2)) # Get the value at index 2
print(new_linked_list.set_value(2, 50))
print(new_linked_list.pop_first())
print(new_linked_list.pop())
print(new_linked_list.remove(1)) # Remove the node at index 1


    # TIME AND SPACE COMPLEXITY OF SINGLY LINKED LIST
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
    
