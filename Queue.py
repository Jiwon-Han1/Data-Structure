'''

[ Queue ]

#-- FIFO (First-In-First-Out):
Queue is a linear data structure that follows the FIFO principle, 
where the element that is inserted first is the one that is removed first.

#-- Basic Operatioins:
- Enqueue: adding an element to the rear end of the queue.
- Dequeue: Removing and returning the element from the front end of the queue.
- Front: Returning the element at the front end of the queue without removing it.
- Rear: Returning the element at the rear end of the queue without removing it.
- IsEmpty: Checking if the queue is empty.
- Size: Returning the number of elements currently in the queue.

#-- Implementation Details:
Instead of List, which requires the change of indices after dequeuing,
one can use Python's collections.deque for efficient queue operations.

'''

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque([])    # This is the point!

    def size(self):
        return len(self.items)
        
    def isEmpty(self, verbose=True):
        if self.size() == 0:
            print("### Queue is empty!\n" if verbose == True else "")
            return True
        else:
            return False

    def enqueue(self, item, verbose=True):
        self.items.append(item)
        print("==> Enqueue: "+str(item)+"\n" if verbose==True else "") 

    def dequeue(self, verbose=True):        
        if self.size() != 0:
            value = self.items.pop()
            print("==> Dequeue: "+str(value)+"\n" if verbose==True else "") 
            return value
        else:
            print("Queue is empty!\n")

    def front(self, verbose=True):
        if self.size() != 0:
            print("Front: "+str(self.items[0])+"\n" if verbose==True else "") 
            return self.items[0]
        else:
            print("Queue is empty!\n")

    def rear(self, verbose=True):
        if self.size() != 0:
            print("Rear: "+str(self.items[self.size()-1])+"\n" if verbose==True else "") 
            return self.items[self.size()-1]
        else:
            print("Queue is empty!\n")

    def display(self):
        print("# Display Queue: "+str(list(self.items))+"\n")
        return self.items

if __name__ == "main__":
    Q = Queue()
    Q.isEmpty()
    
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    
    Q.front()
    Q.rear()
    Q.display()
    
    Q.dequeue()
    Q.dequeue()
    Q.dequeue()
    
    Q.display()
