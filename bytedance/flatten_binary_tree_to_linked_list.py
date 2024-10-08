from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.f(root)
        return root

    def f(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None or root.left is None and root.right is None:
            return root
        
        leftend, rigthend = None, None
        if root.left is not None:
            leftend = self.f(root.left)
        if root.right is not None:
            rigthend = self.f(root.right)
        if leftend is not None:
            leftend.right = root.right
            root.right, root.left = root.left, None
        if rigthend is None:
            rigthend = leftend
        return rigthend

# if __name__ == '__main':
#     s = Solution()
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(5)
#     root.left.left = TreeNode(3)
#     root.left.right = TreeNode(4)
#     # root.left.left = TreeNode(3)
#     # root.right.right = TreeNode(7)
#     # root.right.left = TreeNode(15)
#     root.right.right = TreeNode(6)
#     print(s.flatten(root))