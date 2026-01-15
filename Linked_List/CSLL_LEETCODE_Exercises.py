# CODING EXERCISE 35: Implimenting a Circular Singly Linked List
# 
# class Node: - This line defines a new class named Node which will represent each element in the linked list.
class Node:
    # def __init__(self, value): - This is the constructor of the Node class. It initializes a new instance of the Node class.
    def __init__(self, value):
        # self.value = value - This line sets the value of the node to the passed argument value.
        self.value = value
        # self.next = None - This initializes the next pointer of the node to None.
        self.next = None
    
    # def __str__(self): - This method allows a node's value to be printed directly.
    def __str__(self):
        # return str(self.value) - It converts the node's value to a string and returns it.
        return str(self.value)

# class CSLinkedList: - This line defines a new class named CSLinkedList, which will represent the circular singly linked list.
class CSLinkedList:
    
    # def __init__(self): - This is the constructor for the CSLinkedList class.
    def __init__(self):
        # self.head = None - Initializes the head of the list to None.
        self.head = None
        # self.tail = None - Initializes the tail of the list to None.
        self.tail = None
        # self.length = 0 - Initializes the length of the list to 0.
        self.length = 0
    
    # def __str__(self): - This method allows the linked list to be printed as a string of node values.
    def __str__(self):
        # Create temp_node to keep track of iteration
        temp_node = self.head
        result = ""
        # It iterates over the nodes...  
        while temp_node:
            # ...appending each node's value to a result string...
            result += str(temp_node.value)
            temp_node = temp_node.next
            # ...until it loops back to the head, indicating it has traversed the entire circular list.
            if temp_node == self.head:
                break
            result += " -> "
        return result
    
    # def append(self, value): - This method adds a new node with the given value to the end of the list.
    def append(self, value):
        new_node = Node(value)
        # EDGE CASE: If list is empty
        # It checks if the list is empty and appropriately sets the head and tail.
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        # If the list isn't empty, it adjusts the pointers to include the new node at the end.
        else:
            # 1. Point tail to new_node
            self.tail.next = new_node
            # 2. Point new_node to head
            new_node.next = self.head
            # 3. Make new_node the tail
            self.tail = new_node
        # Increase length of LL by 1
        self.length += 1
    
    # def prepend(self, value): - This method adds a new node with the given value to the beginning of the list.
    # Similar to append, but it inserts the node at the beginning and updates the head and the last node's next pointer.
    def prepend(self, value):
        # Create new_node
        new_node = Node(value)
        # EDGE CASE: If LL is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        # increase length of LL by None
        self.length += 1

    # TIME COMPLEXITY:
    # The append and prepend operations have a time complexity of O(1) because they only involve adjusting a few pointers regardless of the list's size.
    # The __str__ method has a time complexity of O(n) where n is the number of nodes in the list since it iterates through each node once.

    # SPACE COMPLEXITY:
    # The space complexity for the entire structure is O(n),
    # where n is the number of nodes in the list, accounting for the space used by each node.





