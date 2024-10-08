from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        lst = self.traverse(root)
        for i in range(len(lst) - 1):
            if lst[i] >= lst[i + 1]:
                return False
        return True

    def traverse(self, root):
        if root.left is None and root.right is None:
            return [root.val]
        
        lst = []
        if root.left is not None:
            ll = self.traverse(root.left)
            lst.extend(ll)
        lst.append(root.val)
        if root.right is not None:
            rl = self.traverse(root.right)
            lst.extend(rl)
        return lst
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        def dfs(left_bound, right_bound, curr):
            if not curr:
                return True
            if not (left_bound < curr.val < right_bound):
                return False
            return dfs(left_bound, curr.val, curr.left) and dfs(curr.val, right_bound, curr.right)
        return dfs(float("-inf"), float("inf"), root)
    def traverse2(self, root, base1, base2):
        if root.left is None and root.right is None:
            if base1 is not None:
                if base1 >= root.val:
                    return False
            if base2 is not None:
                if base2 <= root.val:
                    return False
            return True
        
        if root.left is not None:
            if root.val <= root.left.val:
                return False
            lflag = self.traverse2(root.left, base1, root.val)
            if not lflag:
                return False
        
        if root.right is not None:
            if root.val >= root.right.val:
                return False
            rl = self.traverse2(root.right, root.val, None)
            if not rl:
                return False
        return True
    
if __name__ == '__main__':
    rt = TreeNode(32, TreeNode(26, TreeNode(19, right=TreeNode(27))), right= TreeNode(47, right= TreeNode(56)))
    s = Solution()
    print(s.isValidBST(rt))