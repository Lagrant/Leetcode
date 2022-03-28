# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isLeaf(self, node):
        return not node.left and not node.right
    def hasChildren(self, node):
        return 2 if node.left and node.right else 1 if node.left or node.right else 0

    def findLeaves(self, root):
        if (self.isLeaf(root)):
            return [[root.val]]
        leaves = []
        leaf_nodes = []
        ans = []
        root.parent = None
        nodes = deque([root])
        while (len(nodes) > 0):
            cur = nodes.popleft()
            if (self.isLeaf(cur)):
                leaves.append(cur.val)
                leaf_nodes.append(cur)
                continue
            if cur.left:
                cur.left.parent = cur
                nodes.append(cur.left)
            if cur.right:
                cur.right.parent = cur
                nodes.append(cur.right)
        ans.append(leaves)

        while leaf_nodes[0] and leaf_nodes[0].parent:
            upper_leaves = []
            upper_leaf_nodes = []
            for leaf in leaf_nodes:
                if leaf.parent.left == leaf:
                    leaf.parent.left = None
                else:
                    leaf.parent.right = None
                if (self.hasChildren(leaf.parent) == 1):
                    continue
                
                upper_leaves.append(leaf.parent.val)
                upper_leaf_nodes.append(leaf.parent)
            ans.append(upper_leaves)
            leaf_nodes = upper_leaf_nodes

        return ans


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

sol = Solution()
print(sol.findLeaves(root))
