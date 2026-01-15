# CODING EXERCISE 29: Merge Two Sorted Linked Lists

# Definition for singly-linked list.
# This line is declaring a class named ListNode. This class will be used to create nodes for the linked lists.
class ListNode(object):
    # The __init__ method is a special method in Python classes, it's the constructor method which is automatically called when an object of a class is instantiated. 
    # Here, it's used to initialize the val and next attributes of a ListNode.
    def __init__(self, val=0, next=None):
        # This sets the value of the node to the val argument provided.
        self.val = val
        # This sets the next attribute of the node to the next argument provided. 
        # This attribute will point to the next node in the linked list.
        self.next = next

#         
class Solution(object):
    # This is the function definition for mergeTwoLists which takes two sorted linked lists l1 and l2 as arguments.
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Here, we're creating a new node prehead with a value of -1. 
        # This is a dummy node, and the merged linked list will start from this node.
        prehead = ListNode(-1)
 
        # We're creating a pointer prev that will be used to traverse and build the new sorted list.
        # We initially point it to prehead.
        prev = prehead

        # This loop will continue as long as there are nodes left in both l1 and l2.
        while l1 and l2:
            # This line compares the values of the current nodes of l1 and l2.
            # # If the value of the current node in l1 is less than or equal to the current node in l2...         
            if l1.val <= l2.val:
                # ...then we add l1's current node to the new list...
                prev.next = l1
                # ...and move forward in l1.
                l1 = l1.next
            # If the value of the current node in l1 is greater than the current node in l2...
            else:
                # ...then we add l2's current node to the new list... 
                prev.next = l2
                # ...and move forward in l2.
                l2 = l2.next 
            # After adding a node from either l1 or l2 to the new list, we need to move forward in the new list as well.           
            prev = prev.next
 
        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        # After exiting the while loop, at least one of l1 and l2 is null, 
        # so we need to connect the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2
 
        # We're returning prehead.next because prehead is a dummy node. 
        # The sorted, merged list starts from prehead.next.
        return prehead.next

# TIME AND SPACE COMPLEXITY:
# while loop:
# Time complexity: O(n + m) - In the worst case scenario, we have to iterate through all nodes in both l1 and l2.
# Space complexity: O(1) - We are not using any extra space that grows with the size of the input. 
# We are only using a few pointers.
# Every other operation is O(1) for Time and Space.



# CODING EXERCISE 30: Remove Duplicates
class ListNode(object):
    # def __init__(self, val=0, next=None):: This is the constructor of the class. 
    # It initializes a new object (or node) of the class with default parameters. 
    # val has a default value of 0 and next has a default value of None.
    def __init__(self, val=0, next=None):
        # self.val = val: This sets the value of the node to the val argument passed during object creation.
        self.val = val
        # self.next = next: This sets the next pointer of the node, which is used to point to the subsequent node in the linked list.
        self.next = next

# class Solution(object):: This defines a class named Solution.
class Solution(object):
    # def deleteDuplicates(self, head):: This defines a method inside the Solution class which aims to remove duplicates from a linked list.
    # The main logic of the method is to iterate through the list while keeping track of the seen values. 
    # If a node with a seen value is encountered, it's removed from the list. 
    # If the value hasn't been seen before, it's added to the seen set, and the iteration continues.
    def deleteDuplicates(self, head):
        # if not head: return None: This checks if the head of the linked list is None (i.e., if the list is empty). If it's empty, it returns None.
        if not head:
            return None
        # seen = set(): This creates an empty set named seen. 
        # This set will be used to keep track of the values that have already been seen in the linked list.
        seen = set()
        # dummy = ListNode(-1): This creates a dummy node with value -1. 
        # The dummy node is a common technique in linked list problems to simplify edge cases, especially at the beginning of the list.
        dummy = ListNode(-1)
        # dummy.next = head: This links the dummy node to the start of the linked list.
        dummy.next = head
        # prev_node = dummy: This initializes the prev_node variable to the dummy node. 
        # This variable is used to keep track of the previous node while iterating through the list.
        prev_node = dummy
        # current_node = head: This initializes the current_node variable to the head of the linked list, i.e., the first node. 
        # This variable is used to iterate through the list.
        current_node = head

        # while current_node:: This starts a loop that will continue as long as there are nodes left in the list to process.
        while current_node:
            # if current_node.val in seen:: This checks if the value of the current node has already been seen before (i.e., if it's a duplicate).
            if current_node.val in seen: # duplicate found
                # prev_node.next = current_node.next: If it's a duplicate, this line skips the current node by connecting the previous node to the next node of the current one.
                prev_node.next = current_node.next
                # current_node = current_node.next: This moves the current node pointer to the next node in the list.
                current_node = current_node.next
            # else:: If the value of the current node has not been seen before:
            else:
                # seen.add(current_node.val): This adds the value of the current node to the `seen` set.
                seen.add(current_node.val)
                # prev_node = current_node: This updates the `prev_node` to be the current node.
                prev_node = current_node
                # current_node = current_node.next: This moves the current node pointer to the next node in the list.
                current_node = current_node.next
        # return dummy.next: After processing all the nodes, this line returns the linked list starting from the node next to the dummy. 
        # This effectively returns the modified head of the linked list.
        return dummy.next
    
    
    # TIME AND SPACE COMPLEXITY:
    # Total Time Complexity: O(n) primarily because of the loop that goes through all the nodes. 
    # The set operations (lookup, insertion) are usually O(1) on average, but in the worst-case scenario, they could be O(n). However, since we're iterating through the list just once, the dominant factor remains O(n).

    # Total Space Complexity: O(n) because of the seen set which in the worst case might store all unique values from the linked list. 
    # The other operations and variables combined don't exceed this space complexity.


