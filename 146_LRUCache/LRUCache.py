'''
LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache. It
should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists
           in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present.
                  When the cache reached its capacity, it should invalidate the
                  least recently used item before inserting a new item.
'''

# Use a dict and a list is not a good solution, it won't passed the OJ due to
# Time Limit Exceeded with 2048 inputs. But it's easier for understanding

class LRUCache:
    data = {}
    keys = []
    size = 0
    capacity = 0
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        if key not in self.keys:
            return -1
        
        self.keys.remove(key)
        self.keys.append(key)
        
        return self.data[key]

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.keys:
            self.size += 1
            self.keys.append(key)
            if self.size > self.capacity:
	        lru_key = self.keys.pop(0)
                del self.data[lru_key]
                self.size -= 1
        
        self.data[key] = value
