from typing import Optional
from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or root.left is None and root.right is None:
            return root
        layer = [root]
        n_layer = []
        while len(layer) > 0:
            for i in range(len(layer) - 1):
                layer[i].next = layer[i + 1]
                if layer[i].left is not None:
                    n_layer.append(layer[i].left)
                    n_layer.append(layer[i].right)
            if layer[-1].left is not None:
                n_layer.append(layer[-1].left)
                n_layer.append(layer[-1].right)
            layer = n_layer
            n_layer = []
        return root
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        L, R, N = root.left, root.right, root.next
        if L:
            L.next = R
            if N: R.next = N.left
            self.connect(L)
            self.connect(R)
        return root