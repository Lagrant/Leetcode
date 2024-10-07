from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        if len(preorder) == 0:
            return None
        piv = inorder.index(preorder[0])
        root = TreeNode(inorder[piv])
        leftchild = self.buildTree(preorder=preorder[1: 1 + piv], inorder=inorder[:piv])
        rightchild = self.buildTree(preorder=preorder[1 + piv:], inorder=inorder[piv + 1:])
        root.left = leftchild
        root.right = rightchild
        return root
    
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    # root.left.left = TreeNode(3)
    # root.right.right = TreeNode(7)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(3)
    print(s.buildTree([1, 2,3], [2, 3, 1]))