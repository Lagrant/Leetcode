from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.cur = root
        self.stack = [root]

    def next(self) -> int:
        while self.cur.left is not None:
            self.stack.append(self.cur.left)
            self.cur = self.cur.left
        if self.cur.right is not None:
            if self.stack[-1] == self.cur:
                self.stack.pop()
                if len(self.stack) > 0 and self.stack[-1].left == self.cur:
                    self.stack[-1].left = None
                elif len(self.stack) > 0 and self.stack[-1].right == self.cur:
                    self.stack[-1].right = None
            self.stack.append(self.cur.right)
            rtval = self.cur.val
            self.cur = self.cur.right
        else:
            rtval = self.cur.val
            self.stack.pop()
            if len(self.stack) > 0:
                if self.stack[-1].left == self.cur:
                    self.stack[-1].left = None
                elif self.stack[-1].right == self.cur:
                    self.stack[-1].right = None
                self.cur = self.stack[-1]
        return rtval

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()