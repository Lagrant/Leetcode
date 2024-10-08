# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.num = 0

    def traverse_branch(self, root, lside):
        level = 1
        if (lside):
            while (root.left is not None):
                root = root.left
                level += 1
        else:
            while (root.right is not None):
                root = root.right
                level += 1
        return level
    
    def countNodes(self, root) -> int:
        if (root is None):
            return self.num
        
        llevel = self.traverse_branch(root, True)
        rlevel = self.traverse_branch(root, False)
        if (llevel == rlevel):
            return 2**llevel - 1
        
        self.num += 1
        self.subNodes(root, llevel, rlevel)

        # self.num += 2**rlevel - 1
        return self.num

    def subNodes(self, root, llevel, rlevel):
        if (root.left is None):
            return
        if (root.right is None):
            self.num += 1
            return
        
        rlevel1 = self.traverse_branch(root.left, False)
        if (rlevel1 + 1 == llevel):
            self.num += 2**rlevel1
            self.subNodes(root.right, self.traverse_branch(root.right, True), rlevel - 1)
        else:
            self.num += 2**(rlevel - 1)
            self.subNodes(root.left, llevel - 1, self.traverse_branch(root.left, False))

        return