# CODING EXERCISE 36: Delete a node from a Circular Singly Linked List
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
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result
    
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
    
    def delete_by_value(self, value):
        # EDGE CASE 1: List is empty
        # if self.length == 0: - Check if the list is empty. 
        # If it is, there's no node to delete, so the method returns False.
        if self.length == 0:
            return False
        
        # EDGE CASE 2: List only has one Node
        # if self.head == self.tail and self.head.value == value: 
        # - This checks if there is only one node in the list (self.head == self.tail) and if that node's value matches the value we want to delete (self.head.value == value).
        if self.head == self.tail and self.head.value == value:
            # self.head = None - If the above condition is true, 
            # set head to None, effectively removing the only node from the list.
            self.head = None
            # self.tail = None - Similarly, set tail to None, leaving the list empty.
            self.tail = None
            # self.length = 0 - Adjust the length of the list to 0 since we've removed the only node.
            self.length = 0
            # return True - Return True to indicate that the node was successfully deleted.
            return True
        
        # prev_node = None - Initialize a prev_node variable to None. 
        # This will be used to keep track of the node preceding the current node during the traversal.
        prev_node = None
        # current_node = self.head - Start the traversal from the head of the list.
        current_node = self.head
        # while True: - Begin an infinite loop to traverse the list. 
        # The loop will break internally once the node is deleted or the list is fully traversed.
        while True:
            # if current_node.value == value: - Check if the current node's value matches the value to be deleted.
            if current_node.value == value: # Node to delete is found
                # if current_node == self.head: - If the node to be deleted is the head, update self.head to the next node.
                if current_node == self.head: # Node is at the head
                    # self.head = current_node.next - Set the head to the next node in the list.
                    self.head = current_node.next
                    # self.tail.next = self.head - Update the tail's next pointer to point to the new head, maintaining the circular nature of the list.
                    self.tail.next = self.head
                # else: - If the node to be deleted is not the head...
                else:
                    # prev_node.next = current_node.next - Bypass the current node by setting the previous node's next to the current node's next.
                    prev_node.next = current_node.next
                    # if current_node == self.tail: - Check if the node to be deleted is the tail.
                    if current_node == self.tail: # Node is at the tail
                        # self.tail = prev_node - If it is, update self.tail to the previous node.
                        self.tail = prev_node
                # self.length -= 1 - Decrease the length of the list by 1 since a node has been removed.
                self.length -= 1 
                # return True - Return True to indicate that the node was successfully deleted.
                return True
                
            # prev = current - Before moving to the next node, set prev to the current node.
            prev_node = current_node
            # current = current.next - Move to the next node in the list.
            current_node = current_node.next
            
            # if current == self.head: - Check if we have traversed the entire list (back to the head).
            if current_node == self.head: # If we have traversed the entire list
                # break - If we are back at the head, break out of the loop.
                break
        # return False - If the loop completes without finding a node to delete, 
        # return False to indicate that no node with the given value was found.
        return False # Node with the value was not found

    # TIME COMPLEXITY:
    # The worst-case time complexity is O(n), where n is the number of nodes in the list. 
    # This is because, in the worst-case scenario, the method might need to traverse the entire list to find the node to delete.

    # SPACE COMPLEXITY:
    # The space complexity is O(1) since the method uses a constant amount of space regardless of the size of the input list.






# CODING EXERCISE 37: Count the number of nodes
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


    # def count_nodes(self): - This line defines a method named count_nodes in the CSLinkedList class. 
    # The method doesn't take any parameters other than self, which is a reference to the instance of the CSLinkedList class.
    def count_nodes(self):
        # count = 0 - Initializes a counter variable count to 0. 
        # This variable will be used to keep track of the number of nodes in the list.
        count = 0
        # temp = self.head - Initializes a temporary pointer temp to the head of the list. This pointer will be used to traverse the list.
        temp = self.head
        # while temp: - Starts a while loop that continues as long as temp is not None. 
        # This loop is used to traverse through each node in the list.
        while temp:
            # count += 1 - Increments the count by 1 for each node encountered in the list.
            count += 1
            # temp = temp.next - Moves the temp pointer to the next node in the list.
            temp = temp.next
            # if temp == self.head: - Checks if temp has reached the head of the list again, 
            # which would indicate that the entire list has been traversed (since it's circular).
            if temp == self.head:
                # break - If temp is back at the head, the loop breaks, stopping the traversal.
                break
        # return count - Returns the count variable, which now holds the total number of nodes in the list.
        return count

    # TIME COMPLEXITY:
    # The time complexity of the count_nodes method is O(n), where n is the number of nodes in the list. 
    # In the worst case, the method traverses all the nodes in the list exactly once.

    # SPACE COMPLEXITY: 
    # The space complexity is O(1), as the method uses a constant amount of space. 
    # It only has a few primitive variables (count and temp), which do not depend on the size of the input list.




