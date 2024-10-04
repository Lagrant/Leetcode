from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i, c in enumerate(cost):
            gas[i] = gas[i] - c
        if sum(gas) < 0:
            return -1
        c_size = len(gas)
        idx = 0
        while gas[idx] < 0:
            idx = (idx + 1) % c_size
        start = idx
        idx = (idx + 1) % c_size
        cum = gas[start]
        cnt = 1
        while cnt <= c_size:
            if cum < 0:
                start = idx
                cum = 0
            else:
                cum += gas[idx]
                idx = (idx + 1) % c_size
                cnt += 1
        return start

if __name__ == '__main__':
    s = Solution()
    st = s.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1])
    print(st)