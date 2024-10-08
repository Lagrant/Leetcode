from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.k = None
        self.kth = None
        self.cnt = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root.left is None and root.right is None:
            return root.val
        self.k = k
        self.traverse3(root)
        return self.kth   
    
    def traverse(self, root):
        if root.left is None and root.right is None:
            return [root.val]
        
        t = []
        if root.left is not None:
            t0 = self.traverse(root.left)
            t.extend(t0)
        t.append(root.val)
        if root.right is not None:
            t0 = self.traverse(root.right)
            t.extend(t0)
        return t
    
    def traverse3(self, root):
        if root.left is None and root.right is None:
            self.cnt += 1
            if self.cnt == self.k:
                self.kth = root.val
            return
        
        if root.left is not None:
            self.traverse3(root.left)
        if self.cnt == self.k:
            return
        
        self.cnt += 1
        if self.cnt == self.k:
            self.kth = root.val
            return
         
        if root.right is not None:
            self.traverse3(root.right)
        return

if __name__ == '__main__':
    rt = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    s = Solution()
    print(s.kthSmallest(rt, 3))