# CODING EXERCISE 31: Remove

# class ListNode(object): This line defines a new class named ListNode. 
# This class represents a node in a linked list, which can store a value and a reference to the next node in the list.
class ListNode(object):
    # def __init__(self, val=0, next=None): This is the initializer method for the ListNode class. 
    # When we create a new ListNode, we can specify its value and the next node it should point to.
    def __init__(self, val=0, next=None):
        # self.val = val This line assigns the provided value to the 'val' attribute of the ListNode.
        self.val = val
        # self.next = next This line assigns the provided next node to the 'next' attribute of the ListNode.
        self.next = next

# class Solution(object):This line defines a new class named Solution, which contains our solution to the problem.
class Solution(object):
    # def removeElements(self, head, val):This line starts the definition of our solution method, which takes a head of a linked list and a value to remove from the list.
    def removeElements(self, head, val):
        # dummy_head = ListNode(-1) Here we're creating a dummy head node. 
        # This node acts as a placeholder and helps handle cases where we need to remove the actual head of the list.
        dummy_head = ListNode(-1)
        # dummy_head.next = head
        # This line sets the next node of our dummy head to be the actual head of the list. 
        # This effectively places our dummy head node at the start of the list.
        dummy_head.next = head
        # prev_node, curr_node = dummy_head, head: This line initializes two pointers that we'll use to traverse the list. 
        # 'prev_node' will keep track of the node before 'curr_node' as we move through the list.
        prev_node, current_node = dummy_head, head
        # while curr_node: This line starts a loop that will continue as long as 'curr_node' is not None, i.e., until we've checked every node in the list.
        while current_node:
            # if curr_node.val == val: This line checks if the value of the current node is the value we want to remove.
            if current_node.val == val:
                # prev_node.next = curr_node.next: If the current node's value is the value we want to remove, this line skips over the current node by setting the 'next' attribute of the previous node to the node after the current one.
                prev_node.next = current_node.next
            # else: prev_node = curr_node If the current node's value isn't the one we want to remove, this line moves the 'prev_node' pointer to the current node.
            else:
                prev_node = current_node
            # curr_node = curr_node.next This line moves the 'curr_node' pointer to the next node in the list, regardless of whether we removed the current node or not.
            current_node = current_node.next
                
        # return dummy_head.next After we've checked every node in the list, this line returns the first node after our dummy head node. 
        # This will be the head of the new list with the specified values removed.
        return dummy_head.next
    
    # TIME COMPLEXITY: O(n)
    # SPACE COMPLEXITY: O(1)


# CODING EXERCISE 32: Reverse a Linked List

# My solution (and as it turns out, the ACTUAL SOLUION as well!)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# This line is declaring a new class called Solution. 
# Classes are a way of grouping related bits of code together, including methods, which are just functions that belong to a class.
class Solution(object):

    # This line is defining a method of the Solution class called reverseList. 
    # This method will take in two parameters: self, which is a reference to the instance of the class, and head, which is the head node of the linked list you want to reverse.
    def reverseList(self, head):

        # This line initializes a variable prev_node to None. 
        # This variable will be used to keep track of the previous node as we traverse the linked list.
        prev_node = None

        # This line initializes another variable current_node to the head of the linked list. 
        # This variable will be used to traverse the linked list.
        current_node = head

        # This line starts a while loop that will continue until current_node is None. 
        # This is essentially saying "keep going until we've visited every node in the linked list".
        while current_node is not None:

            # Inside the while loop, this line saves the next node of curr_node before changing the next of curr_node. 
            # This is crucial because once we reverse curr_node.next, we lose the reference to the next node in the original list.
            next_node = current_node.next

            # This line reverses the direction of the link between the current and the previous node. 
            # Instead of curr_node pointing to the next node in the original list, it now points back to the node before it.
            current_node.next = prev_node

            # This line shifts prev_node one step forward (to the right in the original list). 
            # Now, prev_node is the current_node.
            prev_node = current_node

            # This line also shifts curr_node one step forward. 
            # However, this uses next_node, which we saved before, to move curr_node to its original next node in the list.
            current_node = next_node

        # After the while loop has completed, which means we have traversed and reversed all nodes in the list, curr_node is None (as this condition breaks the while loop) and prev_node is at the last node visited, which is the head of the reversed list. 
        # So, we return prev_node.    
        return prev_node

