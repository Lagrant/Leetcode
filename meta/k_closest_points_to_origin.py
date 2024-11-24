class Point:
    def __init__(self, point) -> None:
        self.coor = point
        self.dis = -(point[0]**2 + point[1]**2)
    
    def __lt__(self, other):
        return True if (self.dis < other.dis) else False
            

class Solution:
    def kClosest(self, points, k: int):
        import heapq
        dis_heap = []
        p_lst = [Point(p) for p in points]
        for p in p_lst:
            if (len(dis_heap) < k):
                heapq.heappush(dis_heap, p)

            elif (len(dis_heap) == k):
                heapq.heappushpop(dis_heap, p)
        
        return [p.coor for p in dis_heap]