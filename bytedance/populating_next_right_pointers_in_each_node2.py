# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None or root.left is None and root.right is None:
            return root
        layer1, layer2 = [root], []
        while layer1 is not None and len(layer1) > 0:
            for cur in layer1:
                if cur.left is not None:
                    layer2.append(cur.left)
                if cur.right is not None:
                    layer2.append(cur.right)
            for i in range(len(layer2) - 1):
                layer2[i].next = layer2[i + 1]
            layer1 = layer2
            layer2 = []
        return root
