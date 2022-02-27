class Solution:
    def findMissingRanges(self, nums, lower: int, upper: int):
        if (len(nums) == 0):
            return [str(lower)] if (lower == upper) else [f"{lower}->{upper}"]
            
        nums.sort()

        m_ranges = []
        num_ranges = []
        for i in range(len(nums) - 1):
            if (nums[i+1] - nums[i] >= 3):
                num_ranges.append([nums[i] + 1, nums[i+1] - 1])
            elif (nums[i+1] - nums[i] == 2):
                num_ranges.append([nums[i] + 1])
        
        if (nums[0] > lower and nums[0] <= upper):
            m_ = f"{lower}->{nums[0]-1}" if (lower != nums[0] - 1) else str(lower)
            m_ranges.append(m_)

        for nr in num_ranges:
            if (len(nr) == 1):
                if (nr[0] > lower and nr[0] < upper):
                    m_ranges.append(str(nr[0]))
            elif (nr[0] >= upper or nr[1] <= lower):
                continue
            elif (nr[0] < lower and nr[1] > upper):
                return [f"{lower}->{upper}"]
            elif (nr[0] < lower and nr[1] < upper):
                m_ranges.append(f"{lower}->{nr[1]}")
            elif (nr[0] > lower and nr[1] > upper):
                m_ranges.append(f"{nr[0]}->{upper}")
            else:
                m_ranges.append(f"{nr[0]}->{nr[1]}")
        
        if (nums[-1] < upper and nums[-1] >= lower):
            m_ = f"{nums[-1]+1}->{upper}" if (upper != nums[-1] + 1) else str(upper)
            m_ranges.append(m_)

        return m_ranges

sol = Solution()
print(sol.findMissingRanges([-1], -1, -1))