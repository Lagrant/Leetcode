from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n_dict = {}
        for n in nums:
            n_dict[n] = 1
        piv, visited, max_cnt = 0, {}, 1
        while piv < len(nums):
            if nums[piv] in visited:
                piv += 1
                continue
            if (nums[piv] + 1 not in n_dict) and (nums[piv] - 1 not in n_dict):
                visited[nums[piv]] = 1
                piv += 1
                continue

            visited[nums[piv]] = 1
            cnt = 1
            next_ = nums[piv] + 1
            while next_ in n_dict:
                cnt += 1
                visited[next_] = 1
                next_ += 1
            
            prev_ = nums[piv] - 1
            while prev_ in n_dict:
                cnt += 1
                visited[prev_] = 1
                prev_ -= 1
            if cnt > max_cnt:
                max_cnt = cnt
            piv += 1
        return max_cnt

if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))