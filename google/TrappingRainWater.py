class Solution:
    """
    This problem should start from the shorter side to the higher side, 
    go step by step.
    For each step, it should compare current height and the previous height, 
    take the biggest value and minus the current height.
    """
    def trap(self, height) -> int:
        if (len(height) == 1):
            return 0
        s = 1
        while (s < len(height) and height[s] >= height[s - 1]):
            s += 1
        if (s >= len(height) - 1):
            return 0

        contain = 0
        sheight = [{'height':height[s - 1], 'rdiff': height[s - 1], 'idx':s-1}]
        for i in range(s, len(height)):

            if (height[i] < sheight[-1]['height']):
                sheight.append({'height': height[i], 'rdiff': height[i], 'idx': i})
                if (len(sheight) >= 2):
                    sheight[-2]['rdiff'] = sheight[-2]['height'] - sheight[-1]['height']
            
            else:
                ldiff = height[i]
                while (len(sheight) > 0 and height[i] >= sheight[-1]['height']):
                    contain += sheight[-1]['rdiff'] * (i - sheight[-1]['idx'] - 1)
                    ldiff -= sheight[-1]['rdiff']
                    sheight.pop()

                if (len(sheight) > 0 and ldiff > 0):
                    contain += ldiff * (i - sheight[-1]['idx'] - 1)
                    sheight[-1]['rdiff'] = sheight[-1]['height'] - height[i]
                
                sheight.append({'height': height[i], 'rdiff': height[i], 'idx': i})
            
        return contain
       
sol = Solution()
print(sol.trap([2,0,2]))