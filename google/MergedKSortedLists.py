# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        s = []
        for ls in lists:
            while (ls is not None):
                s.append(ls.val)
                ls = ls.next
        s.sort()

        if (len(s) == 0):
            return None
        
        head = sNode = ListNode(s[0])
        for i in range(1, len(s)):
            sNode.next = ListNode(s[i])
            sNode = sNode.next
        
        return head

sol = Solution()
print(sol.mergeKLists())