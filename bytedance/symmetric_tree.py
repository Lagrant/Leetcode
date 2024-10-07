from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        if root.left is None and root.right is not None or root.left is not None and root.right is None:
            return False
        if root.left.val != root.right.val:
            return False
        
        return self.checkSymmetric(root.left, root.right)
    
    def checkSymmetric(self, node1, node2):
        if node1.val != node2.val:
            return False
        
        n1l, n1r = node1.left is None, node1.right is None
        n2l, n2r = node2.left is None, node2.right is None
        if n1l ^ n2r or n1r ^ n2l:
            return False
        if all([n1l, n1r, n2l, n2r]):
            return True
        
        if not n1l and not n1r:
            if not (node1.left.val == node2.right.val and node1.right.val == node2.left.val):
                return False
        
        s1, s2 = True, True
        if node1.left is not None:
            s1 = self.checkSymmetric(node1.left, node2.right)
        if node1.right is not None:
            s2 = self.checkSymmetric(node1.right, node2.left)
        return s1 and s2
    
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    # root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(3)
    # root.right.right = TreeNode(3)
    print(s.isSymmetric(root))