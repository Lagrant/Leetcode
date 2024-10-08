from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.targetSum = 0

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        self.targetSum = targetSum

        return self.pathsum(root, 0)

    def pathsum(self, root, cumsum):
        if root is None:
            return cumsum == self.targetSum
        if root.left is None and root.right is None:
            return root.val + cumsum == self.targetSum
        
        if root.left is not None:
            lflag = self.pathsum(root.left, cumsum + root.val)
            if lflag:
                return True
        if root.right is not None:
            rflag = self.pathsum(root.right, cumsum + root.val)
            if rflag:
                return True
        return False