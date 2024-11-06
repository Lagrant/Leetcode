from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.targetSum = None
        self.res = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        self.targetSum = targetSum
        self.dfs(root, [], 0)
        return self.res

    def dfs(self, node, path, subpsum):
        subpsum += node.val
        path.append(node.val)
        if node.left is None and node.right is None:
            if subpsum == self.targetSum:
                self.res.append(path.copy())
        
        if node.left is not None:
            self.dfs(node.left, path, subpsum)
        if node.right is not None:
            self.dfs(node.right, path, subpsum)
        path.pop()
        