from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]
        
        layer1, layer2, res = [root], [], [[root.val]]
        direc = -1
        while len(layer1) > 0:
            for l in layer1:
                if l.left is not None:
                    layer2.append(l.left)
                if l.right is not None:
                    layer2.append(l.right)
            if len(layer2) > 0:
                res.append([l2.val for l2 in layer2][::direc])
            direc *= -1
            layer1, layer2 = layer2, []
        return res