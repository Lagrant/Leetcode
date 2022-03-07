# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.global_len = 0
        self._max_layer = 0
        self.dep_node = None

    def diameterOfBinaryTree(self, root) -> int:
        root.prev = None
        root.visited = False
        self.max_layer(root, 0)

        self.dep_node.visited = True
        self.dfs(self.dep_node, 0)

        return self.global_len - 1

    def max_layer(self, node, layer):
        layer += 1
        # llayer = rlayer = 0
        # lnode = rnode = None
        if (layer > self._max_layer):
            self._max_layer = layer
            self.dep_node = node

        if (node.left is not None):
            node.left.prev = node
            node.left.visited = False
            self.max_layer(node.left, layer)
        if (node.right is not None):
            node.right.prev = node
            node.right.visited = False
            self.max_layer(node.right, layer) 
    
    def dfs(self, node, diam):
        if (node is None):
            return
        
        diam += 1
        self.global_len = diam if (diam > self.global_len) else self.global_len

        if (node.left is not None):
            if (not hasattr(node.left, 'visited')):
                node.left.visited = True
                node.left.prev = node
                self.dfs(node.left, diam)
            elif (node.left.visited == False):
                node.left.visited = True
                self.dfs(node.left, diam)
        
        if (node.right is not None):
            if (not hasattr(node.right, 'visited')):
                node.right.visited = True
                node.right.prev = node
                self.dfs(node.right, diam)
            elif (node.right.visited == False):
                node.right.visited = True
                self.dfs(node.right, diam)
        
        if (node.prev is not None and node.prev.visited == False):
            node.prev.visited = True
            self.dfs(node.prev, diam)

root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)

sol = Solution()
print(sol.diameterOfBinaryTree(root))