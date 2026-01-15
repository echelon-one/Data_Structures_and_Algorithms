# 22. CREATE A SINGLY LINKED LIST

# The code as a whole defines two classes for a singly linked list data structure. 
# The Node class represents individual nodes in the list, 
# and the LinkedList class represents the list itself. 
# When a LinkedList is created, it also creates an initial Node with a given value.




# This line defines a new class named Node. 
# In the context of linked lists, a node is an individual element of the list which holds the data and a reference to the next node.
class Node:

    # This is the constructor method for the Node class. 
    # Whenever a new Node object is created, this method will be called.
    #  It takes two parameters: self which is a reference to the current instance of the class, 
    # and value which is the data that the node will hold.
    def __init__(self, value):

        #  This line sets the value attribute of the node to the value passed to the constructor. 
        # This is the data that this node holds.
        self.value = value

        # This line sets the next attribute of the node to None. 
        # In a linked list, the next attribute usually contains a reference to the next node in the list.
        # Here, it's initialized to None because when a node is first created, it doesn't know what the next node is.
        self.next = None


# This line defines a new class named LinkedList. 
# This class represents the linked list itself and will contain nodes.     
class LinkedList:

    #  This is the constructor method for the LinkedList class. 
    # It takes two parameters: self which is a reference to the current instance of the class, 
    # and value which is the value for the first node in the linked list.
    def __init__(self, value):

        # This line creates a new Node object with the given value. 
        # This new node will be the first node in the linked list.
        new_node = Node(value)

        # This line sets the head attribute of the linked list to the new node. 
        # In a linked list, the head is a reference to the first node in the list.
        self.head = new_node

        # This line sets the tail attribute of the linked list to be the same as the head. 
        # This is because, at the moment of creation, the linked list only contains one node, so the head and tail are the same.
        self.tail = self.head

        # This line sets the length attribute of the linked list to 1. 
        # The length attribute keeps track of how many nodes are in the list. 
        # Since we've just created the list with one node, the length is 1.
        self.length = 1
    
    # TIME AND SPACE COMPLEXITY:
    # Overall, the provided code takes O(1) time and space for each operation, making it highly efficient.
    # However, keep in mind that as the linked list grows, the total space consumed by the list will be O(n), where n is the number of nodes.


    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node =  temp_node.next
        return result



    # 23. INSERTION AT THE BEGINNING OF A LIST
        
    # This line is defining a new method for the LinkedList class, called prepend. 
    # This method takes two arguments: self, which is a reference to the instance of the LinkedList class that this method is being called on; 
    # and value, which is the data for the new node that will be inserted at the beginning of the list.
    def prepend(self, value):
        
        # This line creates a new instance of the Node class with the given value. 
        # The new_node variable is a local variable in the prepend method that holds a reference to the new node.
        new_node = Node(value)
        
        # This line sets the next attribute of the new_node to point to the current head of the LinkedList. 
        # This is done because new_node is about to become the new head of the list, so it needs to reference the node that will come after it in the list.
        new_node.next = self.head
        
        # This line updates the head attribute of the LinkedList to point to new_node, effectively making new_node the first node in the list. 
        # Since new_node already points to the old head of the list (from the previous line), the rest of the list remains intact.
        self.head = new_node
        
        # This line increments the length attribute of the LinkedList by 1. 
        # This is done because we've just added a new node to the list, so the total number of nodes in the list has increased by 1.
        self.length += 1
        
        # In conclusion, the prepend method allows a new value to be inserted at the start of the LinkedList. 
        # It does this by creating a new node with the given value, linking it to the existing head of the list, then updating the head of the list to be the new node, and finally updating the list's length.

    # TIME AND SPACE COMPLEXITY:
    # each line in the prepend method operates in O(1) time and space complexity, 
    # which means the overall time and space complexity of the method is also O(1).




    # 24. INSERTION AT THE END OF A SINGLY LINKED LIST

    # This line is defining a new method for the LinkedList class, named append. 
    # This method takes two arguments: self, a reference to the instance of the LinkedList class that this method is being called on, 
    # and value, the data for the new node that will be appended at the end of the list.
    def append(self, value):
        
        # This line creates a new instance of the Node class with the given value. 
        # The new_node variable is a local variable in the append method that holds a reference to the new node.
        new_node = Node(value)
        
        # These lines check if the LinkedList is empty, that is, the head and tail are both None. 
        # If it is empty, it assigns the head and tail of the LinkedList to the new_node. 
        # Essentially, the new node becomes the first and only node in the list.
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            
        # These lines execute if the LinkedList is not empty. 
        # It sets the next attribute of the current tail node to new_node, meaning it connects the last node of the LinkedList to the new_node. 
        # Then, it updates the tail attribute of the LinkedList to new_node, as new_node is now the last node in the list.    
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        # This line increments the length attribute of the LinkedList by 1. 
        # This is because we've just added a new node to the list, increasing the total number of nodes in the list by 1.
        self.length += 1
        
        # TIME AND SPACE COMPLEXITY:
        # Every line in the append method operates in constant time O(1) and does not allocate additional space beyond the new node, which also makes the space complexity O(1).

    # 25. DELETION FROM A SINGLY LINKED LIST

    # This line defines the remove method, which is going to take an instance of the LinkedList class (self) and an index as arguments.   
    def remove(self, index):
        
        # This conditional checks whether the provided index is out of the range of valid indices for the linked list (less than 0 or greater than or equal to the number of nodes in the list).
        if index < 0 or index >= self.length:
            
            #  If the above condition is met (the index is out of range), the function returns None and exits.
            return None
        
        # This conditional checks whether the provided index is 0, meaning that the head of the list should be removed.
        elif index == 0:
            # If the head is to be removed, the method saves a reference to it in the popped_node variable.
            popped_node = self.head
            
            # This conditional checks whether the list only contains one node.
            if self.length == 1:
                # If there is only one node, it removes the node by setting the head of the list to None.
                self.head = None
                # Similarly, it sets the tail of the list to None, effectively removing the single node in the list.
                self.tail = None
            
            # This is the alternative case where the list contains more than one node.
            else:
                # It removes the head by setting the head of the list to the next node in the list.
                self.head = self.head.next
            # It disconnects the original head node from the list by setting its next reference to None.
            popped_node.next = None
            #  It decreases the length of the list by 1 to account for the removed node.
            self.length -= 1 
            #  It returns the removed node.
            return popped_node
        
        # This is the alternative case where the node to be removed is not the head.    
        else:
            # It sets temp to the head of the list to start a traversal.
            temp = self.head
            # It starts a loop to reach the node preceding the one to be removed.
            for _ in range(index-1):
                # Inside the loop, it advances temp to the next node in each iteration.
                temp = temp.next
            # After reaching the node preceding the one to be removed, it saves a reference to the node to be removed in popped_node.
            popped_node = temp.next
            
            # This checks if the popped_node is the last node (its next attribute is None).
            if popped_node.next is None:
                #  If popped_node is the last node, it updates the tail of the list to temp, which is the new last node after the removal.
                self.tail = temp
            # It removes popped_node by skipping it in the linked list. It sets the next reference of the node preceding popped_node to the node following popped_node.
            temp.next = temp.next.next
            # It disconnects popped_node from the list by setting its next reference to None.
            popped_node.next = None
            # It decreases the length of the list by 1 to account for the removed node.
            self.length -= 1 
            # It returns the removed node.
            return popped_node
            
        # TIME COMPLEXITY:
        # The time complexity for removing a node from a singly linked list is O(n), where n is the length of the linked list. 
        # This is because in the worst-case scenario, you may have to traverse the entire list (when the node to remove is at the end of the list, or the node does not exist).
        
        # SPACE COMPLEXITY:
        # The space complexity for this operation is O(1), which means it uses constant space. 
        # Despite the size of the linked list, we only create two new variables (temp and popped_node), and we do not use any additional data structures that would grow with the size of the input. 
        # So the space complexity is constant.


    # 26. REVERSE A SINGLY LINKED LIST
    # Defines a method named reverse in the LinkedList class.
    def reverse(self):

        # Initializes prev_node to None. It keeps track of the previous node during traversal.
        prev_node = None

        # Initializes current_node with the head of the linked list. The reverse operation starts from here.
        current_node = self.head

        # Starts a while loop that continues until the end of the linked list is reached.
        while current_node is not None:
            # Saves the next node before overwriting current_node.next in the next step.
            next_node = current_node.next
            # Reverses the link by setting the next of current_node to prev_node.
            current_node.next = prev_node
            # Updates prev_node to current_node for the next iteration.
            prev_node = current_node
            # Moves the current_node one step forward for the next iteration.
            current_node = next_node
        # After the end of the loop, the head and tail are swapped to complete the reversal of the linked list.
        self.head, self.tail = self.tail, self.head

    # TIME COMPLEXITY:
    # Overall, the time complexity for the entire reverse function is O(n) as it traverses all n nodes once.

    # SPACE COMPLEXITY:
    # The space complexity is O(1) as it uses a constant amount of space throughout its execution.



    # 27. FIND THE MIDDLE OF A LINKED LIST

    # Write a function to find and return the middle node of a singly linked list. 
    # If the list has an even number of nodes, return the second of the two middle nodes.
    def find_middle(self):
        # This line initializes the slow pointer at the head of the linked list. 
        # This pointer will move one node at a time through the list.
        slow = self.head
        # This line initializes the fast pointer also at the head of the linked list. 
        # This pointer will move two nodes at a time through the list.
        fast = self.head
        # This line starts a while loop that will continue as long as both fast and fast.next are not None. 
        # This ensures that we do not try to access a None value in the next line, which would raise an error.
        while fast is not None and fast.next is not None:
            # This line moves the slow pointer one node forward in the list.
            slow = slow.next
            # This line moves the fast pointer two nodes forward in the list. 
            # Because fast moves twice as fast as slow, by the time fast reaches the end of the list, slow will be at the middle.
            fast = fast.next.next
        # After the while loop, the slow pointer will be at the middle of the linked list. 
        # This line returns the slow node, which is the middle node of the list.
        return slow

    # TIME COMPLEXITY:
    # The time complexity is O(n), where n is the number of nodes in the linked list. 
    # This is because in the worst-case scenario, we have to traverse the whole linked list. 
    # Here, the 'fast' pointer is moving twice as fast as the 'slow' pointer, but it essentially goes through the entire list (or nearly the entire list in the case of an even number of nodes), so the time complexity is proportional to the size of the list, i.e., O(n).
    
    # SPACE COMPLEXITY:
    # The space complexity is O(1), which means that the space required does not change with the size of the input linked list, hence it's constant. 
    # This is because we are only using a fixed amount of space to store the 'slow' and 'fast' pointers, and we are not using any additional data structures like arrays or other linked lists whose size would scale with the input size. No matter how large the input linked list is, we only ever need two nodes ('slow' and 'fast') at any given time, so the space complexity is O(1).



    # 28. REMOVE DUPLICATE VALUES

    # This line is defining the function remove_duplicates within the LinkedList class.
    def remove_duplicates(self):
        # This line checks if the head of the LinkedList is None, which would indicate that the list is empty.
        if self.head is None:
            # If the list is empty, the function ends execution and returns None.
            return
        # If the list is not empty, the function creates a set node_values.
        node_values = set() # Set to store unique values
        # The function sets current_node to the head of the list. This variable will be used to traverse the list.
        current_node = self.head
        # This line adds the value of the head node to node_values.
        node_values.add(current_node.value)
        # This line starts a while loop that will continue as long as the next attribute of the current_node is not None.
        while current_node.next:
            #  This line checks if the value of the next node is already in the set of unique values.
            if current_node.next.value in node_values: # duplicate found
                # If the value is in the set, this line removes the next node from the list by skipping over it
                # and setting the next attribute of the current node to the node after the next node.
                current_node.next = current_node.next.next
                # Since a node was removed, the length of the list is decremented by 1.
                self.length -= 1
            # This is the other case where the value of the next node is not in the set.
            else:
                # This line adds the value of the next node to the set of unique values.
                node_values.add(current_node.next.value)
                # Since the next node is unique, we move forward to the next node.
                current_node = current_node.next
        # After the loop, the current_node will be the last node in the list. 
        # So, we update the tail of the list to be current_node.
        self.tail = current_node

        # TIME COMPLEXITY:
        # Overall, the time complexity of the remove_duplicates method is O(n), where n is the number of nodes in the linked list. 
        # This is because the while loop iterates through the list once, performing constant-time operations in each iteration.
        
        # SPACE COMPLEXITY:
        # node_values = set(): Creating the set to store unique node values takes constant space, O(1).
        # The space complexity of the remove_duplicates method is O(1), as the space used does not grow with the size of the input. 
        # It only requires a constant amount of extra space to store the set node_values.







new_linked_list = LinkedList(20)
new_linked_list.prepend(10)
new_linked_list.append(30)
print(new_linked_list)
new_linked_list.delete(0)
print(new_linked_list)
