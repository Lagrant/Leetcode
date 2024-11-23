from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        miss_child = False
        que = deque([[root]])
        layer_idx = -1
        while len(que) > 0:
            cur_layer = que.popleft()
            layer_idx += 1
            cur_layer_size = len(cur_layer)
            next_layer = deque()
            for cl in cur_layer:
                if cl.left is not None:
                    if miss_child:
                        return False
                    next_layer.append(cl.left)
                else:
                    miss_child = True
                if cl.right is not None:
                    if miss_child:
                        return False
                    next_layer.append(cl.right)
                else:
                    miss_child = True
            if cur_layer_size != 2 ** layer_idx and len(next_layer) > 0:
                return False
            if len(next_layer) > 0:
                que.append(next_layer)
        return True