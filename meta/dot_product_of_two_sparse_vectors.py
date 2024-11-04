from typing import List
class SparseVector:
    def __init__(self, nums: List[int]):
        self.v = []
        self.idx = []
        for i, n in enumerate(nums):
            if n == 0:
                continue
            self.v.append(n)
            self.idx.append(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        idx1, idx2 = {}, {}
        for i, d in enumerate(self.idx):
            idx1[d] = i
        for i, d in enumerate(vec.idx):
            idx2[d] = i
        cum = 0
        for d, val in idx1.items():
            if d not in idx2:
                continue
            cum += self.v[val] * vec.v[idx2[d]]
        return cum
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)