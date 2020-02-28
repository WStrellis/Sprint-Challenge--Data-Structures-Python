from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.dll = DoublyLinkedList()
        self.limit = limit  # maximum number of items
        self.size = 0  # current number of items
        self.nodes = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # get item from cache
        found_item = self.nodes.get(key)
        if found_item:
            # update MRU
            self.dll.move_to_front(found_item)
            return found_item.value[1]
        # item does not exist
        return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # check if key exists
        if key in self.nodes:
            # move to MRU
            self.dll.move_to_front(self.nodes.get(key))
            #  update ref key
            self.nodes[key] = self.dll.head
            # update value
            self.dll.head.value = (key, value)
            return
        # if no check size. If at limit delete LRU.
        if self.size == self.limit:
            # remove from nodes
            del self.nodes[self.dll.tail.value[0]]
            # remove from dll
            self.dll.remove_from_tail()
            # decrement  size
            self.size -= 1
        # add item to dll
        self.dll.add_to_head((key, value))
        # add item to nodes
        self.nodes[key] = self.dll.head
        # increment size
        self.size += 1
