from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value 
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value = None):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    
    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail   

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self


    
    # CODING EXERCISE 42: Remove Duplicates

    # This is the function definition for remove_duplicates
    # It takes one argument ll which is a LinkedList object.
    def remove_duplicates(ll):
        # This condition checks if the head of the linked list is None. 
        # If it's None, it means the list is empty and there are no duplicates to remove
        if ll.head is None:
            # If the LinkedList ll is empty (i.e., the head is None), the function ends and returns None.
            return
        
        # This line sets the current_node to the head of the LinkedList. 
        # current_node will be used to traverse the list.
        current_node = ll.head
        # This line initializes prev_node as None. 
        # prev_node will be used to keep track of the node before current_node
        prev_node = None
        
        # This is the start of the while loop that runs as long as the current_node is not None.
        # This loop is used to traverse the list.
        while current_node:
            # Inside the while loop, runner is set to the current_node. 
            # runner will be used to look ahead in the list for duplicates
            runner = current_node
            # This is a nested while loop that runs as long as runner.next is not None.
            # This loop is used to check for duplicates of current_node's value in the remaining list.
            while runner.next:
                # This is a condition to check if the next value in the list (after runner) is the same as the value of current_node.
                if runner.next.value == current_node.value:
                    # If the above condition is true, it means we have found a duplicate.
                    # So, we bypass the duplicate node by changing runner.next to runner.next.next.
                    runner.next = runner.next.next
                # If the above condition is false...
                else:
                    # ...we move runner one step forward in the list.
                    runner = runner.next
            # After we have checked all the remaining list for duplicates of current_node, we set prev_node to current_node.
            prev_node = current_node
            # We move current_node one step forward in the list.
            current_node = current_node.next
        
        # After the outer while loop ends (meaning we have traversed the entire list), prev_node is the last node in the list.
        # We set ll.tail to prev_node, effectively updating the tail of the LinkedList.
        ll.tail = prev_node
        # The function ends by returning the head of the LinkedList.
        # This is not strictly necessary as the LinkedList is modified in-place, but it could be useful if you want to chain operations.
        return ll.head
    
    # TIME COMPLEXITY: O(N^2) Due to the nested loop
    # SPACE COMPLEXITY: O(1)


    # INTERVIEW QUESTION 2/CODING EXERCISE 43: Return Kth to Last

    def kthToLast(ll, k):
        pointer1 = ll.head
        pointer2 = ll.head

        for i in range(k):
            if pointer2 is None:
                return None
            else:
                pointer2 = pointer2.next

        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1

    # TIME COMPLEXITY: O(n)
    # SPACE COMPLEXITY: O(1)


    # INTERVIEW QUESTION 3/CODING EXERCISE 44: Partition
    def partition(ll, x):
        curNode = ll.head
        ll.tail = ll.head

        while curNode:
            nextNode = curNode.next
            curNode.next = None
            if curNode.value < x:
                curNode.next = ll.head
                ll.head = curNode
            else:
                ll.tail.next = curNode
                ll.tail = curNode
            curNode = nextNode
        if ll.tail.next is not None:
            ll.tail.next = None

    # TIME COMPLEXITY: O(n)
    # SPACE COMPLEXITY: O(1)


    # INTERVIEW QUESTION 4: Sum Linked Lists

    def sumList(llA, llB):
        n1 = llA.head
        n2 = llB.head
        carry = 0
        ll = LinkedList()

        while n1 or n2:
            result = carry
            if n1:
                result += n1.value
                n1 = n1.next
            if n2:
                result += n2.value
                n2 = n2.next
            ll.add(int(result % 10))
            carry = result / 10
        
        return ll
    
    # TIME COMPLEXITY: O(n)
    # SPACE COMPLEXITY: O(n)


    # INTERVIEW QUESTION 5: Intersection
    # Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
    # Note that the intersection is defined based on reference, not value. That is, the kth node of the 
    # first linked list is the exact same node (by reference) as the jth node of the second linked list,
    # then they are intersecting.

    # HINT: Two intersecting linked lists will have the same tail node.
    def intersection(llA, llB):
        if llA.tail is not llB.tail:
            return False
        lenA = len(llA)
        lenB = len(llB)
        
        shorter = llA if lenA < lenB else llB
        longer = llB if lenA < lenB else llA

        diff = len(longer) - len(shorter)
        longerNode = longer.head
        shorterNode = shorter.head 
        for i in range(diff):
            longerNode = longerNode.next

        while shorterNode is not longerNode:
            shorterNode = shorterNode.next
            longerNode = longerNode.next
        
        return longerNode

    # TIME COMPLEXITY: O(A + B)
    # SPACE COMPLEXITY: O(1)
    
    # Helper Function for intersection function.
    def addSameNode(llA, llB, value):
        tempNode = Node(value)
        llA.tail.next = tempNode
        llA.tail = tempNode
        llB.tail.next = tempNode
        llB.tail = tempNode



customLL = LinkedList()
customLL.generate(10, 0, 99)
#print(customLL)
#print(customLL.kthToLast(3))
#customLL.partition(50)
#print(customLL)

llA = LinkedList()
#llA.add(7)
#llA.add(1)
#llA.add(6)
llA.generate(3,0,10)

llB = LinkedList()
llB.generate(4,0,10)
#llB.add(5)
#llB.add(9)
#llB.add(2)

llA.addSameNode(llB, 11)
llA.addSameNode(llB, 14)
print(llA)
print(llB)
#print(llA.sumList(llB))
print(llA.intersection(llB))

