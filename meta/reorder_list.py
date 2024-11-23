from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None or head.next.next is None:
            return
        if head.next.next.next is None:
            n1 = head.next
            n2 = n1.next
            head.next = n2
            n2.next = n1
            n1.next = None
            return
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        midnode = slow

        prev = midnode.next
        cur = prev.next
        prev.next = None
        midnode.next = None
        while cur is not None:
            succ = cur.next
            cur.next = prev
            prev = cur
            cur = succ
        head_r = prev

        cur, cur_r = head, head_r
        while cur is not None and cur_r is not None:
            prev = cur
            cur = cur.next
            prev_r = cur_r
            cur_r = cur_r.next
            prev.next = prev_r
            prev_r.next = cur