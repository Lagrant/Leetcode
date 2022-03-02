# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        cnt = 1
        cur = head
        rmv_node, rmv_prev = head, None
        while (cnt < n and cur.next is not None):
            cur = cur.next
            cnt += 1

        while (cur.next is not None):
            cur = cur.next
            rmv_prev = rmv_node
            rmv_node = rmv_node.next
        
        if (rmv_prev is not None):
            rmv_prev.next = rmv_node.next
        else:
            head = head.next

        return head