# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self) -> None:
        self.case_map = {
            110: self.case1,
            101: self.case2,
            1001: self.case3,
            1010: self.case4
        }
    def flipEquiv(self, root1, root2) -> bool:
        if (root1 == root2 == None):
            return True
        elif (root1 is None or root2 is None):
            return False
        
        if (root1.val != root2.val):
            return False
        
        return self.comp(root1, root2)

    def case1(self, root1, root2):
        if (root1.right.val == root2.left.val):
            # root2.left, root2.right = root2.right, root2.left
            return self.comp(root1.right, root2.left)
        else:
            return False
    def case2(self, root1, root2):
        if (root1.right.val == root2.right.val):
            return self.comp(root1.right, root2.right)
        else:
            return False
    def case3(self, root1, root2):
        if (root1.left.val == root2.right.val):
            # root2.left, root2.right = root2.right, root2.left
            return self.comp(root1.left, root2.right)
        else:
            return False
    def case4(self, root1, root2):
        if (root1.left.val == root2.left.val):
            return self.comp(root1.left, root2.left)
        else:
            return False

    def comp(self, root1, root2) -> bool:

        sub1, sub2 = 0, 0
        sub = 1111
        if (root1.left != None):
            sub1 += 1
        else:
            sub -= 1000
        if (root1.right != None):
            sub1 += 1
        else:
            sub -= 100
        if (root2.left != None):
            sub2 += 1
        else:
            sub -= 10
        if (root2.right != None):
            sub2 += 1
        else:
            sub -= 1
        if (sub1 == sub2 == 0):
            return True
        elif (sub1 != sub2):
            return False
        
        if (sub1 + sub2 < 4):
            return self.case_map[sub](root1, root2)

        if (root1.left.val == root2.right.val and root1.right.val == root2.left.val):
            # root2.left, root2.right = root2.right, root2.left
            r1 = self.comp(root1.left, root2.right)
            r2 = self.comp(root1.right, root2.left)
            return r1 and r2
        elif (root1.left.val == root2.left.val and root1.right.val == root2.right.val):
            r1 = self.comp(root1.left, root2.left)
            r2 = self.comp(root1.right, root2.right)
            return r1 and r2
        else:
            return False


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1, root2) -> bool:
        if root1 is root2:
            return True
        
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        return ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) 
                or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)))
        
root1 = TreeNode(0)
root1.left = TreeNode(1)
root2 = TreeNode(0)
root2.left = TreeNode(1)
sol = Solution()
print(sol.flipEquiv(root1, root2))