from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# GENERATOR
def traverse(root):
    if not root:
        return 
    
    yield from traverse(root.left)
    yield root.val
    yield from traverse(root.right)


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        dif = float("inf")
        
        # make a gen
        seq = traverse(root)

        # take first elem
        prev = next(seq)
        
        # take others and find min
        for cur in seq:
            dif = min(cur-prev, dif)
            prev = cur

        return dif
            
if __name__ == '__main__':
    # rt = TreeNode(1476, TreeNode(1054, TreeNode(1, right=TreeNode(215, right=TreeNode(745)))))
    rt = TreeNode(236, TreeNode(104, right=TreeNode(227)), TreeNode(701, right=TreeNode(911)))
    s = Solution()
    print(s.getMinimumDifference(rt))