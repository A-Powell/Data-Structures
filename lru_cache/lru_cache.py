from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
     linked list that holdsthe key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.dll = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage.keys():
            value = self.dll.head  # Starting Point

            while value.key is not key:  # 'Loop' to find the correct match
                value = value.next  # Call next while loops continues until case is matched

            self.dll.move_to_front(value)  # Move node to the front
            return value.value
        else:
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
        if key in self.storage.keys():  # exists?
            self.storage[key] = value
            result = self.dll.head
            while result.key is not key:
                result = result.next
            result.value = value

        elif self.dll.length < self.limit:  # Check limit
            self.dll.add_to_head(key, value)
            self.storage[key] = value
        else:  # If fill, remove last and add to head
            switch_key, switch_value = self.dll.remove_from_tail()
            del self.storage[switch_key]
            self.dll.add_to_head(key, value)
            self.storage[key] = value
