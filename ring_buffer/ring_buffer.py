from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()


    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        elif self.storage.length == self.capacity and self.current == self.storage.tail:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head
        elif self.storage.length >= self.capacity:
            #Something's wrong with the below couple of lines...look at my test printouts
            self.storage.delete(self.current.next)
            self.current.insert_after(item)
            self.current = self.current.next


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        temp = self.storage.head
        while temp.next is not None:
            list_buffer_contents.append(temp.value)
            temp = temp.next
        list_buffer_contents.append(temp.value)

        return list_buffer_contents









    # def append(self, item):
        # x = self.storage.head
        # while x is not None:
        #     print(self.storage.length, x.value)
        #     x = x.next
    #     if self.storage.length < self.capacity:
    #         self.storage.add_to_head(item)
    #         if self.current is None:
    #             self.current = self.storage.head
    #     else:
    #         temp = self.storage.head
    #         while temp.value != self.current.value:
    #             temp = temp.next
    #         self.current = self.current.prev
    #         self.storage.delete(temp.next)
    #         temp.insert_after(item)

    # def get(self):
    #     # Note:  This is the only [] allowed
    #     list_buffer_contents = []
    #     temp = self.storage.tail
    #     while temp.prev is not None:
    #         list_buffer_contents.append(temp.value)
    #         temp = temp.prev
    #     list_buffer_contents.append(temp.value)

    #     return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
