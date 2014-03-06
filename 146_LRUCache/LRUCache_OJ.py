'''
LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache. It
should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists
           in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present.
                  When the cache reached its capacity, it should invalidate the
                  least recently used item before inserting a new item.

Solution:
 - use double linked list to maintain the node
 - use hash map to do search operation
'''

class ListNode:
    def __init__(self, key, val, next, prev):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0
        self.hash = {}

    def __repr__(self):
        node = self.head
        while node != self.tail:
            print node.key, node.val
            node = node.next

    # @return an integer
    def get(self, key):
        if key in self.hash:
	        node = self.hash[key]
	        self.update_position(node)
	        return node.val
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.hash:
	        node = self.hash[key]
	        self.update_position(node)
	        node.val = value
	        return

        if self.size == self.capacity: # remove tail node
            del self.hash[self.tail.key]
            # save the node to tail node and update postion later
            node = self.tail
            node.key = key
            node.val = value
        else:
            # create a new node and put it after tail
            node = ListNode(key, value, None, self.tail)
            if self.head is None: # init the link list for one node
                self.head = node
                self.tail = node
            else: # point tail to the new node
                self.tail.next = node
                self.tail = node

            self.size += 1

        self.hash[key] = node
        self.update_position(node)

    # put node before the head node
    def update_position(self, node):
        if self.head == node:
            return
        prev = node.prev
        next = node.next
        prev.next = next
        if next is not None:
            next.prev = prev
        else:
            self.tail = prev
        head = self.head
        head.prev = node
        self.head = node
        node.next = head
        node.prev = None

