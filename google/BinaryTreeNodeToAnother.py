# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(self, root, startValue: int, destValue: int) -> str:
        def dfs(cur, start_path, dest_path):

            if not cur or start_path[-1] == '$' and dest_path[-1] == '$':
                return start_path, dest_path
            if cur.val == startValue:
                start_path.append('$')
            elif cur.val == destValue:
                dest_path.append('$')

            s_len, d_len = len(start_path), len(dest_path)

            if start_path[-1] != '$':
                start_path.append('L')
            if dest_path[-1] != '$':
                dest_path.append('L')
            start_path, dest_path = dfs(cur.left, start_path, dest_path)
        
            if start_path[-1] == '$' and dest_path[-1] == '$':
                return start_path, dest_path
            
            if (start_path[-1] != '$'):
                start_path = start_path[:s_len]
                start_path.append('R')
            if (dest_path[-1] != '$'):
                dest_path = dest_path[:d_len]
                dest_path.append('R')
            return dfs(cur.right, start_path, dest_path)
            
        start_path = ['#']
        dest_path = ['#']
        start_path, dest_path = dfs(root, start_path, dest_path)
        start_path, dest_path = start_path[1:-1], dest_path[1:-1]
        if (len(start_path) == 0):
            return ''.join(dest_path)
        if (len(dest_path) == 0):
            return 'U' * len(start_path)

        common_root = 0
        while common_root < len(start_path) and common_root < len(dest_path):
            if start_path[common_root] != dest_path[common_root]:
                break
            common_root += 1

        if common_root == 0 and len(start_path) == 1:
            return 'U' + ''.join(dest_path)
        if common_root == 0 and len(dest_path) == 1:
            return 'U' * len(start_path) + ''.join(dest_path)
        if common_root == len(start_path) and len(dest_path) > len(start_path):
            return ''.join(dest_path[common_root:])
        if common_root == len(dest_path) and len(start_path) > len(dest_path):
            return 'U' * (len(start_path) - common_root)
        return 'U' * (len(start_path) - common_root) + ''.join(dest_path[common_root:])

root = TreeNode(5, TreeNode(8), TreeNode(3, TreeNode(4), TreeNode(7)))
left = root.left
left.left = TreeNode(1)
left.left.left = TreeNode(6, None, TreeNode(2))
right = root.right
 
sol = Solution()
print(sol.getDirections(root, 4, 3))

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def recurse(node, val):
            if node is None:
                return None
            if node.val == val:
                return ''
            p0 = recurse(node.left, val)
            p1 = recurse(node.right, val)
            if p0 is not None:
                return 'L' + p0
            elif p1 is not None:
                return 'R' + p1
            else:
                return None
        p0 = recurse(root, startValue)
        p1 = recurse(root, destValue)
        
        prefix = 0
        while prefix < len(p0) and prefix < len(p1) and p0[prefix] == p1[prefix]:
            prefix += 1
        
        return (len(p0) - prefix) * 'U'+ p1[prefix:]