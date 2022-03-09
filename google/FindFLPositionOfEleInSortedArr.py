class Solution:
    """
    I can use two functions independently instead of a parameter
    to switch two cases
    """
    def searchRange(self, nums, target: int):
        def search(nums, start, end, left=True):
            if (start > end):
                return -1
            if (end - start <= 1):
                if (left):
                    if (nums[end] == target and nums[start] < target):
                        return end
                    elif (nums[end] == nums[start] == target or nums[start] == target and nums[end] > target):
                        return start
                    else:
                        return -1
                else:
                    if (nums[end] > target and nums[start] == target):
                        return start
                    elif (nums[end] == nums[start] == target or nums[end] == target and nums[start] < target):
                        return end
                    else:
                        return -1
            mid = int((end + start) / 2)
            if (nums[mid] > target):
                return search(nums, start, mid - 1, left)
            elif (nums[mid] < target):
                return search(nums, mid + 1, end, left)
            
            elif (nums[mid] == target):
                if (left):
                    return search(nums, start, mid, left)
                else:
                    return search(nums, mid, end, left)

        if (len(nums) == 0 or target > nums[-1] or target < nums[0]):
            return [-1, -1]
        
        first, last = -1, -1
        mid = int(len(nums) / 2)
        if (nums[mid] >= target):
            first = search(nums, 0, mid, True)
        elif (nums[mid] < target):
            first = search(nums, mid + 1, len(nums) - 1, True)

        mid = int((len(nums) + first) / 2)
        if (nums[mid] > target):
            last = search(nums, 0, mid - 1, False)
        elif (nums[mid] <= target):
            last = search(nums, mid, len(nums) - 1, False)

        if(-1 in [first, last]):
            k = - first * last
            return [k, k]
        
        return [first, last]

sol = Solution()
print(sol.searchRange(nums = [1,1,2,2,2,3,3,3,3,3,4,5,5,5,6,7,8,8,9,9,9,10], target = 7))