from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dis = []
        for a in arr:
            dis.append([abs(x - a), a])
        dis.sort(key=lambda x: x[0])
        start = k
        laste = dis[k - 1]
        while start < len(arr):
            if dis[start][0] == laste[0]:
                start += 1
            else:
                break
        dis = dis[:start]
        dis[k:start] = sorted(dis[k:start], key=lambda x: x[1])
        dis = dis[:k]
        subarr = [d[1] for d in dis]
        subarr.sort()
        return subarr
    
    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = left + (right - left) // 2
            print(mid, mid + k)
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left: left + k]
    
if __name__ == '__main__':
    s = Solution()
    print(s.findClosestElements([1,2,3,4,5], 4, 3)) # [1,2,3,4]