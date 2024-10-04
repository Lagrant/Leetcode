from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        wstack = []
        water = 0
        for h in height:
            if len(stack) == 0 or h <= stack[-1]:
                stack.append(h)
                wstack.append(1)
                continue
            width = 1
            while len(stack) > 0 and h > stack[-1]:
                water += (h - stack[-1]) * wstack[-1]
                back_h = stack.pop()
                width += wstack.pop()
            if len(stack) == 0:
                water -= (h - back_h) * (width - 1)
            stack.append(h)
            wstack.append(width)
        return water

if __name__ == '__main__':
    s = Solution()
    res = s.trap([4,2,0,3,2,5])
    print(res)