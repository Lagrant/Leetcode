from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return root.val
        return self.tsum(root, 0)
    def tsum(self, root, cumsum) -> int:
        if root.left is None and root.right is None:
            return root.val + cumsum * 10
        cumsum = cumsum * 10 + root.val
        rtsum = 0
        if root.left is not None:
            lsum = self.tsum(root.left, cumsum)
            rtsum += lsum
        if root.right is not None:
            rsum = self.tsum(root.right, cumsum)
            rtsum += rsum
        return rtsum