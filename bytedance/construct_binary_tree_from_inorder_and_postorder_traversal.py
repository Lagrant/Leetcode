from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.pos = {}
        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        for i, n in enumerate(inorder):
            self.pos[n] = i
        
        root = self.build(inorder, postorder, 0)
        return root
        
    def build(self, inorder: List[int], postorder: List[int], piv0: int) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        piv = self.pos[postorder[-1]] - piv0
        root = TreeNode(postorder[-1])
        leftchild = self.build(inorder[:piv], postorder[:piv], piv0)
        rightchild = self.build(inorder[piv + 1:], postorder[piv:-1], self.pos[postorder[-1]] + 1)
        root.left = leftchild
        root.right = rightchild
        return root