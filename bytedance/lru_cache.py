class ListNode:
    def __init__(self, value, key, prev_=None, next_=None):
        self.value = value
        self.key = key
        self.prev_ = prev_
        self.next_ = next_
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.update(key)
            return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.update(key)
            return
        
        if self.capacity == 1:
            if self.size == 1:
                del self.cache[self.head.key]
                self.size -= 1
            self.cache[key] = ListNode(value, key)
            self.head = self.tail = self.cache[key]
            self.size += 1
            return
        
        if self.size == self.capacity:
            rec = self.head
            self.head = self.head.next_
            self.head.prev_ = None
            rec.next_ = None
            self.size -= 1
            del self.cache[rec.key]

        self.cache[key] = ListNode(value, key)
        if self.tail is not None:
            self.tail.next_ = self.cache[key]
            self.cache[key].prev_ = self.tail
        self.tail = self.cache[key]
        if self.head is None:
            self.head = self.cache[key]
        self.size += 1
        
    def update(self, key):
        if self.capacity > 1 and self.cache[key].next_ is not None:
            if self.cache[key].prev_ is None:
                self.head = self.head.next_
                self.head.prev_ = None
            else:
                self.cache[key].prev_.next_ = self.cache[key].next_
                self.cache[key].next_.prev_ = self.cache[key].prev_
            
            self.cache[key].prev_ = self.tail
            self.tail.next_ = self.cache[key]
            self.cache[key].next_ = None
            self.tail = self.cache[key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
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
    lru.get(1)
    lru.get(2)
    lru.get(3)
    lru.get(4)
    # lru.put(4,4)
    # lru.get(1)
    lru.get(5)
    # lru.get(4)