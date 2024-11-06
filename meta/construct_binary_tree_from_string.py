from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if len(s) == 0:
            return None
        
        s = deque(list(s))
        val = self.find_integer(s)
        root = TreeNode(val)
        nodestack = [root]
        while len(s) > 0:
            if s[0] == '(':
                s.popleft()
                val = self.find_integer(s)
                newnode = TreeNode(val)
                if nodestack[-1].left is None:
                    nodestack[-1].left = newnode
                else:
                    nodestack[-1].right = newnode
                nodestack.append(newnode)
            if s[0] == ')':
                s.popleft()
                nodestack.pop()
        return root

    def find_integer(self, s):
        i = ''
        while len(s) > 0 and s[0] != '(' and s[0] != ')':
            i += s[0]
            s.popleft()
            if len(s) > 0 and s[0] == '-':
                break
        return int(i)
    
if __name__ == '__main__':
    s = Solution()
    print(s.str2tree("4(2(3)(1))(6(5))"))