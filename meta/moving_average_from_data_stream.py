from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.stream = deque()
        self.cur_avg = 0

    def next(self, val: int) -> float:
        self.stream.append(val)

        if len(self.stream) <= self.size:
            self.cur_avg = (self.cur_avg * (len(self.stream) - 1) + val) / len(self.stream)
            return self.cur_avg
        else:
            self.cur_avg = self.cur_avg - (self.stream[0] - val) / self.size
            self.stream.popleft()
            return self.cur_avg


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)