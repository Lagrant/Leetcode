from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        lbound = self.find_left_boundary(root)
        leaves = self.find_leaves(root)
        rbound = self.find_right_boundary(root)[::-1]
        return lbound + leaves + rbound[:-1]

    def find_left_boundary(self, root):
        if root.left is None:
            return [root.val]
        if root.left and not root.left.left and not root.left.right:
            return [root.val, root.left.val]

        def left_boundary(node):
            if node.left is None and node.right is None:
                return []
            lbound = [node.val]
            if node.left is not None:
                lbound.extend(left_boundary(node.left))
            elif node.right is not None:
                lbound.extend(left_boundary(node.right))
            return lbound
        return left_boundary(root)
    
    def find_right_boundary(self, root):
        if root.right is None:
            return [root.val]
        
        def right_boundary(node):
            if node.right is None and node.left is None:
                return []
            rbound = [node.val]
            if node.right is not None:
                rbound.extend(right_boundary(node.right))
            elif node.left is not None:
                rbound.extend(right_boundary(node.left))
            return rbound
        return right_boundary(root)
    
    def find_leaves(self, root):
        leaves = []
        if not root.left and not root.right:
            return leaves
        def dfs(node):
            if not node:
                return
            if node.left is None and node.right is None:
                leaves.append(node.val)
                return
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        if root.left and not root.left.left and not root.left.right:
            dfs(root.right)
        else:
            dfs(root)
        return leaves

if __name__ == '__main__':
    root = TreeNode(1, left=TreeNode(2))
    s = Solution()
    print(s.boundaryOfBinaryTree(root))