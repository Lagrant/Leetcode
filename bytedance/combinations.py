from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def cbn(acc: List, idx):
            if len(acc) == k:
                res.append(acc.copy())
                return
            if n + 1 - idx + len(acc) < k:
                return
            
            for i in range(idx, n + 1):
                acc.append(i)
                cbn(acc, i + 1)
                acc.pop()

        if n == 1:
            return [[n]]
        if k == 1:
            return map(lambda x: [x], range(1, n + 1))
        
        res = []
        for i in range(1, n + 1):
            cbn([i], i + 1)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))