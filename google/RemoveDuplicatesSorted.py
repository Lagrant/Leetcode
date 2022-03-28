class Solution:
    def removeDuplicates(self, nums) -> int:
        cursor = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[cursor]:
                continue
            if i == cursor + 1:
                cursor += 1
                continue
            cursor += 1
            nums[cursor] = nums[i]
        return cursor + 1