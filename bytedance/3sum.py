from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums_i = [[n,i] for i, n in enumerate(nums)]
        nums_i = sorted(nums_i, key=lambda x: x[0])
        dup = {}
        for i in range(len(nums_i)):
            j, k = i + 1, len(nums_i) - 1
            while j < k:
                if nums_i[j][0] + nums_i[k][0] == -nums_i[i][0]:
                    t = [nums_i[i][0], nums_i[j][0], nums_i[k][0]]
                    ts = ','.join(map(lambda x: str(x), t))
                    if ts not in dup:
                        triplets.append(t)
                        dup[ts] = True
                    j += 1
                    while j < k and nums_i[j][0] ==nums_i[j - 1][0]:
                        j += 1
                    k -= 1
                    while k > j and nums_i[k][0] == nums_i[k + 1][0]:
                        k -= 1
                elif nums_i[j][0] + nums_i[k][0] > -nums_i[i][0]:
                    k -= 1
                else:
                    j += 1
        return triplets
    
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        neg = defaultdict(int)
        pos = defaultdict(int)
        zeros = 0
        
        for x in nums:
            if x < 0:
                neg[x] += 1
            elif x > 0:
                pos[x] += 1
            else:
                zeros += 1
        
        r = []
        
        if zeros:
            for n in neg:
                if -n in pos:
                    r.append((0, n, -n))
        
            if zeros > 2:
                r.append((0,0,0))

        for set_a, set_b in ((neg, pos), (pos, neg)):
            set_a_items = list(set_a.items())
            for i, (x, q) in enumerate(set_a_items):
                for x2, q2 in set_a_items[i:]:
                    if x != x2 or (x == x2 and q > 1):
                        if -x-x2 in set_b:
                            r.append((x, x2, -x-x2))

        return r


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum2([-1,0,1,2,-1,-4]))