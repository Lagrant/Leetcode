import random

class RandomizedSet:

    def __init__(self):
        self.rset = {}
        self.rarr = []

    def insert(self, val: int) -> bool:
        if val not in self.rset:
            self.rset[val] = len(self.rarr)
            self.rarr.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.rset:
            temp = self.rarr[-1]
            self.rarr[self.rset[val]], self.rarr[-1] = self.rarr[-1], self.rarr[self.rset[val]]
            self.rset[temp] = self.rset[val]
            del self.rset[val]
            self.rarr.pop()
            
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.rarr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
    s = RandomizedSet()
    s.insert(1)
    s.remove(2)
    s.insert(2)
    s.getRandom()
    s.remove(1)
    s.insert(2)
    s.getRandom()