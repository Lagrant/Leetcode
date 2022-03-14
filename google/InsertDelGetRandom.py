import random
class RandomizedSet:

    def __init__(self):
        self.elements = {}

    def insert(self, val: int) -> bool:
        if (val not in self.elements):
            self.elements[val] = 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if (val in self.elements):
            self.elements.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        keys = list(self.elements.keys())
        k = random.randint(0, len(keys)-1)
        return keys[k]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []
    
    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.dict:
            self.list[self.dict[val]], self.list[len(self.list) - 1] = self.list[len(self.list) - 1],self.list[self.dict[val]]
           
           
            self.dict[self.list[self.dict[val]]] = self.dict[val]
            self.list.pop()
            self.dict.pop(val)
            return True
        else:
            return False
        
        

    def getRandom(self) -> int:
        return choice(self.list)