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

if __name__ == '__main__':
    root = TreeNode(3)
    node1 = TreeNode(5)
    node2 = TreeNode(1)
    node3 = TreeNode(6)
    node4 = TreeNode(2)
    node5 = TreeNode(7)
    node6 = TreeNode(4)
    node7 = TreeNode(0)
    node8 = TreeNode(8)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node4.left = node5
    node4.right = node6
    node2.left = node7
    node2.right = node8
    s = Solution()
    print(s.lowestCommonAncestor(root, node1, node2))