# CODING EXERCISE 38: Split a Circular Singly Linked List into two Equal Halfs
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
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result

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

    def split_list(self):
        # if self.length == 0: - This line checks if the list is empty. 
        # If the list's length is 0, it means there are no elements in the list.
        if self.length == 0:
            # return None, None - If the list is empty, 
            # the method returns two None values, indicating that there are no halves to return.
            return None, None
        
        # Find the middle
        # mid = (self.length + 1) // 2 - This line calculates the midpoint of the list. 
        # The use of (self.length + 1) // 2 ensures that for an odd length, the extra element goes to the first half.
        mid = (self.length + 1) // 2
        # count = 1 - Initializes a counter count to 1. 
        # This counter is used to keep track of when the loop reaches the middle of the list.
        count = 1
        
        # first_list = CSLinkedList() - Creates a new instance of CSLinkedList to store the first half of the original list.
        first_list = CSLinkedList()
        # second_list = CSLinkedList() - Creates another instance of CSLinkedList to store the second half.
        second_list = CSLinkedList()
        
        # current = self.head - Sets a pointer current to the head of the original list to start traversing the list.
        current = self.head
        # last_first_list = None - Initializes a variable to keep track of the last node of the first half.
        last_first_list = None
        
        # Add first half of list into 0 to middle
        # The while count <= mid: loop - This loop iterates over the first half of the list. 
        # It keeps appending the current value to the first_list and moves the current pointer to the next node until the middle of the list is reached.
        while count <= mid:
            # first_list.append(current.value) - Appends the current node's value to the first_list.
            first_list.append(current.value)
            # last_first_list = current - Updates last_first_list to be the current node.
            last_first_list = current
            # current = current.next - Moves to the next node in the list.
            current = current.next
            # count += 1 - Increments the counter.
            count += 1
        
        # After the first loop....    
        # set the tail of the first half
        # if last_first_list: - Checks if there is at least one node in the first list.
        if last_first_list:
            # first_list.tail = last_first_list - Sets the tail of the first list to the last node of the first half.
            first_list.tail = last_first_list
            # first_list.tail.next = first_list.head - Ensures that the first list remains circular by linking the tail to the head.
            first_list.tail.next = first_list.head
            
        
        # Handle the second half
        # The while current != self.head: loop - This loop iterates over the second half of the list, 
        # appending each node's value to the second_list until it reaches the head again, indicating the end of the circular list.
        while current != self.head:
            # second_list.append(current.value) - Appends the current node's value to the second_list.
            second_list.append(current.value)
            # current = current.next - Moves to the next node.
            current = current.next

        # After the second loop....    
        # Set the tail of the second half
        # if second_list.length > 0: - Checks if the second list has at least one node.
        if second_list.length > 0:
            # second_list.tail = self.tail - Sets the tail of the second list to the original list's tail.
            second_list.tail = self.tail
            # second_list.tail.next = second_list.head - Ensures that the second list is circular.
            second_list.tail.next = second_list.head

        # return first_list, second_list - Returns the two halves of the list as separate circular singly linked lists.
        return first_list, second_list
    
    # This method effectively splits a circular singly linked list into two halves, taking care to maintain the circular nature of each half.


    # TIME COMPLEXITY:

    # SPACE COMPLEXITY: 




# CODING EXERCISE 39: Check if a circular linked list is sorted

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(nodes))


    # MY SOLUTION
    def is_sorted(self):
        # EDGE CASE 1: Empty list
        if self.head == None:
            return True
        current = self.head
        prev = self.head
        
        while current:
            current = current.next
            # if prev greater than next, return true, else return False
            if prev.data <= current.data:
                return True 
            prev = prev.next
            return False
        
    

    # ACTUAL SOLUTION
    # We define the method is_sorted, which will operate on an instance of a CircularLinkedList.
    def is_sorted(self):
        # If self.head is None, it means the list is empty. 
        # An empty list is considered sorted by definition because there are no elements to be out of order.
        # If self.head.next == self.head, it means the list has only one node. 
        # A single-node list is also considered sorted, as there's no other node to compare it with.
        if self.head is None or self.head.next == self.head:
            # If either condition in line 2 is true, the method returns True, indicating the list is sorted.
            return True  # An empty list is considered sorted.
        
        # We initialize a temporary pointer temp to the head of the list. This pointer will be used to traverse the circular linked list.
        temp = self.head
        # We start a loop that will continue until temp.next is equal to self.head. 
        # This condition ensures we traverse the entire list but stop before looping around again.
        while temp.next != self.head:
            # Inside the loop, we check if the data of the current node (temp) is greater than the data of the next node (temp.next).
            # If this condition is true, it means the list is not in ascending order, and we return False.
            if temp.data > temp.next.data:
                return False
            # We advance temp to the next node in the list, moving one step forward in the traversal.
            temp = temp.next
        # If the loop completes without finding any unsorted nodes (i.e., the if condition inside the loop never triggers return False), 
        # the function returns True, indicating the list is sorted.
        return True
        
    # TIME COMPLEXITY:
    # The time complexity is O(n), where n is the number of nodes in the circular linked list. 
    # In the worst case, we traverse the entire list once.

    # SPACE COMPLEXITY:
    # The space complexity is O(1). 
    # We only use a constant amount of extra space (the temp variable) regardless of the size of the input list.



