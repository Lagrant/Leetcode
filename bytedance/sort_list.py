from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h, t = self.sortList1(head)
        return h
    
    def sortList1(self, head: Optional[ListNode]):
        if head is None or head is not None and head.next is None:
            return head, head
        
        cur = head
        piv = cur.next
        prepiv, precur = cur, None
        while piv is not None:
            if cur.val > piv.val:
                prepiv.next = piv.next
                piv.next = head
                if precur is None:
                    precur = piv
                head = piv
                piv = prepiv.next
            else:
                prepiv =piv
                piv = piv.next

        tail = None
        if cur.next is not None:
            curnext, tail = self.sortList1(cur.next)
            cur.next = curnext
        if precur is not None:
            precur.next = None
            head, precur = self.sortList1(head)
            if precur is not None:
                precur.next = cur
            else:
                head = cur
        return head, tail if tail is not None else cur
    
if __name__ == '__main__':
    head = ListNode(3, ListNode(4, ListNode(1)))
    s = Solution()
    print(s.sortList(head))