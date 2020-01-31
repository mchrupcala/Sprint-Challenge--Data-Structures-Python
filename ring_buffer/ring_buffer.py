from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()


    def append(self, item):
        # Before the buffer's full, add new elements at the end, and keep track of the most recent addition.
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            print(item, self.current.value)
        # but if full & most recent item's the tail, remove the oldest item (head) and head is the newest item
        elif (self.storage.length >= self.capacity) and self.current.next is None:
            print(self.current.value)
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head
        # but if buffer's full and oldest item is NOT the tail, delete the oldest, replace it with new item, and now it's the newest item
        elif self.storage.length >= self.capacity:
            #Something's wrong with the below couple of lines...look at my test printouts
            self.storage.delete(self.current.next)
            self.current.insert_after(item)
            self.storage.length += 1
            self.current = self.current.next
            #VV head.value is breaking at value 20....why?
            print("Current val:", self.current.value, self.storage.head.value)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        temp = self.storage.head
        # print(temp.value)
        if temp is not None:
            while temp.next is not None:
                list_buffer_contents.append(temp.value)
                temp = temp.next
            list_buffer_contents.append(temp.value)

        return list_buffer_contents



# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
