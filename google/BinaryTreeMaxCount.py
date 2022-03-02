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
        node = root
        max_l = max_r = -float('inf')
        if (node.left is not None):
            max_l = self.subPathSum(node.left)
        if (node.right is not None):
            max_r = self.subPathSum(node.right)
        
        local_max = max(node.val, node.val + max_l, node.val + max_r)
        self.output = max(local_max, self.output, node.val + max_l + max_r)
        
        return local_max

    def maxPathSum(self, root):

        self.subPathSum(root)
        return self.output

root = TreeNode(-3)
sol = Solution()
print(sol.maxPathSum(root))