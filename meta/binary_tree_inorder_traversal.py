from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        if root is None:
            return []
        if root.left:
            vals.extend(self.inorderTraversal(root.left))
        vals.append(root.val)
        if root.right:
            vals.extend(self.inorderTraversal(root.right))
        return vals