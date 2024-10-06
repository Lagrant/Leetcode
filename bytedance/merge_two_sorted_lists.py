# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None and list2 is None:
            return None
        prev = head = cur = ListNode(-101)
        maxv = -101
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                cur.val = list1.val
                list1 = list1.next_
            else:
                cur.val = list2.val
                list2 = list2.next_
            if maxv < cur.val:
                maxv = cur.val
            cur.next_ = ListNode(-101)
            prev = cur
            cur = cur.next_
        
        ll = list1 if list1 is not None else list2
        while ll is not None:
            cur.val = ll.val
            cur.next_ = ListNode(-101)
            prev = cur
            if maxv < cur.val:
                maxv = cur.val
            cur = cur.next_
            ll = ll.next_
        if cur.val < maxv:
            prev.next_ = None
        return head