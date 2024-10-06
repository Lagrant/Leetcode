from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pnon = p is None
        qnon = q is None
        if pnon ^ qnon:
            return False
        if pnon:
            return True
        if not pnon and p.val != q.val:
            return False
        plnon = p.left is None
        prnon = p.right is None
        qlnon = q.left is None
        qrnon = q.right is None
        lnon = plnon ^ qlnon
        rnon = prnon ^ qrnon
        if lnon or rnon:
            return False
        if not plnon:
            leftflag = self.isSameTree(p.left, q.left)
            if not leftflag:
                return False
        if not prnon:
            rightflag = self.isSameTree(p.right, q.right)
            if not rightflag:
                return False
        return True