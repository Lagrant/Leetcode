# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.output = -float('inf')
    
    def subPathSum(self, root) -> int:
        if root.left is None and root.right is None:
            self.output = max(self.output, root.val)
            return root.val
        
        lsum, rsum, localsum = -float('inf'), -float('inf'), -float('inf')
        if root.left is not None:
            lsum = self.subPathSum(root.left)
        if root.right is not None:
            rsum = self.subPathSum(root.right)
        localsum = max(root.val, root.val + lsum, root.val + rsum)
        self.output = max(localsum, self.output, root.val + lsum + rsum)
        return localsum
    
    def maxPathSum(self, root):
        self.subPathSum(root)
        return self.output