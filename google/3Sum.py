class Solution:
    def find(self, piv, nums):
        if (len(nums) == 0):
            return -1
        elif (len(nums) == 1):
            return 0 if (nums[0] == piv) else -1
        
        start = 0
        end = len(nums) - 1
        while (end - start > 1):
            mid = int((start + end) / 2)
            if (nums[mid] == piv):
                return mid
            elif (nums[mid] < piv):
                start = mid
            else:
                end = mid
        if (nums[start] == piv):
            return start
        elif (nums[end] == piv):
            return end
        else:
            return -1

    def threeSum(self, nums):
        sum3 = []
        if (len(nums) < 3):
            return sum3

        nums.sort()
        piv = 0
        for i in range(len(nums) - 1):
            if (nums[i] == 0):
                piv = i
                break
            elif (nums[i] < 0 and nums[i+1] > 0):
                piv = i + 1
                break
    
        i = 0
        while (i < piv):
            cur = nums[i]
            j = piv
            while (j < len(nums)):
                sum2 = nums[i] + nums[j]
                if (sum2 < 0):
                    sum2 = -sum2
                    if (sum2 < nums[j] or sum2 > nums[-1]):
                        j += 1
                    elif (self.find(sum2, nums[j+1:]) != -1):
                        sum3.append([nums[i], nums[j], sum2])
                        j += 1
                    else:
                        j += 1
                elif (sum2 > 0):
                    sum2 = -sum2
                    if (sum2 < nums[i + 1] or sum2 > nums[piv - 1]):
                        j += 1
                    elif (self.find(sum2, nums[i+1:piv]) != -1):
                        sum3.append([nums[i], nums[j], sum2])
                        j += 1
                    else:
                        j += 1
                else:
                    j += 1
                while(j < len(nums) and nums[j] == nums[j-1]):
                    j += 1
                # else:
                #     if (nums[piv] == 0):
                #         sum3.append([nums[i], nums[j], 0])
                #         j += 1
                #     else:
                #         j += 1
            i += 1
            while (i < piv and nums[i] == nums[i-1]):
                i += 1

        if (nums[piv:piv+3] == [0,0,0]):
            sum3.append([0,0,0])
        return sum3

sol = Solution()
print(sol.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))