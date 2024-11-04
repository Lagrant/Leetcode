from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.ptr = None
        self.val = float('inf')

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        head, tail = self.traverse(root)
        head.left = tail
        tail.right = head
        return self.ptr

    def traverse(self, node):
        headl, taill, headr, tailr = None, None, None, None
        if node.val < self.val:
            self.val = node.val
            self.ptr = node
        if node.left is None and node.right is None:
            return node, node
        if node.left is not None:
            headl, taill = self.traverse(node.left)
            taill.right = node
            node.left = taill
        if node.right is not None:
            headr, tailr = self.traverse(node.right)
            node.right = headr
            headr.left = node
        
        return headl if headl is not None else node, tailr if tailr is not None else node