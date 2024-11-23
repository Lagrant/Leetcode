from typing import List
class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        idx = self.bin_search(candidates, target)
        candidates = candidates[:idx]
        
        ret = self.comb(candidates, target, 0)
        if ret is None: return []
        ret_dict = {}
        for r in ret:
            ret_dict[','.join(map(lambda x: str(x), r))] = 1
        ret2 = []
        for r in ret_dict:
            ret2.append(list(map(lambda x: int(x), r.split(','))))
        return ret2

    def comb(self, cand, target, cum):
        if len(cand) == 0:
            return None
        if len(cand) > 1:
            i = 1
            while cand[i] == cand[i - 1]:
                i += 1

        if cum + cand[0] == target:
            return [[cand[0]]]
        if cum + cand[0] > target:
            return None
        
        ret = []
        cb1 = self.comb(cand[1:], target, cum)
        cb2 = self.comb(cand[1:], target, cum + cand[0])
        if cb1 is not None:
            ret.extend(cb1)
        if cb2 is not None:
            ret.extend([c + [cand[0]] for c in cb2])
        return ret if len(ret) > 0 else None

    def bin_search(self, candidates, target):
        i, j = 0, len(candidates) - 1
        while abs(i - j) > 1:
            mid = (i + j) // 2
            if candidates[mid] > target:
                j = mid
            elif candidates[mid] < target:
                i = mid
            else:
                while mid < len(candidates) and candidates[mid] == target:
                    mid += 1
                return mid
        if candidates[j] <= target:
            return j + 1
        else:
            return i + 1

class Solution(object):
    def combinationSum2(self, candidates, target):
        ans = []
        ds = []
        candidates.sort()


        def findCombination(ind, target):
            if target == 0:
                ans.append(ds[:])
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                findCombination(i + 1, target - candidates[i])
                ds.pop()


        findCombination(0, target)
        return ans
        

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([2,2,2], 2))