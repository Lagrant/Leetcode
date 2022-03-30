from collections import defaultdict
class DetectSquares:

    def __init__(self):
        self.cols = defaultdict(dict)
        self.rows = defaultdict(dict)

    def add(self, point) -> None:
        self.cols[point[0]][point[1]] = self.cols[point[0]].get(point[1], 0) + 1
        self.rows[point[1]][point[0]] = self.rows[point[1]].get(point[0], 0) + 1

    def count(self, point) -> int:
        p_cols = self.cols[point[0]]
        if len(list(p_cols.keys())) == 0:
            return 0

        row_dict = self.rows[point[1]]
        # for row in self.rows[point[1]]:
            # row_dict[row[0]] = row_dict.get(row[0], 0) + 1
        
        cnt = 0
        for col in p_cols:
            if col == point[1]:
                continue
            size = abs(col - point[1])
            if size + point[0] in row_dict:
                if size + point[0] in self.rows[col]:
                    cnt += self.rows[col][size + point[0]] * row_dict[size + point[0]] * self.rows[col][point[0]]
            if point[0] - size in row_dict:
                if point[0] - size in self.rows[col]:
                    cnt += self.rows[col][point[0] - size] * row_dict[point[0] - size] * self.rows[col][point[0]]

        return cnt

# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()
obj.add([5, 10])
obj.add([10, 5])
obj.add([10, 10])
p1 = obj.count([5, 5])
obj.add([3, 0])
obj.add([8, 0])
obj.add([8, 5])
p2 = obj.count([3, 5])
obj.add([9, 0])
obj.add([9, 8])
obj.add([1, 8])
p3 = obj.count([1, 0])
obj.add([0, 0])
obj.add([8, 0])
obj.add([8, 8])
p3 = obj.count([0, 8])
# p3 = obj.count([11, 10])