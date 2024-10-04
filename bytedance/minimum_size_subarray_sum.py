from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cum = [0] * len(nums)
        cum[0] = nums[0]
        for i in range(1, len(nums)):
            cum[i] = cum[i - 1] + nums[i]
        if cum[-1] < target:
            return 0
        if cum[0] >= target:
            return 1
        if cum[-1] == target:
            return len(nums)
        for i, n in enumerate(cum):
            if n >= target:
                interv = i + 1
                break
        piv = 1
        while piv < len(cum):
            next_end = piv + interv - 1 if piv + interv - 1 < len(cum) else len(cum) - 1
            if cum[next_end] < target + cum[piv - 1]:
                piv += 1
                continue
            if cum[next_end] == target + cum[piv - 1]:
                if next_end == len(cum) - 1:
                    interv = next_end - piv + 1
                    break
                else:
                    piv += 1
                    continue
            interv = self.bin_search(cum[piv: next_end + 1], target + cum[piv - 1]) + 1
            piv += 1
        return interv

    def bin_search(self, arr, t):
        i, j = 0, len(arr) - 1
        while abs(i - j) > 1:
            mid = (i + j) // 2
            if arr[mid] < t:
                i = mid
            elif arr[mid] > t:
                j = mid
            else:
                while arr[mid] == t:
                    mid -= 1
                return mid + 1
        return j if arr[j] > t else -1
    
if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(5, [2,3,1,1,1,1,1]))