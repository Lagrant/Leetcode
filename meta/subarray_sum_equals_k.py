from typing import List
from collections import deque, defaultdict
class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subcnt = 0
        sumarr, sumdict = [0], defaultdict(list)
        for n in nums:
            sumarr.append(sumarr[-1] + n)
            if sumarr[-1] == k:
                subcnt += 1
        sumarr = sumarr[1:]
        for i, sa in enumerate(sumarr):
            sumdict[sa].append(i)
        for i, sa in enumerate(sumarr):
            if k == 0:
                if len(sumdict[sa]) > 1:
                    subcnt += len(sumdict[sa]) - 1
                    del sumdict[sa]
                continue
            if sa + k in sumdict:
                for j in range(len(sumdict[sa + k]) -1, -1, -1):
                    if sumdict[sa + k][j] > i:
                        subcnt += 1
                    else:
                        break

        return subcnt
    
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        prefix_sum_count = {0: 1}  # Initialize with prefix sum 0 and count 1
        
        for num in nums:
            prefix_sum += num  # Update the running prefix sum
            if (prefix_sum - k) in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]  # Increment count if (prefix_sum - k) is found
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1  # Update the frequency of the current prefix sum
            else:
                prefix_sum_count[prefix_sum] = 1  # Initialize the frequency if the prefix sum is seen for the first time
        
        return count
    
if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([-1, -1, 1], 0))