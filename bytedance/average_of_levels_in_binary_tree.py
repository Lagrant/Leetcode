from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root.left is None and root.right is None:
            return [root.val]
        
        avg, layer1, layer2 = [root.val], [root], []
        while len(layer1) > 0:
            for l in layer1:
                if l.left is not None:
                    layer2.append(l.left)
                if l.right is not None:
                    layer2.append(l.right)
            if len(layer2) > 0:
                avg.append(sum([l2.val for l2 in layer2]) / len(layer2))
            layer1, layer2 = layer2, []
        return avg