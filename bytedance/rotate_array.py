from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_size = len(nums)
        cnt = 0
        k = k % n_size
        for i in range(1, k + 1):
            if cnt == n_size:
                break
            piv = -i
            prev_p = first_p = piv
            curr_p = (first_p + k) % n_size
            temp = nums[prev_p]
            temp, nums[curr_p] = nums[curr_p], temp
            cnt += 1

            while cnt < n_size and curr_p != first_p and curr_p != (first_p % n_size):
                prev_p = curr_p
                curr_p = (prev_p + k) % n_size
                temp, nums[curr_p] = nums[curr_p], temp
                cnt += 1

if __name__ == '__main__':
    s = Solution()
    s.rotate([1,2,3,4,5,6], 4)