# head = [1,2,3,4]
# reverseList(head)

# TIME AND SPACE COMPLEXITY:
# Each line inside the loop has a time complexity of O(n), and the loop runs n times. 
# Therefore, the overall time complexity of this method is O(n). 
# Since we're not using any additional data structures that grow with input size, the space complexity of the method is O(1), which is constant space complexity.





# CODING EXERCISE 33: Palindrome Linked List

# 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution(object):
    def isPalindrome(self, head):
        # Here we're setting both slow and fast to start at the head of the linked list. 
        # These are pointers that will be used to traverse the linked list.
        slow = fast = head

        # This line begins a loop that will continue until the fast pointer reaches the end of the list. The fast pointer moves twice as fast as the slow pointer. 
        # So, by the time fast reaches the end, slow will be at the midpoint of the list.
        while fast and fast.next:

            # Inside the loop, we're moving slow one step forward... 
            slow = slow.next
            # ...and fast two steps forward in each iteration. 
            # This is how we ensure slow is at the midpoint when fast reaches the end
            fast = fast.next.next
        
        # We're initializing prev to None before starting to reverse the second half of the linked list.
        prev = None
        # This loop will reverse the second half of the linked list. 
        # It continues until all nodes in the second half are visited.
        while slow:
            # Here we're saving the next node of slow before changing its reference.
            nxt = slow.next
            # This line is making the slow node point back to the previous node, which is the essence of reversing the list.
            slow.next = prev
            # Here, we're moving prev one step forward...
            prev = slow
            # ...and then moving slow to its next node (saved in nxt).
            slow = nxt 

        # This loop will continue as long as there are nodes in the reversed list (prev).
        while prev:
            # Inside this loop, we're comparing the node values of the first half and the second half (reversed). 
            # If any pair of nodes have different values, we return False, implying the list is not a palindrome.
            if head.val != prev.val:
                return False
            # We're moving the pointers of the original list (head)...
            head = head.next
            # ...and reversed list (prev) one step forward for the next comparison in each iteration.
            prev = prev.next
        # If the control reaches this line, it means all pairs of nodes have been checked and none have mismatched. 
        # Hence, we return True because the linked list is a palindrome.
        return True


        # TIME AND SPACE COMPLEXITY:
        # the time complexity of the function is O(n) because each operation involving n is linear. 
        # The space complexity is O(1) as no extra space dependent on the size of the linked list is used.



# CODING EXERCISE 34: Middle

# My Solution:
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow



# Actual Solution:
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#  We're declaring a new class named Solution. 
# In Python, we usually encapsulate related functions and variables inside a class.
class Solution(object):
    # We're defining a method called middleNode inside the Solution class. 
    # This method takes two parameters: self, which is a reference to the current instance of the class, 
    # and head, which is the head of the linked list.
    def middleNode(self, head):
        # Here, we're initializing a variable called fast and setting it equal to head. 
        # This variable will serve as one of our pointers that will traverse through the linked list.
        fast = head
        # This begins a while loop that will continue until fast is None (which would mean we've reached the end of the list) 
        # or fast.next is None (which would mean we're at the second to last node).
        while fast and fast.next:
            # Within the loop, we're moving head one step forward in the list.
            head = head.next
            # Then, we're moving fast two steps forward. 
            # This line also implicitly checks whether fast.next is None, since Python will raise an exception if we try to access None.next.
            fast = fast.next.next
        # Once the loop ends, head is now at the middle node of the list, so we return head.
        return head

# NOTES: 
# The purpose of this method is to find and return the middle node of a linked list. 
# We do this by moving fast twice as fast as head. By the time fast reaches the end of the list, head will be at the middle.


# TIME AND SPACE COMPLEXITY:
# Overall, the time complexity of this function is O(n) because we're traversing the list once. 
# The space complexity is O(1) because we're only using a fixed amount of space that does not grow with the size of the input list.
