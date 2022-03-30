from collections import defaultdict
import heapq
class Element(list):
    def __lt__(self, other):
        return self[1] < other[1]

class StockPrice:

    def __init__(self):
        self.stocks = defaultdict(int)
        self.latest = -1
        self.max_price = []
        self.min_price = []

    def update(self, timestamp: int, price: int) -> None:
        if timestamp not in self.stocks:
            
            if timestamp > self.latest:
                self.latest = timestamp
            self.stocks[timestamp] = price
            heapq.heappush(self.max_price, Element([timestamp, -price]))
            heapq.heappush(self.min_price, Element([timestamp, price]))
        else:
            if (self.max_price[0][0] == timestamp):
                heapq.heappop(self.max_price)
                heapq.heappush(self.max_price, Element([timestamp, -price]))
            else:
                heapq.heappush(self.max_price, Element([timestamp, -price]))

            if (self.min_price[0][0] == timestamp):
                heapq.heappop(self.min_price)
                heapq.heappush(self.min_price, Element([timestamp, price]))
            else:
                heapq.heappush(self.min_price, Element([timestamp, price]))
            self.stocks[timestamp] = price

    def current(self) -> int:
        return self.stocks[self.latest]

    def maximum(self) -> int:
        while -self.max_price[0][1] != self.stocks[self.max_price[0][0]]:
            heapq.heappop(self.max_price)

        return -self.max_price[0][1]

    def minimum(self) -> int:
        while self.min_price[0][1] != self.stocks[self.min_price[0][0]]:
            heapq.heappop(self.min_price)

        return self.min_price[0][1]


# Your StockPrice object will be instantiated and called as such:
obj = StockPrice()
obj.update(1,10)
obj.update(2,5)
param_2 = obj.current()
param_3 = obj.maximum()
# param_4 = obj.minimum()
obj.update(1,3)
p4 = obj.maximum()
p4