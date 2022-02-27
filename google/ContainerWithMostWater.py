class Solution:
    """
    The key idea is to realize that given inital size, the only way
    to potientially improve it is to replace the shorter line with a 
    longer one on its side. So find a longer line on the shorter side 
    over and over again until the left side and the right side come 
    together.
    """
    def maxArea(self, height) -> int:
        start = 0
        end = len(height) - 1
        max_area = min(height[start], height[end]) * (len(height) - 1)
        while (start < end):
            if (height[start] < height[end]):
                start1 = start + 1
                while (start1 < end and height[start1] <= height[start]):
                    start1 += 1
                start = start1
                cur_area = (end - start) * min(height[start], height[end])
                
            else:
                end1 = end - 1
                while (start < end1 and height[end1] <= height[end]):
                    end1 -= 1
                end = end1
                cur_area = (end - start) * min(height[start], height[end])
            
            if (cur_area > max_area):
                max_area = cur_area
        return max_area

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))