class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if (len(nums1) > len(nums2)):
            return self.findMedianSortedArrays(nums2, nums1)
        
        l1 = len(nums1)
        l2 = len(nums2)
        _min = -2**31+1
        _max = 2**31 -1
        low, high = 0, l1
        while (low <= high):
            mid1 = int((low + high) / 2)
            mid2 = int((l1 + l2 + 1) / 2 - mid1)

            x1 = _min if (mid1 == 0) else nums1[mid1 - 1]
            y1 = _max if (mid1 == l1) else nums1[mid1]
            x2 = _min if (mid2 == 0) else nums2[mid2 - 1]
            y2 = _max if (mid2 == l2) else nums2[mid2]

            if (x1 > y2):
                high = mid1 - 1
            elif (x2 > y1):
                low = mid1 + 1
            else:
                if ((l1 + l2) % 2):
                    return max(x1, x2)
                else:
                    return (max(x1, x2) + min(y1, y2)) / 2.
        
        return 0.0

sol = Solution()
print(sol.findMedianSortedArrays([1],[2, 3, 4, 5]))