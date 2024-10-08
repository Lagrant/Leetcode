from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return [root.val]
        layer1 = [root]
        layer2 = []
        view = [root.val]
        while layer1 is not None and len(layer1) > 0:
            for l1 in layer1:
                if l1.left is not None:
                    layer2.append(l1.left)
                if l1.right is not None:
                    layer2.append(l1.right)
            if len(layer2) > 0:
                view.append(layer2[-1].val)
            layer1, layer2 = layer2, []
        return view
    
    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(root, level):
            if root is None:
                return
            if len(result) < level:
                result.append(root.val)
            dfs(root.right, level+1)
            dfs(root.left, level+1)
            
        dfs(root, 1)
        return result