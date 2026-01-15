# MULTIPROCESSING MODULE
# How to use multiprocessing.Queue as a FIFO queue:

# Similar to queue model but allows queue items to be processed in parallel by multiple concurrent workers
# Multiprocessing queue is meant for sharing data between processers and can store any pickable objects
# Multiprocessing queue uses the same methods as the Queue module except for task_done() and join()

from multiprocessing import Queue 

customQueue = Queue(maxsize=3)
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)

print(customQueue.get())
