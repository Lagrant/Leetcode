class Solution:
    def searchRange(self, nums, target: int):
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        if len(nums) == 2:
            if target not in nums:
                return [-1, -1]
            if nums[0] == nums[1] == target:
                return [0, 1]
            idx = nums.index(target)
            return [idx, idx]
        
        piv = self.search(nums, target)
        if piv == -1:
            return [-1, -1]
        pleft = self.searchLeft(nums, piv)
        pright = self.searchRight(nums, piv)
        return [pleft, pright]
        
    def searchLeft(self, nums, pivot):
        if pivot == 0 or nums[pivot - 1] != nums[pivot]:
            return pivot
        if nums[0] == nums[pivot]:
            return 0
        
        target = nums[pivot]
        pivot -= 1
        i, j = 0, pivot
        while abs(i - j) > 1:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid
            if nums[mid] == target:
                j = mid
        return j

    def searchRight(self, nums, pivot):
        if pivot == len(nums) - 1 or nums[pivot + 1] != nums[pivot]:
            return pivot
        if nums[-1] == nums[pivot]:
            return len(nums) - 1
        
        target = nums[pivot]
        pivot += 1
        i, j = pivot, len(nums) - 1
        while abs(i - j) > 1:
            mid = (i + j) // 2
            if nums[mid] > target:
                j = mid
            if nums[mid] == target:
                i = mid
        return i
        
        
    def search(self, nums, target):
        i, j = 0, len(nums) - 1
        while abs(j - i) > 1:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                j = mid
            else:
                i = mid
        if nums[i] == target:
            return i
        if nums[j] == target:
            return j
        return -1
            
if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([1,2,3], 1))