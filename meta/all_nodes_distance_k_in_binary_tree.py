from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        return self.search_target(root, target, k)[0]

    def search_target(self, node, target, k):
        if node.val == target.val:
            res_down = self.search_k_down(node, k, 0)
            return res_down, 0
        
        resl = []
        resr = []
        distl, distr = -1, -1
        if node.left is not None:
            resl, distl = self.search_target(node.left, target, k)
        if node.right is not None:
            resr, distr = self.search_target(node.right, target, k)
        
        if distl != -1:
            if distl + 1 == k:
                resl.append(node.val)
                return resl, distl + 1
            if distl + 1 > k:
                return resl, distl + 1
            resl.extend(self.search_k_down(node.right, k, distl + 2))
            return resl, distl + 1
        if distr != -1:
            if distr + 1 == k:
                resr.append(node.val)
                return resr, distr + 1
            if distr + 1 > k:
                return resr, distr + 1
            resr.extend(self.search_k_down(node.left, k, distr + 2))
            return resr, distr + 1
        return [], -1

    def search_k_down(self, node, k, dist):
        if node is None:
            return []
        if dist == k:
            return [node.val]
        res = []
        if node.left is not None:
            res.extend(self.search_k_down(node.left, k, dist + 1))
        if node.right is not None:
            res.extend(self.search_k_down(node.right, k, dist + 1))
        return res

if __name__ == '__main__':
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    node3 = TreeNode(2)
    root.left = node1
    node1.left = node2
    node1.right = node3
    s = Solution()
    print(s.distanceK(root, node3, 1))
