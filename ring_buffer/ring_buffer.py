from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.size = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.size == self.capacity:
            # remove last item from dll
            self.storage.remove_from_tail()
            self.size -= 1
        # add new item to dll.head
        self.storage.add_to_head(item)
        # increment size
        self.size += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        self.current = self.storage.tail
        while self.current:
            list_buffer_contents.append(self.current.value)
            self.current = self.current.prev

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
