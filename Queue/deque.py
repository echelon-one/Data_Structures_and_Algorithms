# COLLECTIONS MODULE
# How to use collections.deque as a FIFO queue:

from collections import deque

customQueue = deque(maxlen=3)
print(customQueue)


customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
# This last one will make the queue overwrite the first element of 1 with the 2
customQueue.append(4)
print(customQueue)
# The popleft method will remove the new first element of 2
print(customQueue.popleft())
print(customQueue)
# The clear method will remove all elements from the queue
print(customQueue.clear())
print(customQueue)