# CODING EXERCISE 40: Insert into a Sorted Circular Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node


    # Defines the insert_into_sorted method with data as the parameter. 
    # This method inserts a new node with data into the circular linked list.
    def insert_into_sorted(self, data):
        #Create a new node (new_node) with the given data.
        new_node = Node(data)
        # EDGE CASE 1: Empty list
        if not self.head:
            # If the list is empty, sets self.head to new_node...
            self.head = new_node
            # ...and points new_node.next to itself, creating a circular link.
            new_node.next = new_node
        
        # Check if the new node's data is less than or equal to the data of the head node. 
        # This indicates that the new node needs to be inserted before the current head, becoming the new head.
        elif data <= self.head.data:
            # Call the prepend method to insert the new node at the beginning of the list.
            self.prepend(data)
        # This else block handles the case where the new node needs to be inserted somewhere other than at the beginning.
        else:
            # Initialize a temporary pointer temp to the head of the list, and use to traverse the list.
            temp = self.head
            # Iterate through the list until the correct position for the new node is found. 
            # The loop continues as long as the next node is not the head (ensuring it doesn't loop around) 
            # and the next node's data is less than the new node's data.
            while temp.next != self.head and temp.next.data < data:
                # Move temp to the next node in the list.
                temp = temp.next
            # Insert the new node into its correct position by adjusting the pointers. new_node.next is set to temp.next, 
            new_node.next = temp.next
            # and temp.next is set to new_node, effectively inserting new_node between temp and temp.next.
            temp.next = new_node

    # TIME COMPLEXITY:
    # The worst-case time complexity is O(n), where n is the number of nodes in the list. 
    # This occurs when the new node needs to be inserted at the end of the list or when it's greater than all existing nodes, 
    # requiring a full traversal.
    
    # SPACE COMPLEXITY:
    # The space complexity is O(1) because the method uses a fixed amount of space regardless of the input size. 
    # It only creates one new node and a few pointers, all of which occupy constant space.





# CODING EXERCISE 41: Josephus Circle Using a Circular Singly Linked List.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def count_nodes(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count

    def delete_node(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = cur.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self, step):
        # temp is initialized to the head of the circular linked list. This variable will be used to traverse the list.
        temp = self.head

        # This while loop continues as long as there are more than one node in the list. 
        # The goal is to keep eliminating nodes until only one remains.
        while self.count_nodes() > 1:
            # count is used to track the number of steps taken as we move through the circular linked list.
            count = 1 
            # This inner while loop moves temp step - 1 times through the list (since we also count the starting node), 
            # effectively landing on the step-th node.
            while count != step:
                temp = temp.next
                count += 1
            # Prints the data of the node that is about to be removed.
            print(f"Removed: {temp.data}")
            # Removes the node at the temp position from the list.
            self.delete_node(temp.data)
            # Moves temp to the next node after the deletion, preparing for the next round of elimination.
            temp = temp.next
            
        # Once the loop ends, temp will be at the last remaining node. 
        # The data of this node is returned, indicating the last person standing.
        return f"Last person left standing: {temp.data}"

    # TIME COMPLEXITY:
    # The outer while loop runs as long as there are more than one nodes in the list. 
    # In the worst case, this will be n times where n is the number of nodes.
    # Inside the outer while loop, there's a count which goes up to step. 
    # However, since the steps are taken on a circular list, this can be considered as O(n) in the worst case (when step is approximately n).
    # count_nodes() is called in each iteration of the outer while loop. 
    # This method itself has a time complexity of O(n) because it traverses the entire list to count the nodes.
    # Therefore, the overall time complexity is O(n^2), as for each of the n nodes, 
    # we could potentially be traversing an n-sized list (due to count_nodes() and the inner while loop).

    # SPACE COMPLEXITY: 
    # The space complexity is O(1) since we are using a fixed number of variables (temp and count) and not using any additional data structures that grow with the input size. 
    # The space taken by the circular linked list itself is not considered here as it is the input to the function.


