from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        que = deque([root])
        cum = 0
        while len(que) > 0:
            node = que.popleft()
            if low <= node.val <= high:
                cum += node.val
            if node.left is not None and low <= node.val:
                que.append(node.left)
            if node.right is not None and high >= node.val:
                que.append(node.right)
        return cum