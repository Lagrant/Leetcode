from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        nodelist = []
        cur = head
        while cur is not None:
            nodelist.append(cur)
            cur = cur.next
        nodelist = self.merge(nodelist)
        cur = head = nodelist[0]
        for i in range(1, len(nodelist)):
            cur.next = nodelist[i]
            cur = cur.next
        cur.next = None
        return head
    
    def merge(self, nodelist):
        if len(nodelist) == 0:
            return []
        if len(nodelist) == 1:
            return nodelist
        if len(nodelist) == 2:
            if nodelist[0].val > nodelist[1].val:
                nodelist[0], nodelist[1] = nodelist[1], nodelist[0]
            return nodelist
        piv = len(nodelist) // 2
        nodelist1 = self.merge(nodelist[:piv])
        nodelist2 = self.merge(nodelist[piv:])
        ndl = []
        i, j = 0, 0
        while i < len(nodelist1) and j < len(nodelist2):
            if nodelist1[i].val < nodelist2[j].val:
                ndl.append(nodelist1[i])
                i += 1
            else:
                ndl.append(nodelist2[j])
                j += 1
        if i < len(nodelist1):
            ndl.extend(nodelist1[i:])
        if j < len(nodelist2):
            ndl.extend(nodelist2[j:])
        return ndl

if __name__ == '__main__':
    head = ListNode(3, ListNode(4, ListNode(1)))
    s = Solution()