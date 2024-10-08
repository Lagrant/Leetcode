# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self) -> None:
        self.qstr = None
        self.pstr = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.left is None and root.right is None:
            return root
        self.treematch(root, p, q, '')
        i = 0
        anc = None
        while i < len(self.pstr) and i < len(self.qstr):
            if self.pstr[i] == self.qstr[i]:
                i += 1
            else:
                if i == 0:
                    return root
                anc = self.pstr[:i]
                break
        if anc is None:
            anc = self.pstr if len(self.pstr) < len(self.qstr) else self.qstr
        anc_node = root
        for a in anc:
            if a == '0':
                anc_node = anc_node.right
            else:
                anc_node = anc_node.left
        return anc_node

    def treematch(self, root, p, q, matchstr):
        if root.val == p.val:
            self.pstr = matchstr
        elif root.val == q.val:
            self.qstr = matchstr
        if self.qstr is not None and self.pstr is not None:
            return
        if root.left is not None:
            self.treematch(root.left, p, q, matchstr + '1')
        if root.right is not None:
            self.treematch(root.right, p, q, matchstr + '0')

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None

# if __name__ == '__main__':
#     root = TreeNode(-1)
#     root.left = TreeNode(0)
#     # root.right = TreeNode(-48)
#     lr = root.left
#     lr.left = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))
#     # lr.right = TreeNode(-100)
#     # lr.right.left = TreeNode(7)
#     # lr.right.right = TreeNode(4)
#     # rr = root.right
#     # rr.left = TreeNode(-101)
#     # rr.right = TreeNode(48)
#     # rr.right.left = TreeNode(-71)
#     s = Solution()
#     print(s.lowestCommonAncestor(root, TreeNode(2), TreeNode(3)).val)