class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if len(s) == 1:
            return s == goal
        if s == goal:
            return True
        
        for i in range(1, len(goal)):
            if goal[i:] == s[:-i] and goal[:i] == s[-i:]:
                return True
        return False