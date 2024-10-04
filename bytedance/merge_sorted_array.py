from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1
        while p >= 0:
            if p2 < 0:
                break
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            if p1 < 0:
                nums1[:p2 + 1] = nums2[:p2 + 1]
        # print(nums1)


if __name__ == '__main__':
    s = Solution()
    s.merge([2,0], 1, [1], 1)