class Cell:
    def __init__(self, val, key, prev=None, next=None) -> None:
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head = None    # head of the cache cell linked list
        self.tail = None

    def get(self, key: int) -> int:
        if (key in self.cache):
            if (self.cache[key].next is not None):
                self.cache[key].next.prev = self.cache[key].prev
            else:
                return self.head.val
            
            if (self.cache[key].prev is not None):
                self.cache[key].prev.next = self.cache[key].next
            elif (self.tail.next is not None):
                self.tail = self.tail.next
            
            self.head.next = self.cache[key]

            self.cache[key].prev = self.head
            self.cache[key].next = None
            self.head = self.cache[key]
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if (key in self.cache):
            self.cache[key].val = value
            if (self.cache[key].next is not None):
                self.cache[key].next.prev = self.cache[key].prev
            else:
                return
            
            if (self.cache[key].prev is not None):
                self.cache[key].prev.next = self.cache[key].next
            else:
                self.tail = self.tail.next
            

            self.head.next = self.cache[key]
            self.cache[key].prev = self.head
            self.cache[key].next = None
            self.head = self.cache[key]

        elif (self.size < self.capacity):
            self.cache[key] = Cell(value, key, self.head)
            if (self.head is None):
                self.tail = self.head = self.cache[key]
            else:
                self.head.next = self.cache[key]
                self.head = self.cache[key]
            self.size += 1
        else:
            new_tail = self.tail.next
            if (new_tail is not None):
                new_tail.prev, self.tail.next = None, None
                self.tail.prev = self.head
                self.head.next = self.tail
                self.head, self.tail = self.tail, new_tail

            old_key = self.head.key
            self.cache.pop(old_key)
            self.cache[key] = self.head
            self.head.key = key
            self.head.val = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
cache = {}
cache[key] = class cell:
val
prev
next
"""

lru = LRUCache(3)

lru.put(1, 1)
lru.put(2, 2)
lru.put(3, 3)
lru.put(4, 4)
lru.get(4)
lru.get(3)
lru.get(2)
lru.get(1)
lru.put(5, 5)
# lru.put(4, 1)
lru.get(1)
lru.get(2)
lru.get(3)
lru.get(4)
lru.get(5)


from collections import OrderedDict

class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        
        if len(self) > self.capacity:
            self.popitem(last=False)