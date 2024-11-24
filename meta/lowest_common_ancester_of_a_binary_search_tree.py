# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self) -> None:
        self.visitp = {}
        self.visitq = {}
        # self.findq, self.findp = False, False
        self.p = None
        self.q = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        return self.dfs(root)[2]
    
    def dfs(self, node):
        findq, findp = False, False
        if node.val == self.p.val:
            findp = True
        if node.val == self.q.val:
            findq = True
        if findp and findq:
            return True, True, node
        
        pl, ql, pr, qr = False, False, False, False
        if node.left is not None:
            pl, ql, nodel = self.dfs(node.left)
            if pl and ql:
                return True, True, nodel
        if node.right is not None:
            pr, qr, noder = self.dfs(node.right)
            if pr and qr:
                return True, True, noder
        rtl = pl or pr or findp
        rtr = ql or qr or findq
        return rtl, rtr, node if rtl and rtr else None