from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        vcoors = self.traversal(root, [0, 0])
        vcoors.sort(key=lambda x: x[1][0])
        sz = vcoors[-1][1][0] - vcoors[0][1][0] + 1
        rt = [[] for _ in range(sz)]
        cnt = 0
        for i in range(len(vcoors) - 1):
            rt[cnt].append([vcoors[i][0], vcoors[i][1][1]])
            if vcoors[i][1][0] != vcoors[i + 1][1][0]:
                cnt += 1
                rt[cnt - 1].sort(key=lambda x: x[1])
                rt[cnt - 1] = [r[0] for r in rt[cnt - 1]]
        rt[cnt].append([vcoors[-1][0], vcoors[-1][1][1]])
        rt[cnt].sort(key=lambda x: x[1])
        rt[cnt] = [r[0] for r in rt[cnt]]
        return rt
    def traversal(self, node, coor):
        if node is None:
            return []
        ncoor = [[node.val, coor]]
        if node.left is not None:
            nl = self.traversal(node.left, [coor[0] - 1, coor[1] + 1])
            ncoor.extend(nl)
        if node.right is not None:
            nr = self.traversal(node.right, [coor[0] + 1, coor[1] + 1])
            ncoor.extend(nr)
        return ncoor