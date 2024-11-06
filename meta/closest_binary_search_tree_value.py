from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.close = None

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not self.close or abs(target - root.val) < self.close[0] or abs(target - root.val) == self.close[0] and root.val < self.close[1]:
            self.close = [abs(target - root.val), root.val]
        if root.val > target:
            if root.left is not None:
                self.closestValue(root.left, target)
            else:
                return self.close[1]
        elif root.val == target:
            return self.close[1]
        else:
            if root.right is not None:
                self.closestValue(root.right, target)
            else:
                return self.close[1]
        return self.close[1]