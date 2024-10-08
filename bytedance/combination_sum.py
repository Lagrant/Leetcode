from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 1:
            if candidates[0] == target:
                return candidates
        
        def search(cands, arr, acc):
            for i, c in enumerate(cands):
                if acc + c > target:
                    return
                elif acc + c == target:
                    res.append(arr + [c])
                    return
                else:
                    arr.append(c)
                    acc += c
                    search(cands[i:], arr, acc)
                    arr.pop()
                    acc -= c
        candidates.sort()
        res = []
        search(candidates, [], 0)
        return res
    
if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))