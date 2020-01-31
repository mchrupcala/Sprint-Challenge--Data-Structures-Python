import sys
sys.path.append('../dll')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        #   Because the pointers in a DLL give us a strict order to work with, so queues and stacks can remove/add from the head/tail pretty easily.
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            val = self.storage.remove_from_head()
            self.size -= 1
            return val
        else:
            return

    def len(self):
        return self.size
